const Gun = require('gun')
var gun = Gun("http://localhost:8080/gun");


var appRouter = function (app) {
    app.get("/", function (req, res) {
        res.status(200).send("Welcome to our restful API");
    });
app.post("/addEntry", function(req,res){
    console.log(req.body);
    gun.get('mark').put({
        name: "Mark",
        email: "mark@gunDB.io",
    });

    gun.get('mark').on(function (data, key) {
        console.log("update:", data);
    });
    
    res.status(200).send("accepted");
});

}

module.exports = appRouter;