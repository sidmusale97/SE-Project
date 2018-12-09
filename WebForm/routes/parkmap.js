var mysql = require('mysql');
var config = require('../config/database');
var con = config.database;

const getStatus = async function(callback){
    con.connect(function(err) {
       // if (err) throw err;
        con.query("SELECT * FROM ParkingSpots", function (err, result, fields) {
            if (err) throw err;
            //console.log(result);

            
    var spots = "";
    for(i = 0; i < 25; i++){
            if(result[i].Occupied == 1){
                spots = spots.concat("o");  // array entry = 1 means spot is occupied
                //console.log(spots);
            }else if(result[i].Reserved == 1){
                spots = spots.concat("r");  // spot is reserved
                //console.log(spots);
            }else{
                spots = spots.concat("n");  // spot is open
                //console.log(spots);
            }
    }
    //console.log(spots);
    callback(spots);
});
});
}

module.exports = getStatus;