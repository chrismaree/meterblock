const Gun = require('gun')
var gun = Gun("http://localhost:8080/gun");


var appRouter = function (app) {
    app.get("/", function (req, res) {
        res.status(200).send("Welcome to our restful API");
    });
app.post("/addEntry", function(req,res){
    console.log(req.body);
    gun.get(req.body.key).put(req.body.value);    
    res.status(200).send();
});

}

module.exports = appRouter;