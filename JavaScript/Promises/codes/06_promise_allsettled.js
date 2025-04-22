// --- 06_promise_allsettled.js ---
// We simulate different network operations that may succeed or fail
function fetchDataFromServer(serverId) {
  return new Promise((resolve, reject) => {
    const serverSuccessRate = {
      'EU': 0.95, // 95% success rate
      'US': 0.98, // 98% success rate
      'ASIA': 0.85, // 85% success rate
    };
    
    setTimeout(() => {
      // Simulate success or failure based on predefined rates
      const success = Math.random() < (serverSuccessRate[serverId] || 0.5);
      if (success) {
        resolve({
          serverId,
          data: `Data from server ${serverId}`,
          timestamp: new Date().toISOString()
        });
      } else {
        reject(new Error(`Error connecting to server ${serverId}`));
      }
    }, 1000 + Math.random() * 1000);
  });
}

const serverRequests = [
  fetchDataFromServer('EU'),
  fetchDataFromServer('US'),
  fetchDataFromServer('ASIA'),
  // Adding a promise that will always fail to demonstrate
  new Promise((_, reject) => setTimeout(() => reject(new Error('Server offline')), 1500)),
];

console.log('Requesting data from multiple servers...\n');

Promise.allSettled(serverRequests)
  .then(results => {
    console.log('All requests completed (successful or failed)');
    
    // Count successful and failed results
    const fulfilled = results.filter(r => r.status === 'fulfilled');
    const rejected = results.filter(r => r.status === 'rejected');
    
    console.log(`\nResults: ${fulfilled.length} successful, ${rejected.length} failed`);
    
    // Processing successful results
    console.log('\nRetrieved data:');
    fulfilled.forEach((result, index) => {
      console.log(`${index + 1}. Server ${result.value.serverId}: ${result.value.data}`);
    });
    
    // Logging errors
    console.log('\nErrors found:');
    rejected.forEach((result, index) => {
      console.log(`${index + 1}. Error: ${result.reason.message}`);
    });
  });

console.log('Code continues to execute while requests are being processed...');