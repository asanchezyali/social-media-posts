const { parentPort, workerData } = require("worker_threads");

function computeRangeSum(start, end) {
  let sum = 0;
  for (let i = start; i < end; i++) {
    sum += i;
  }
  return sum;
}

const { start, end } = workerData;
const result = computeRangeSum(start, end);

parentPort.postMessage(result);
