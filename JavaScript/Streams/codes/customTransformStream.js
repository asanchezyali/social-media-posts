const { Transform } = require('stream');

// Stream to filter lines containing a keyword
class LineFilter extends Transform {
  constructor(keyword) {
    super();
    this.keyword = keyword;
    this.incomplete = '';
  }
  
  _transform(chunk, encoding, callback) {
    // Convert chunk to string and combine with previous data
    const data = this.incomplete + chunk.toString();
    // Split by lines
    const lines = data.split('\n');
    // Save the last line for the next chunk
    this.incomplete = lines.pop();
    
    // Filter and send lines containing the keyword
    for (const line of lines) {
      if (line.includes(this.keyword)) {
        this.push(line + '\n');
      }
    }
    callback();
  }
  
  _flush(callback) {
    // Process any remaining data
    if (this.incomplete && this.incomplete.includes(this.keyword)) {
      this.push(this.incomplete + '\n');
    }
    callback();
  }
}