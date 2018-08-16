var express = require("express");
var bodyParser = require("body-parser");
var routes = require("./routes/routes.js");
var app = express();

var http = require('http');

var gunServer = http.createServer();

// Our GUN setup from the last example.
var Gun = require('gun');
var gun = Gun({
    web: gunServer
});

// Start the server on port 8080.
gunServer.listen(8080, function () {
    console.log('Server listening on http://localhost:8080/gun')
})


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

routes(app);

var server = app.listen(3000, function () {
    console.log("app running on port.", server.address().port);
});
