const { Worker } = require("worker_threads");
const os = require("os");

// Determine available CPU cores
const numCPUs = os.cpus().length;

function runWorker(workerData) {
  return new Promise((resolve, reject) => {
    const worker = new Worker("./worker.js", { workerData });
    worker.on("message", resolve);
    worker.on("error", reject);
    worker.on("exit", (code) => {
      if (code !== 0) reject(new Error(`Worker stopped with code ${code}`));
    });
  });
}

async function main() {
  try {
    console.time("parallel-execution");

    // Create a worker for each CPU core
    const workers = Array(numCPUs)
      .fill()
      .map((_, index) => {
        return runWorker({
          start: index * 250000000,
          end: (index + 1) * 250000000,
        });
      });

    // Wait for all workers to complete
    const results = await Promise.all(workers);
    const finalResult = results.reduce((sum, current) => sum + current, 0);

    console.timeEnd("parallel-execution");
    console.log(`Final sum: ${finalResult}`);
  } catch (err) {
    console.error("Error:", err);
  }
}

main();
