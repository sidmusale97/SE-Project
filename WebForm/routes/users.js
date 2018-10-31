var express = require('express');
var router = express.Router();
var mysql = require('mysql');
var config = require('../config/database');
var session = require('express-session');
var bcrypt = require('bcryptjs')
var bodyParser = require('body-parser');
var expressValidator = require('express-validator');
var con = config.database;

//Constructor
function User(profile){
    this.profile = profile;
}

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
    const name = req.body.Name;
    const username = req.body.Username;
    const password = req.body.Password;
    const confirmpass = req.body.conPass;
    const email = req.body.Email;
    //var confirmEmail = req.body.conEmail;

    req.checkBody('Name','Name is required').notEmpty();
    req.checkBody('Email','Email is required').notEmpty();
    req.checkBody('Email','Email is not valid').isEmail();
    req.checkBody('Username','Username is required').notEmpty();
    req.checkBody('Password','Password is required').notEmpty();
    req.checkBody('conPass','Passwords do not match').equals(req.body.Password);

    // if(password !== confirmpass && email !== confirmEmail)
    // {
    //     res.render('RegistrationForm.ejs', {error:"Passwords and Emails don't match"});
    // }
    // else if(password !== confirmpass){
    //     res.render('RegistrationForm.ejs', {error:"Passwords don't match"});
    // }
    // else if(email !== confirmEmail){
    //     res.render('RegistrationForm.ejs', {error:"Emails don't match"});
    // }
    // else{
        
    // }

    let errors = req.validationErrors();
    
    if(errors){
        req.session.errors= errors;
        req.session.success = false;
        res.render('RegistrationForm.ejs');
        console.log(errors);
    }else{
        let newUser = new User({
            name:name,
            email:email,
            username:username,
            password:password
        });
        console.log(newUser);
        // bcrypt.getSalt(10,function(err,salt){
        //     bcrypt.hash(newUser.password,salt,function(err,hash){
        //         if(err){
        //             console.log(err);
        //         }
        //         newUser.password = hash;
        //         newUser.save(function(err){
        //             if(err){
        //                 console.log(err);
        //                 return;
        //             }else{
        //                 res.redirect('/login');
        //             }
        //         })
        //     });
        // });
        res.redirect('/');
     
    }
    router.get('/login',function(req,res){
        res.render('AccountMainPage.ejs');
    });
    
});

//Register page
router.get('/registerpage', (req,res,next) =>{
    res.render('RegistrationForm.ejs');
});


module.exports = router;