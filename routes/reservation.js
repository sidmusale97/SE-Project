const express = require('express');
const router = express.Router();
var mongodb = require('mongodb').MongoClient;
const config = require('../config/database');

router.get('/form', (req,res,next) => {
    res.render('ReservationForm.ejs');
});

router.get('/create', (req,res,next) => {
    mongodb.connect(config.database, {useNewUrlParser: true}, (err,db) =>{
        if(err)throw err;
        else{
            console.log('connected');
        }
        var dbo = db.db('SE_Project');
        var id = req.session.userId;
        var time = req.body.datefield;
        console.log(req.body);
        var newReserve = {userId: id, time: time};
        dbo.collection('Reservations').insertOne(newReserve, (err,res) => {
            if(err)throw err;
            else{
                console.log('1 doc inserted');
            }
            db.close();
        });
    });
});

module.exports = router;