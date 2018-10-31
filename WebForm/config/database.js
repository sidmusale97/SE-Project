const mysql = require('mysql');

var dbData = {host: 'se-project.cqeckwiwnfhm.us-east-2.rds.amazonaws.com',
user: 'root',
password: '12345678',
database: 'se'}
var con = mysql.createConnection(dbData);

con.connect((err) => {
    if (err) throw err;
    else{
        console.log("connected");
    }
});
module.exports = {
    database : con,
    dbData: dbData
}