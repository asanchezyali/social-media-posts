// Basic examples of stream types

// Readable Stream
const fs = require('fs');
const readableStream = fs.createReadStream('file.txt');
readableStream.on('data', (chunk) => {
  console.log(`Received ${chunk.length} bytes`);
});

// Writable Stream
const writableStream = fs.createWriteStream('output.txt');
writableStream.write('Hello World\n');
writableStream.end();

// Transform Stream
const { Transform } = require('stream');
const upperCaseTransform = new Transform({
  transform(chunk, encoding, callback) {
    // Convert data to uppercase
    callback(null, chunk.toString().toUpperCase());
  }
});