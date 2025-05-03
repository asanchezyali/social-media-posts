// --- 08_async_await_basics.js ---
// Simulating an API call that returns user data
async function fetchUserData(userId) {
  console.log(`Fetching user data for ID: ${userId}...`);
  
  // Simulate API delay
  await new Promise(resolve => setTimeout(resolve, 1000));
  
  // Simulate success/failure
  if (userId <= 0) {
    throw new Error('Invalid user ID');
  }
  
  return {
    id: userId,
    name: 'Alex',
    email: `user${userId}@example.com`
  };
}

// Using async/await with try/catch
async function displayUserProfile(userId) {
  console.log('Starting user profile retrieval...');
  
  try {
    const userData = await fetchUserData(userId);
    console.log('User data retrieved successfully:');
    console.log(userData);
  } catch (error) {
    console.error('Error fetching user data:', error.message);
  }
  
  console.log('Profile display operation completed.');
}

// Execute our async function
console.log('Before calling async function');
displayUserProfile(123)
  .then(() => console.log('Async operation chain completed.'));
console.log('After calling async function (executes immediately)');

// Try with an invalid ID to see error handling
setTimeout(() => {
  console.log('\nTrying with invalid ID:');
  displayUserProfile(-1);
}, 2000);