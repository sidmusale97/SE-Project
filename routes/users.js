const express = require('express');
const router = express.Router();
var mongodb = require('mongodb').MongoClient;
const config = require('../config/database');
var session = require('express-session');
var username;
//Login
router.post('/login', (req,res,next) => {
    username = req.body.Username;
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
                req.session.userId = result._id;
                res.render('AccountMainPage.ejs', {name:result.name});
            }
            db.close();
            
        });
    });
    
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
        res
    }
})


//Register page
router.get('/registerpage', (req,res,next) =>{
    res.render('RegistrationForm.ejs');
});



module.exports = router;