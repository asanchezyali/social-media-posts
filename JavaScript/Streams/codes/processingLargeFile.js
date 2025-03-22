const fs = require('fs');
const csv = require('csv-parser');

// Process a large CSV file line by line
fs.createReadStream('huge-data.csv')
  .pipe(csv())
  .on('data', (row) => {
    // Process each row without loading the entire file
    console.log(row);
  })
  .on('end', () => {
    console.log('Processing complete');
  });