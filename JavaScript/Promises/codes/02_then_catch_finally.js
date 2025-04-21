// --- 02_then_catch_finally.js ---
// How to run:
// 1. Open your browser's developer console (usually F12).
// 2. Paste this entire code block and press Enter.
// OR
// 3. Save this code as 02_then_catch_finally.js.
// 4. Open your terminal and run: node 02_then_catch_finally.js

console.log("Creating a promise...");

const myDataPromise = new Promise((resolve, reject) => {
  console.log("Executor: Simulating fetching data...");
  const success = Math.random() > 0.3; // Higher chance of success

  setTimeout(() => {
    if (success) {
      const userData = { id: 123, name: "Alex", email: "alex@example.com" };
      console.log("Executor: Data fetched! Resolving...");
      resolve(userData);
    } else {
      const error = new Error("Network Error: Could not fetch user data.");
      console.log("Executor: Failed to fetch data. Rejecting...");
      reject(error);
    }
  }, 1500); // Simulate 1.5 seconds delay
});

console.log("Promise created. Waiting for it to settle...");

// --- Handling the Promise --- 

myDataPromise
  .then((data) => {
    // This function runs ONLY if the promise is resolved (successful)
    console.log("\n.then() block executed:");
    console.log("Received data:", data);
    console.log(`Welcome, ${data.name}!`);
    // You can return a value here to be used in the next .then() (chaining - next topic!)
    return data.id;
  })
  .catch((error) => {
    // This function runs ONLY if the promise is rejected (failed)
    console.error("\n.catch() block executed:");
    console.error("An error occurred:", error.message);
    // Handle the error gracefully, maybe show a message to the user
    // You can also return a default value or re-throw the error
  })
  .finally(() => {
    // This function runs ALWAYS, whether the promise was resolved or rejected
    console.log("\n.finally() block executed:");
    console.log("Promise has settled (either resolved or rejected). Cleanup can happen here.");
  });

console.log("\nPromise handler (.then, .catch, .finally) attached.");
console.log("Execution continues while waiting for the promise...");

// Note: The logs from .then/.catch/.finally will appear *after* the last console.log here,
// because the promise takes time to settle (due to setTimeout).
