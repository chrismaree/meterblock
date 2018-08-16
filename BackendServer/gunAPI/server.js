/* server.js */

// import the native http module
var http = require('http')

// import gun
var Gun = require('gun')

var server = http.createServer(function (req, res) {
    if (Gun.serve(req, res)) {
        return
    }
});

// start listening for requests on `localhost:8080`
server.listen(8080)