var port = process.env.PORT || 3000,
    http = require('http'),
    fs = require('fs'),
    index = fs.readFileSync('index.html');
    p2 = fs.readFileSync('2puertas.html');
    p3 = fs.readFileSync('3puertas.html');
    var url = require('url');

var server = http.createServer(function (req, res) {
    var path = url.parse(req.url).pathname;
    var fsCallback = function(error, data) {
        if(error) throw error;

        res.writeHead(200);
        res.write(data);
        res.end();
    }
    switch(path){
        case '/1puerta':
            doc = fs.readFile(__dirname + '/index.html', fsCallback);
        break;
        case '/2puertas':
            doc = fs.readFile(__dirname + '/2puertas.html', fsCallback);
        break;
        case '/3puertas':
            doc = fs.readFile(__dirname + '/3puertas.html', fsCallback);
        break;
        case '/index':
            doc = fs.readFile(__dirname + '/index.html', fsCallback);
        break;
        default:
            doc = fs.readFile(__dirname + '/index.html', fsCallback);
        break;
    }
});

// Listen on port 3000, IP defaults to 127.0.0.1
server.listen(port);

// Put a friendly message on the terminal
console.log('Server running at http://127.0.0.1:' + port + '/');
