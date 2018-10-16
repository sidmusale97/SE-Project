const express = require('express');
const router = express.Router();
var mongodb = require('mongodb').MongoClient;
const config = require('../config/database');

router.get('/form', (req,res,next) => {
    res.render('ReservationForm.ejs');
});

router.post('/create', (req,res,next) => {
    mongodb.connect(config.database, {useNewUrlParser: true}, (err,db) =>{
        if(err)throw err;
        else{
            console.log('connected');
        }
        var dbo = db.db('SE_Project');
        var Username = req.session.Username;
        var time = req.body.datefield;

        if(Username == null || time == null)
        {
            res.redirect("/users/reservation/form");
        }
        var newReserve = {username: Username, time: time};
        dbo.collection('Reservations').insertOne(newReserve, (err,result) => {
            if(err)throw err;
            else{
                console.log('1 doc inserted');
                //res.write('Reservation succuessfully made. Redirecting to main page...');
                setTimeout(() =>{
                    res.redirect('/users/login/success');
                }, 2000);
            }
            db.close();
        });
    });
});



module.exports = router;