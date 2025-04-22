// --- 05_promise_race.js ---
// Simulates searching for a product across different services with varying times
function searchAmazon(productName) {
  console.log(`Searching for "${productName}" on Amazon...`);
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`Amazon responded`);
      resolve({
        source: 'Amazon',
        price: 29.99,
        inStock: true
      });
    }, 1500 + Math.random() * 1000); // 1.5-2.5 seconds
  });
}

function searchEbay(productName) {
  console.log(`Searching for "${productName}" on eBay...`);
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`eBay responded`);
      resolve({
        source: 'eBay',
        price: 26.50,
        inStock: true
      });
    }, 800 + Math.random() * 2000); // 0.8-2.8 seconds
  });
}

function searchLocalStore(productName) {
  console.log(`Searching for "${productName}" in local store...`);
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`Local store responded`);
      resolve({
        source: 'Local Store',
        price: 32.99,
        inStock: true
      });
    }, 500 + Math.random() * 1000); // 0.5-1.5 seconds
  });
}

// Adding a timeout to cancel if all searches take too long
function timeout(ms) {
  return new Promise((_, reject) => {
    setTimeout(() => {
      reject(new Error(`Timeout after ${ms}ms`));
    }, ms);
  });
}

const productName = "Bluetooth Headphones";
console.log(`\nSearching for the best price for: ${productName}`);
console.time('Search time');

// Race between sources and a timeout
Promise.race([
  searchAmazon(productName),
  searchEbay(productName),
  searchLocalStore(productName),
  timeout(2000) // Cancel after 2 seconds
])
  .then(result => {
    console.log(`\nWe have a winner!`);
    console.log(`${result.source} was the fastest to respond`);
    console.log(`Price: $${result.price}`);
    console.timeEnd('Search time');
  })
  .catch(error => {
    console.error(`\nError: ${error.message}`);
    console.timeEnd('Search time');
  });

console.log('\nSearch in progress across all sources...');