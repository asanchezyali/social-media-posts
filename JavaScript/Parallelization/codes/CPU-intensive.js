const http = require("http");

function computeIntensive() {
  let result = 0;
  for (let i = 0; i < 1e9; i++) {
    result += i;
  }
  return result;
}

const server = http.createServer((req, res) => {
  if (req.url === "/compute" && req.method === "GET") {
    const result = computeIntensive();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ result }));
  } else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Not Found");
  }
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
