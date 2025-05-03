// --- 11_real_world_examples.js ---
// Example 1: API Request with Timeout and Retry
async function fetchWithTimeout(url, timeout = 5000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);
  
  try {
    const response = await fetch(url, { signal: controller.signal });
    const data = await response.json();
    return data;
  } finally {
    clearTimeout(timeoutId);
  }
}

async function fetchWithRetry(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await fetchWithTimeout(url);
    } catch (error) {
      if (i === retries - 1) throw error;
      await new Promise(resolve => 
        setTimeout(resolve, Math.pow(2, i) * 1000)
      );
    }
  }
}

// Example 2: Resource Pool
class ResourcePool {
  constructor(factory, poolSize = 5) {
    this.resources = Array(poolSize).fill(null);
    this.factory = factory;
    this.available = [...Array(poolSize).keys()];
    this.waiting = [];
  }
  
  async acquire() {
    if (this.available.length > 0) {
      const index = this.available.pop();
      if (!this.resources[index]) {
        this.resources[index] = await this.factory();
      }
      return { resource: this.resources[index], index };
    }
    
    return new Promise(resolve => {
      this.waiting.push(resolve);
    });
  }
  
  release({ resource, index }) {
    if (this.waiting.length > 0) {
      const resolve = this.waiting.shift();
      resolve({ resource, index });
    } else {
      this.available.push(index);
    }
  }
}

// Example 3: Batch Processing with Rate Limiting
async function processBatch(items, batchSize = 3, delay = 1000) {
  const results = [];
  
  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize);
    const batchResults = await Promise.all(
      batch.map(item => processItem(item))
    );
    results.push(...batchResults);
    
    if (i + batchSize < items.length) {
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
  
  return results;
}

// Example 4: Event to Promise conversion
function eventToPromise(emitter, successEvent, errorEvent) {
  return new Promise((resolve, reject) => {
    const success = (...args) => {
      cleanup();
      resolve(...args);
    };
    
    const error = (...args) => {
      cleanup();
      reject(...args);
    };
    
    const cleanup = () => {
      emitter.removeListener(successEvent, success);
      emitter.removeListener(errorEvent, error);
    };
    
    emitter.on(successEvent, success);
    emitter.on(errorEvent, error);
  });
}

// Example usage for demonstration
async function demonstrateExamples() {
  // Example 1: API Request with Timeout and Retry
  try {
    const data = await fetchWithRetry('https://api.example.com/data');
    console.log('API Response:', data);
  } catch (error) {
    console.error('API Error:', error);
  }
  
  // Example 2: Resource Pool
  const pool = new ResourcePool(async () => {
    await new Promise(resolve => setTimeout(resolve, 100));
    return { id: Math.random() };
  });
  
  // Use multiple resources concurrently
  const operations = Array(8).fill().map(async (_, i) => {
    const { resource, index } = await pool.acquire();
    console.log(`Using resource ${resource.id} at index ${index}`);
    await new Promise(resolve => setTimeout(resolve, 200));
    pool.release({ resource, index });
    return `Operation ${i} complete`;
  });
  
  const results = await Promise.all(operations);
  console.log('Resource pool results:', results);
  
  // Example 3: Batch Processing
  const items = Array(10).fill().map((_, i) => ({ id: i }));
  const batchResults = await processBatch(items);
  console.log('Batch processing results:', batchResults);
  
  // Example 4: Event to Promise
  const EventEmitter = require('events');
  const emitter = new EventEmitter();
  
  // Simulate an async event
  setTimeout(() => emitter.emit('success', 'Operation completed'), 500);
  
  const result = await eventToPromise(emitter, 'success', 'error');
  console.log('Event result:', result);
}

// Simulated processItem function for the batch processing example
async function processItem(item) {
  await new Promise(resolve => setTimeout(resolve, 100));
  return { ...item, processed: true };
}

// Run the examples if this file is executed directly
if (require.main === module) {
  demonstrateExamples().catch(console.error);
}