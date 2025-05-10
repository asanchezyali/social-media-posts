// --- 10_best_practices.js ---
// [BAD] WRONG: Not handling errors
async function wrongErrorHandling() {
  const data = await riskyOperation(); // Unhandled promise rejection!
}

// [GOOD] RIGHT: Proper error handling
async function rightErrorHandling() {
  try {
    const data = await riskyOperation();
    return data;
  } catch (error) {
    console.error('Operation failed:', error);
    throw error; // Re-throw if you want callers to handle it
  }
}

// [BAD] WRONG: Sequential when parallel is possible
async function wrongSequential() {
  const users = await fetchUsers();
  const posts = await fetchPosts();
  const comments = await fetchComments();
}

// [GOOD] RIGHT: Parallel execution when possible
async function rightParallel() {
  const [users, posts, comments] = await Promise.all([
    fetchUsers(),
    fetchPosts(),
    fetchComments()
  ]);
}

// [BAD] WRONG: await in a loop
async function wrongLoop() {
  const ids = [1, 2, 3, 4, 5];
  const results = [];
  for (const id of ids) {
    results.push(await fetchData(id)); // Sequential execution
  }
}

// [GOOD] RIGHT: Map and Promise.all
async function rightLoop() {
  const ids = [1, 2, 3, 4, 5];
  const results = await Promise.all(
    ids.map(id => fetchData(id))
  );
}

// [BAD] WRONG: Not considering race conditions
let data;
async function wrongRaceCondition() {
  data = await fetchData(); // Global state modification
}

// [GOOD] RIGHT: Proper state management
class DataManager {
  constructor() {
    this.data = null;
    this.loading = false;
  }
  
  async fetchData() {
    if (this.loading) return this.data;
    
    this.loading = true;
    try {
      this.data = await fetchData();
      return this.data;
    } finally {
      this.loading = false;
    }
  }
}