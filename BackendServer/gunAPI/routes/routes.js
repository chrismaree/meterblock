const Gun = require('gun')
var gun = Gun("http://localhost:8080/gun");


function checkContentType(req, res, next) {
    if (!req.is('application/json')) {
        return res.status(400).send({
            ok: false,
            error: "Bad request"
        });
    }

    next();
}

var appRouter = function (app) {

app.post("/addEntry", function(req,res){
    console.log(req.body);
    var newRecord = gun.get(req.body.time).put(req.body.value)
    var meterRecords = gun.get(req.body.key)
    meterRecords.set(newRecord)
    
    
    meterRecords.map().once(function (person) {
        console.log("The record is", person);
    });
    
        
    res.status(200).send();
});

}

module.exports = appRouter;