// Consumer: Process tasks from the queue
const Queue = require("bull");
const cluster = require("cluster");
const os = require("os");

const workQueue = new Queue("data-processing", {
  redis: { host: "redis-server", port: 6379 },
});

// Use cluster to utilize all CPU cores
if (cluster.isMaster) {
  const numCPUs = os.cpus().length;
  console.log(`Setting up ${numCPUs} workers`);

  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on("exit", (worker) => {
    console.log(`Worker ${worker.process.pid} died. Restarting...`);
    cluster.fork();
  });
} else {
  // Worker process logic
  console.log(`Worker ${process.pid} started`);

  // Process jobs (8 concurrent jobs per worker)
  workQueue.process("process-chunk", 8, async (job) => {
    const { chunkId, data } = job.data;
    await job.progress(10);

    console.log(`Processing chunk ${chunkId}`);
    const startTime = Date.now();

    // Process data (CPU-intensive work)
    const processedData = data.map((item) => {
      let result = 0;
      for (let i = 0; i < 10000; i++) {
        result += Math.sqrt(item.value * i);
      }
      return { ...item, processed: result };
    });

    await job.progress(100);
    const duration = Date.now() - startTime;

    return {
      chunkId,
      processedCount: processedData.length,
      duration,
      workerId: process.pid,
    };
  });
}
