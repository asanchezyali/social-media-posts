const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  if (req.url === '/video' && req.method === 'GET') {
    const videoPath = './video.mp4';
    const stat = fs.statSync(videoPath);
    
    res.writeHead(200, {
      'Content-Length': stat.size,
      'Content-Type': 'video/mp4'
    });
    
    // Stream the file directly to the response
    fs.createReadStream(videoPath).pipe(res);
  } else {
    res.writeHead(404);
    res.end('Resource not found');
  }
});

server.listen(3001, () => {
  console.log('Server running at http://localhost:3001/');
});