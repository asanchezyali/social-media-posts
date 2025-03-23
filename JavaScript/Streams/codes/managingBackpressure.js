const fs = require('fs');

const readableStream = fs.createReadStream('large-file.dat');
const writableStream = fs.createWriteStream('destination.dat');

readableStream.on('data', (chunk) => {
  // write() returns false when internal buffer is full
  const canWrite = writableStream.write(chunk);
  
  if (!canWrite) {
    // Pause the readable stream until the writable drains
    readableStream.pause();
    
    // Resume when the writable can accept more data
    writableStream.once('drain', () => {
      readableStream.resume();
    });
  }
});

readableStream.on('end', () => {
  writableStream.end();
});