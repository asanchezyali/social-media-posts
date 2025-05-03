// --- 09_error_handling_patterns.js ---
// Simulating database operations
async function connectToDatabase() {
  console.log('Connecting to database...');
  await new Promise(resolve => setTimeout(resolve, 500));
  return { connected: true };
}

async function queryDatabase(connection, query) {
  console.log(`Executing query: ${query}`);
  await new Promise(resolve => setTimeout(resolve, 800));
  
  if (!connection.connected) {
    throw new Error('Database connection lost');
  }
  
  if (query.includes('invalid')) {
    throw new Error('Invalid SQL query');
  }
  
  return [`Result 1 for ${query}`, `Result 2 for ${query}`];
}

async function processResults(results) {
  console.log('Processing results...');
  await new Promise(resolve => setTimeout(resolve, 300));
  return results.map(r => r.toUpperCase());
}

// Pattern 1: Sequential operations with proper cleanup
async function performDatabaseOperation(query) {
  let connection = null;
  
  try {
    // Establish connection
    connection = await connectToDatabase();
    
    // Execute query
    const results = await queryDatabase(connection, query);
    
    // Process results
    const processedResults = await processResults(results);
    
    return processedResults;
  } catch (error) {
    console.error('Operation failed:', error.message);
    throw error; // Re-throw to let caller handle it
  } finally {
    if (connection) {
      console.log('Closing database connection...');
      connection.connected = false;
    }
  }
}

// Pattern 2: Parallel operations with Promise.all
async function executeMultipleQueries(queries) {
  try {
    const connection = await connectToDatabase();
    
    console.log('Executing queries in parallel...');
    const results = await Promise.all(
      queries.map(query => queryDatabase(connection, query))
    );
    
    const processedResults = await Promise.all(
      results.map(result => processResults(result))
    );
    
    return processedResults;
  } catch (error) {
    console.error('Batch operation failed:', error.message);
    throw error;
  }
}

// Pattern 3: Retry mechanism
async function executeWithRetry(operation, maxAttempts = 3) {
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await operation();
    } catch (error) {
      if (attempt === maxAttempts) throw error;
      
      console.log(`Attempt ${attempt} failed, retrying...`);
      await new Promise(resolve => 
        setTimeout(resolve, Math.pow(2, attempt) * 100)
      );
    }
  }
}

// Demo the patterns
async function demonstratePatterns() {
  console.log('--- Pattern 1: Sequential with Cleanup ---');
  try {
    const results = await performDatabaseOperation('SELECT * FROM users');
    console.log('Success:', results);
  } catch (error) {
    console.log('Handler caught:', error.message);
  }
  
  console.log('\n--- Pattern 2: Parallel Operations ---');
  try {
    const queries = [
      'SELECT * FROM users',
      'SELECT * FROM posts',
      'SELECT * FROM comments'
    ];
    const results = await executeMultipleQueries(queries);
    console.log('Batch results:', results);
  } catch (error) {
    console.log('Batch handler caught:', error.message);
  }
  
  console.log('\n--- Pattern 3: Retry Mechanism ---');
  let failCount = 0;
  const unreliableOperation = async () => {
    failCount++;
    if (failCount < 3) throw new Error('Temporary failure');
    return 'Operation succeeded!';
  };
  
  try {
    const result = await executeWithRetry(unreliableOperation);
    console.log('Final result:', result);
  } catch (error) {
    console.log('Retry handler caught:', error.message);
  }
}

demonstratePatterns();