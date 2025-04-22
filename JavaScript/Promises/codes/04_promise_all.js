// --- 04_promise_all.js ---
// Simulates API requests for different resources
function fetchUserData(userId) {
  console.log(`Requesting user data ${userId}...`);
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`User data ${userId} received`);
      resolve({ id: userId, name: `User ${userId}`, email: `user${userId}@example.com` });
    }, 1000 + Math.random() * 1000); // Random time between 1-2 seconds
  });
}

function fetchUserPosts(userId) {
  console.log(`Requesting posts for user ${userId}...`);
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`Posts for user ${userId} received`);
      resolve([
        { id: 1, title: `Post 1 from user ${userId}` },
        { id: 2, title: `Post 2 from user ${userId}` }
      ]);
    }, 1200 + Math.random() * 1000); // Random time between 1.2-2.2 seconds
  });
}

function fetchUserFollowers(userId) {
  console.log(`Requesting followers for user ${userId}...`);
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`Followers for user ${userId} received`);
      resolve([101, 102, 103]);
    }, 800 + Math.random() * 1000); // Random time between 0.8-1.8 seconds
  });
}

console.time('Total loading time');

// Using Promise.all to execute all requests in parallel
const userId = 42;
Promise.all([
  fetchUserData(userId),
  fetchUserPosts(userId),
  fetchUserFollowers(userId)
])
  .then(([userData, userPosts, userFollowers]) => {
    console.log('\nAll data was successfully loaded!');
    console.log('User data:', userData);
    console.log('Posts:', userPosts);
    console.log('Followers:', userFollowers.length);
    
    console.timeEnd('Total loading time');
  })
  .catch(error => {
    console.error('Error loading data:', error);
    console.timeEnd('Total loading time');
  });

console.log('\nRequesting all data in parallel...');