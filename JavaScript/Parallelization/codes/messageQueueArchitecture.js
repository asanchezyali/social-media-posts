const Queue = require("bull");
const workQueue = new Queue("data-processing", {
  redis: { host: "localhost", port: 6379 },
});

// Set up the worker to process jobs
workQueue.process("process-chunk", async (job) => {
  const { chunkId, data } = job.data;
  console.log(`Processing chunk ${chunkId} with ${data.length} items`);
  
  // Simulate processing time
  await new Promise(resolve => setTimeout(resolve, 100));
  
  // Do actual processing here
  const results = data.map(item => ({
    ...item,
    processed: true,
    result: item.value * 2
  }));
  
  console.log(`Completed processing chunk ${chunkId}`);
  return { processedCount: results.length };
});

// Listen for completed jobs
workQueue.on('completed', (job, result) => {
  console.log(`Job ${job.id} completed with result:`, result);
});

// Listen for failed jobs
workQueue.on('failed', (job, err) => {
  console.error(`Job ${job.id} failed with error:`, err);
});

async function distributeWork(dataset, chunkSize = 1000) {
  const chunks = [];
  for (let i = 0; i < dataset.length; i += chunkSize) {
    chunks.push(dataset.slice(i, i + chunkSize));
  }
  
  console.log(`Distributing ${chunks.length} tasks`);
  
  const jobPromises = chunks.map((chunk, index) => {
    return workQueue.add(
      "process-chunk",
      {
        chunkId: index,
        data: chunk,
        timestamp: Date.now(),
      },
      {
        attempts: 3,
      }
    );
  });
  
  await Promise.all(jobPromises);
  console.log("All tasks queued for processing");
  
  // To wait for all jobs to complete
  return new Promise((resolve) => {
    let completedCount = 0;
    const totalJobs = chunks.length;
    
    const completionListener = (job) => {
      completedCount++;
      console.log(`Progress: ${completedCount}/${totalJobs} chunks processed`);
      
      if (completedCount === totalJobs) {
        workQueue.removeListener('completed', completionListener);
        console.log("All tasks have been processed!");
        resolve();
      }
    };
    
    workQueue.on('completed', completionListener);
  });
}

// Simulate a large dataset
const mockData = Array.from({ length: 10000 }, (_, i) => ({ id: i, value: Math.random() }));

// Main execution
async function main() {
  try {
    await distributeWork(mockData, 1000);
    
    // This code will execute only after all jobs are completed
    console.log("Work distribution and processing complete!");
    
    // Clean up resources
    await workQueue.close();
  } catch (error) {
    console.error("Error occurred:", error);
  }
}

main();