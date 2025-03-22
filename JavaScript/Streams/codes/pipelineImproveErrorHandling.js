const { pipeline } = require('stream');
const fs = require('fs');
const zlib = require('zlib');

// Using pipeline for better error handling
pipeline(
  fs.createReadStream('file.txt'),
  zlib.createGzip(),
  fs.createWriteStream('output.gz'),
  (err) => {
    if (err) {
      console.error('Pipeline failed', err);
    } else {
      console.log('Pipeline succeeded');
    }
  }
);