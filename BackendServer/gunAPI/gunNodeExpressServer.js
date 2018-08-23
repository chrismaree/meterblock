var express = require("express");
var bodyParser = require("body-parser");
var routes = require("./routes/routes.js");
var app = express();

var http = require('http');
var gunServer = http.createServer();


var Gun = require('gun');
var gun = Gun({
    file: 'db/data.json',
    web: gunServer,
    radisk: false,
    localStorage: true
});


// Start the server on port 8080.
gunServer.listen(8080, function () {
    console.log('Server lcaistening on http://localhost:8080/gun')
})


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

routes(app);

var server = app.listen(3000, function () {
    console.log("app running on port.", server.address().port);
});
