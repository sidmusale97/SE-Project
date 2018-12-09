var mysql = require('mysql');
var config = require('../config/database');
var con = config.database;

var parkingMap = {};
parkingMap.marker = null;

getStatus = function(){

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT * FROM ParkingSpots", function (err, result, fields) {
            if (err) throw err;
            console.log(result);
        });
    });
    
}

getStatus();
