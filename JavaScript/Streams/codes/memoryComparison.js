const fs = require('fs');
const { promisify } = require('util');
const readFile = promisify(fs.readFile);

// Simple results storage
const results = { stream: null, noStream: null };

// Function to measure memory usage in MB (using RSS for more accurate measurement)
function getMemoryUsage() {
  return Math.round(process.memoryUsage().rss / 1024 / 1024 * 100) / 100;
}

// 1. Processing WITHOUT streams - loads entire file into memory
async function processWithoutStreams(filePath) {
  const initialMemory = getMemoryUsage();
  console.log(`Memory before loading file: ${initialMemory} MB`);
  
  // Read the entire file into memory
  const data = await readFile(filePath);
  
  const afterLoadMemory = getMemoryUsage();
  console.log(`Memory after loading file: ${afterLoadMemory} MB`);
  console.log(`File size: ${(data.length / 1024 / 1024).toFixed(2)} MB`);
  
  // Process the data (counting lines)
  const lines = data.toString().split('\n');
  
  const finalMemory = getMemoryUsage();
  console.log(`Lines processed: ${lines.length}`);
  console.log(`Final memory usage: ${finalMemory} MB`);
  
  results.noStream = { 
    initial: initialMemory,
    afterLoad: afterLoadMemory,
    max: Math.max(initialMemory, afterLoadMemory, finalMemory), 
    final: finalMemory 
  };
}

// 2. Processing WITH streams - processes the file in chunks
function processWithStreams(filePath) {
  return new Promise((resolve) => {
    const initialMemory = getMemoryUsage();
    console.log(`Memory before starting stream: ${initialMemory} MB`);
    
    let linesCount = 0;
    let maxMemory = initialMemory;
    let incompleteLine = '';
    let chunkCount = 0;
    
    const readStream = fs.createReadStream(filePath, {
      highWaterMark: 16 * 1024 // 16KB chunks
    });
    
    readStream.on('data', (chunk) => {
      chunkCount++;
      
      // Process the chunk
      const data = incompleteLine + chunk.toString();
      const lines = data.split('\n');
      incompleteLine = lines.pop();
      linesCount += lines.length;
      
      // Track memory usage
      const currentMemory = getMemoryUsage();
      maxMemory = Math.max(maxMemory, currentMemory);
    });
    
    readStream.on('end', () => {
      if (incompleteLine) linesCount++;
      const finalMemory = getMemoryUsage();
      
      console.log(`Lines processed: ${linesCount}`);
      console.log(`Total chunks: ${chunkCount}`);
      console.log(`Maximum memory used: ${maxMemory} MB`);
      console.log(`Final memory usage: ${finalMemory} MB`);
      
      results.stream = { 
        initial: initialMemory,
        max: maxMemory, 
        final: finalMemory 
      };
      resolve();
    });

    readStream.on('error', (err) => {
      console.error('Error reading file:', err);
      resolve();
    });
  });
}

// Main comparison function
async function compareMemoryUsage(filePath) {
  // Get file size for display
  try {
    const stats = fs.statSync(filePath);
    const fileSizeMB = (stats.size / (1024 * 1024)).toFixed(2);
    console.log(`\n📂 Processing file: ${filePath} (${fileSizeMB} MB)`);
  } catch (err) {
    console.log(`\n📂 Processing file: ${filePath}`);
  }
  
  // 1. Run with streams
  console.log('\n📊 WITH STREAMS:');
  await processWithStreams(filePath);
  
  // Wait for garbage collection
  console.log('\nWaiting for garbage collection...');
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  // 2. Run without streams
  console.log('\n📊 WITHOUT STREAMS:');
  await processWithoutStreams(filePath);
  
  // Print comparison
  console.log('\n============= MEMORY USAGE COMPARISON =============');
  console.log('| Method        | Maximum Memory | Final Memory  |');
  console.log('|---------------|---------------|---------------|');
  console.log(`| WITHOUT STREAM | ${results.noStream.max.toFixed(2).padStart(7)} MB    | ${results.noStream.final.toFixed(2).padStart(7)} MB    |`);
  console.log(`| WITH STREAM    | ${results.stream.max.toFixed(2).padStart(7)} MB    | ${results.stream.final.toFixed(2).padStart(7)} MB    |`);
  console.log('=================================================');
  
  // Memory increase from initial to after loading the file (non-stream method)
  const memoryIncrease = results.noStream.afterLoad - results.noStream.initial;
  console.log(`\n📈 Loading the entire file increased memory by: ${memoryIncrease.toFixed(2)} MB`);
  
  // Improvement percentage
  const improvement = ((results.noStream.max - results.stream.max) / results.noStream.max * 100).toFixed(2);
  console.log(`\n✅ Streams used ${improvement}% less maximum memory!`);
  
  // Tutorial explanation
  console.log('\n📚 CONCLUSION:');
  console.log('   • Streams process data in small chunks (one at a time)');
  console.log('   • Without streams, the entire file is loaded into memory');
  console.log('   • For large files, streams significantly reduce memory usage');
}

// Run the comparison
const filePath = process.argv[2] || 'file.txt';
compareMemoryUsage(filePath);