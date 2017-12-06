const HELLO_WORLD = 'hello world';
console.log()

debugger

const http = require('http');

const hostname = '0.0.0.0';
const port = 80;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.end(`
    <h2>Hello World\n</h2>
    <hr>
    <p>JUST WELL: ${process.env['SHIT']}</p>`);
  });

server.on("request", function (req){
  console.log(req.headers['user-agent'])
})
server.listen(port, hostname, () => {
  console.log(`Node js server running at http://${hostname}:${port}/`);
});
