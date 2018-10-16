const express = require('express');
const router = express.Router();
var mongodb = require('mongodb').MongoClient;
const config = require('../config/database');
var session = require('express-session');

//Login
router.post('/login', (req,res,next) => {
    var username = req.body.Username;
    var password = req.body.Password;
    mongodb.connect(config.database, {useNewUrlParser: true}, (err, db) => {
        if (err) throw err;
        else{
            console.log("connected");
        }
        var dbo = db.db('SE_Project');
        dbo.collection('Users').findOne({username: username, password: password}, (err, result) =>{
            if (err)throw err;
            if (result == null)
            {
                res.render('index.ejs', {error: "Username does not exist or password is invalid"});
            }
            else
            {
                req.session.Username = result.username;
                req.session.name = result.name;
                res.redirect('/users/login/success');
            }
            db.close();
            
        });
    });
    
});

router.get('/login/success', (req,res,next) => {
    var Username = req.session.Username;
    var reservations = null;
    mongodb.connect(config.database, {useNewUrlParser: true}, (err,db) =>{
            if (err)throw err;
            else{
                var dbo = db.db('SE_Project');
                dbo.collection('Reservations').find(function(err, result){
                console.log(result);
                reservations = result;
                });
            }
            db.close();
    });
    console.log(reservations);
    res.render('AccountMainPage.ejs', {name: req.session.name, reservations: reservations});
});

//Register
router.post('/register', (req,res,next) => {
    var username = req.body.Username;
    var password = req.body.Password;
    var confirmpass = req.body.conPass;
    var email = req.body.email;
    var confirmEmail = req.body.conEmail;

    if(password !== confirmpass && email !== confirmEmail)
    {
        res.render('RegistrationForm.ejs', {error:"Passwords and Emails don't match"});
    }
    else if(password !== confirmpass){
        res.render('RegistrationForm.ejs', {error:"Passwords and Emails don't match"});
    }
    else if(email !== confirmEmail){
        res.render('RegistrationForm.ejs', {error:"Emails don't match"});
    }
    else{
    
    }
})


//Register page
router.get('/registerpage', (req,res,next) =>{
    res.render('RegistrationForm.ejs');
});



module.exports = router;