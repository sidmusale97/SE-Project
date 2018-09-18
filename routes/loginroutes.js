var mysql = require('mysql');

//Establishing connection to DB
var conn = mysql.createConnection({
    host: 'sid1997.cqeckwiwnfhm.us-east-2.rds.amazonaws.com',
    database: 'SE_Project',
    user: 'siddharth',
    password:'sidd1997'
});

conn.connect(function(err){
    if(err){
        console.error("Error connecting " + err.stack);
    }
    console.log('Connected');

});
exports.determine = function(req,res){
    var buttonClicked = req.body.Login;
    if(buttonClicked === 'Log In'){
        res.render(path.join(__dirname, '/'))
    }
}
