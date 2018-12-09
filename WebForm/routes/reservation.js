const express = require('express');
const router = express.Router();
var mongodb = require('mongodb').MongoClient;
const config = require('../config/database');

var con = config.database;
router.get('/form', (req,res,next) => {
    res.render('ReservationForm.ejs');
    
});

router.post('/create', (req,res,next) => {
    var userID = req.session.userID;
    var time = req.body.datefield;

    if(userID == null || time == null)
    {
        res.redirect("/reservation/form");
    }
    var query = "INSERT INTO Reservations (userID, DateTime) VALUES ('" +userID + "','" + time + "')";
    con.query(query, (err,result,fields) => {
        if(err)throw err;
        else{
            console.log('1 doc inserted');
            //res.write('Reservation succuessfully made. Redirecting to main page...');
             setTimeout(() =>{
                res.redirect('/users/login/success');
            }, 2000);
        }
    });
});

router.post('/cancel', (req,res,next)=> {
    var userID = req.session.userID;
    var time = req.body.datefield;
    
    if(userID == null || time == null){
        res.redirect("/reservation/cancel");
    }

    con.query("DELETE FROM Reservations WHERE userID = ?",[userID], (err,result,fields) => {
        if(err)throw err;
        else{
            console.log('1 doc deleted');
            //res.write('Reservation succuessfully made. Redirecting to main page...');
             setTimeout(() =>{
                res.redirect('/users/profile');
            }, 2000);
        }
    });
});


module.exports = router;