// --- 07_promise_any.js ---
// Simulate loading images from different CDNs with varying times and reliability
function loadImageFromCDN(cdnName, reliability = 1.0) {
  console.log(`Attempting to load image from ${cdnName}...`);
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // Simulate success or failure based on reliability factor
      const success = Math.random() <= reliability;
      
      if (success) {
        console.log(`${cdnName}: Image loaded successfully`);
        resolve({
          cdn: cdnName,
          url: `https://${cdnName.toLowerCase()}.example.com/image.jpg`,
          loadTime: Math.floor(Date.now() - startTime) + 'ms'
        });
      } else {
        console.log(`${cdnName}: Error loading image`);
        reject(new Error(`Error loading from ${cdnName}`));
      }
    }, 1000 + Math.random() * 2000); // 1-3 seconds
  });
}

const startTime = Date.now();
console.log('Starting image loading from multiple CDNs...\n');

// Try loading from various CDNs with different reliability
Promise.any([
  loadImageFromCDN('PrimeCDN', 0.7),    // 70% reliability
  loadImageFromCDN('FastNetwork', 0.5), // 50% reliability
  loadImageFromCDN('BackupCDN', 0.9)    // 90% reliability
])
  .then(result => {
    console.log(`\nImage loaded successfully!`);
    console.log(`Source: ${result.cdn}`);
    console.log(`URL: ${result.url}`);
    console.log(`Load time: ${result.loadTime}`);
  })
  .catch(error => {
    // AggregateError is a new type that groups all errors when all promises fail
    console.error('\nNo CDN could load the image');
    console.error(`Errors found: ${error.errors.length}`);
    error.errors.forEach((err, i) => {
      console.error(`  ${i + 1}. ${err.message}`);
    });
  });

console.log('Attempting to load the image...');