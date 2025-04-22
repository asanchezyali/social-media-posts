// --- 03_promise_chaining.js ---
// Simulates retrieving a user ID from a database
function getUserId(username) {
  console.log(`Looking up ID for user: ${username}...`);
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // Simulates database lookup
      if (username.toLowerCase() === 'alejandro') {
        resolve(123);
      } else {
        reject(new Error('User not found'));
      }
    }, 1000);
  });
}

// Simulates retrieving profile details based on an ID
function getUserProfile(userId) {
  console.log(`Getting profile for ID: ${userId}...`);
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // Simulates database lookup
      resolve({
        id: userId,
        name: 'Alejandro',
        role: 'Developer',
        city: 'Medellín'
      });
    }, 1000);
  });
}

// Simulates checking permissions for a profile
function checkPermissions(userProfile) {
  console.log(`Verifying permissions for: ${userProfile.name}...`);
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (userProfile.role === 'Developer') {
        resolve({
          ...userProfile,
          permissions: ['read', 'write', 'deploy']
        });
      } else {
        resolve({
          ...userProfile,
          permissions: ['read']
        });
      }
    }, 800);
  });
}

// Using promise chaining
console.log("Starting authentication flow...");
getUserId('Alejandro')
  .then(userId => {
    console.log(`User ID found: ${userId}`);
    return getUserProfile(userId); // Returns a new promise
  })
  .then(userProfile => {
    console.log(`Profile obtained:`, userProfile);
    return checkPermissions(userProfile); // Returns another promise
  })
  .then(profileWithPermissions => {
    console.log(`Authentication complete!`);
    console.log(`User ${profileWithPermissions.name} has permissions: ${profileWithPermissions.permissions.join(', ')}`);
  })
  .catch(error => {
    console.error(`Error in process: ${error.message}`);
  })
  .finally(() => {
    console.log("Authentication process finished.");
  });

console.log("Code continues to run while promises resolve...");