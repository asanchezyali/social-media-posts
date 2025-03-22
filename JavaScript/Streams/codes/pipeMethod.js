const fs = require('fs');
const zlib = require('zlib');

// Creating a pipeline using pipe()
fs.createReadStream('file.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('file.txt.gz'))
  .on('finish', () => {
    console.log('Compression completed');
  });