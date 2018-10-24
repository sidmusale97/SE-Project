const express = require('express');
const router = express.Router();
const mysql = require('mysql');
const config = require('../config/database');
var session = require('express-session');

var con = config.database;
//Login
router.post('/login', (req,res,next) => {
    var username = req.body.Username;
    var password = req.body.Password;
    var query = "SELECT * FROM Users WHERE Username = '" + username + "' and Password = '" + password + "'";
    con.query(query,(err, result, fields) =>{
        if (err)throw err;
        if (result == null)
            {
                res.render('index.ejs', {error: "Username does not exist or password is invalid"});
            }
            else
            {
                req.session.userID = result[0].idUsers;
                req.session.name = result[0].Name;
                res.redirect('/users/login/success');
            }   
        });
    });

router.get('/login/success', (req,res,next) => {
    var reservations = null;
    var query = "SELECT * FROM Reservations WHERE userID = "+ req.session.userID;
    console.log(query);
    var months = ["January", "Feburary", ", March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    con.query(query, (err, result, fields) => {
        for (var r in result)
        {
            console.log(r);
        }  
        res.render('AccountMainPage.ejs', {name:req.session.name, reservations:result});
    });
   
});

//Register
router.post('/register', (req,res,next) => {
    var username = req.body.Username;
    var password = req.body.Password;
    var name = req.body.Name;
    var confirmpass = req.body.conPass;
    var email = req.body.email;
    var confirmEmail = req.body.conEmail;
    var license = req.body.license;

    var query = "INSERT INTO Users (Username,Password,Name,License) VALUES ('" +username + "','" + password + "','" + name + "','" + license+"')";

    if(password !== confirmpass && email !== confirmEmail)
    {
        res.render('RegistrationForm.ejs', {error:"Passwords and Emails don't match"});
    }
    else if(password !== confirmpass){
        res.render('RegistrationForm.ejs', {error:"Passwords don't match"});
    }
    else if(email !== confirmEmail){
        res.render('RegistrationForm.ejs', {error:"Emails don't match"});
    }
    else{
        con.query(query,(err, result, fields) =>{
            if (err)throw err;
            });   
            res.render('AccountMainPage.ejs');
        }
})


//Register page
router.get('/registerpage', (req,res,next) =>{
    res.render('RegistrationForm.ejs');
});



module.exports = router;