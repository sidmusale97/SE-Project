// written by: Siddharth Musale and Corey Chen
// tested by: Corey Chen
// debugged by: Corey Chen

const express = require('express');
const router = express.Router();
const config = require('../config/database');
const getStatus = require('./parkmap');
var con = config.database;
router.get('/form', (req,res,next) => {
    getStatus(function(data){
        console.log(data);
        res.render('ReservationForm.ejs',{data: data,});
    })
});

router.get('/cancel',(req,res,next)=> {
    res.render('ReservationCancel.ejs');
});
router.get('/success',(req,res,next)=> {
    res.render('ReservationSuccess.ejs');
});
router.get('/cancelled',(req,res,next)=> {
    res.render('ReservationCancelled.ejs');
});

router.post('/create', (req,res,next) => {
    var userID = req.session.userID;
    var time = req.body.datefield;
    var spot = req.body.spotID

    if(userID == null || time == null)
    {
        res.redirect("/reservation/form");
    }
    var query = "INSERT INTO Reservations (userID, DateTime, ParkingSpot) VALUES (" +userID + ",'" + time + "'," + spot + ")";
   // console.log(query);
    con.query(query, (err,result,fields) => {
        if(err)throw err;
        //else{
            console.log('1 doc inserted');
            //res.write('Reservation succuessfully made. Redirecting to main page...');
            // setTimeout(() =>{
               // res.redirect('/users/login/success');
            //}, 2000);
        //}
    });
    res.redirect("/reservation/success");
});

router.post('/cancel', (req,res,next)=> {
    var userID = req.session.userID;
    var time = req.body.datefield;
    
    if(userID == null || time == null){
        res.redirect("/reservation/cancel");
    }
    var query="DELETE FROM Reservations WHERE userID = "+userID+" AND DateTime = '"+time+"'";
    //console.log(query);

    con.query(query, (err,result,fields) => {
        if(err)throw err;
        else{
            console.log('1 doc deleted');
            //res.write('Reservation succuessfully made. Redirecting to main page...');
             setTimeout(() =>{
                //res.redirect('/users/home');
            }, 2000);
        }
    });
    res.redirect('/reservation/cancelled');

});


module.exports = router;