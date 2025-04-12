const Queue = require("bull");

const workQueue = new Queue("data-processing", {
  redis: { host: "localhost", port: 6379 },
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
}

// Simulate a large dataset
// This could be any data source, like a database or an API
const mockData = Array.from({ length: 10000 }, (_, i) => ({ id: i, value: Math.random() }));

distributeWork(mockData, 1000);
