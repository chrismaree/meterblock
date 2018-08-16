var express = require("express");
var bodyParser = require("body-parser");
var routes = require("./routes/routes.js");
var app = express();

var http = require('http')
var Gun = require('gun')

var gunServer = http.createServer(function (req, res) {
    if (Gun.serve(req, res)) {
        return
    }
});

gunServer.listen(8080)


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

routes(app);

var server = app.listen(3000, function () {
    console.log("app running on port.", server.address().port);
});
