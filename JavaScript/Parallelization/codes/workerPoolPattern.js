const { Worker } = require("worker_threads");
const os = require("os");

class WorkerPool {
  constructor(workerScript, numWorkers = os.cpus().length) {
    this.workerScript = workerScript;
    this.numWorkers = numWorkers;
    this.workers = [];
    this.freeWorkers = [];
    this.taskQueue = [];
    this.tasks = {};
    this.taskIdCounter = 0;

    this._initPool();
  }

  _initPool() {
    // Create worker threads
    for (let i = 0; i < this.numWorkers; i++) {
      const worker = new Worker(this.workerScript);
      this.workers.push(worker);
      this.freeWorkers.push(i);

      worker.on("message", (result) => {
        const { taskId, data } = result;

        // Resolve the promise for this task
        if (this.tasks[taskId]) {
          this.tasks[taskId].resolve(data);
          delete this.tasks[taskId];
        }

        // Add worker back to the pool
        this.freeWorkers.push(i);
        this._processQueue();
      });
    }
  }

  executeTask(taskData) {
    return new Promise((resolve, reject) => {
      const taskId = this.taskIdCounter++;

      this.tasks[taskId] = { resolve, reject, taskData };
      this.taskQueue.push(taskId);
      this._processQueue();
    });
  }

  _processQueue() {
    if (this.taskQueue.length > 0 && this.freeWorkers.length > 0) {
      const taskId = this.taskQueue.shift();
      const workerId = this.freeWorkers.shift();

      this.workers[workerId].postMessage({
        taskId,
        data: this.tasks[taskId].taskData,
      });
    }
  }
}
