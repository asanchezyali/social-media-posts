// --- 01_creating_promise.js ---
// How to run:
// 1. Open your browser's developer console (usually F12).
// 2. Paste this entire code block and press Enter.
// OR
// 3. Save this code as 01_creating_promise.js.
// 4. Open your terminal and run: node 01_creating_promise.js

console.log("Creating a promise...");

// A promise takes a function (the 'executor') with two arguments: resolve and reject.
const myFirstPromise = new Promise((resolve, reject) => {
  console.log("Executor function started (simulating async work)...");
  const success = Math.random() > 0.5; // Simulate success or failure randomly

  // Simulate an asynchronous operation (like fetching data) using setTimeout
  setTimeout(() => {
    if (success) {
      const data = { message: "Yay! Data fetched successfully!" };
      console.log("Async work finished: Resolving the promise.");
      resolve(data); // If successful, call resolve with the result
    } else {
      const error = new Error("Oops! Something went wrong.");
      console.log("Async work finished: Rejecting the promise.");
      reject(error); // If failed, call reject with an error
    }
  }, 2000); // Simulate a 2-second delay
});

console.log("Promise created. It's now 'pending'.");

// We'll see how to handle the result (resolve/reject) in the next example!
// For now, this just shows the creation and the state changes.

// You might see 'undefined' logged after 'Promise created...'
// That's the return value of the last console.log, not related to the promise itself.
