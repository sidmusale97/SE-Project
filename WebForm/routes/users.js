var express = require('express');
var router = express.Router();
var mysql = require('mysql');
var config = require('../config/database');
var session = require('express-session');
var bcrypt = require('bcryptjs')
var bodyParser = require('body-parser');
var expressValidator = require('express-validator');
const getStatus = require('./parkmap');
var con = config.database;

//Constructor
function User(profile){
    this.profile = profile;
}
router.get('/loginpage', (req,res,next) => {
    res.render('loginpage.ejs')
});
router.get('/home', (req,res,next) => {
    res.render('index.ejs')
});
router.get('/about', (req,res,next) => {
    res.render('AboutPage.ejs')
});
router.get('/update',( req,res,next)=>{
    res.render('update.ejs')
});
//router.get('/map', (req,res,next) => {
//    res.render('ParkingMap.ejs')
//});


router.get('/profile/update',(req,res,next)=>{
    res.render('UpdateInfo.ejs');
});

//Login
router.post('/profile', (req,res,next) => {
    var username = req.body.Username;
    var password = req.body.Password;
    var query = "SELECT * FROM Users WHERE Username = '" + username + "' and Password = '" + password + "'";
    con.query(query,(err, result, fields) =>{
        if (err)throw err;
        if (result == null)
            {
                res.render('loginpage.ejs', {error: "Username does not exist or password is invalid"});
            }
        else
            { 
                req.session.userID = result[0].idUsers;
                req.session.name = result[0].Name;
                //res.redirect('/login/success');

                var reservations = null;
                var query = "SELECT * FROM Reservations WHERE userID = "+ req.session.userID;
                //console.log(query);
                var months = ["January", "Feburary", ", March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
                con.query(query, (err, result, fields) => {
                    for (var r in result)
                    {
                        console.log(r);
                    }  
                    res.render('AccountMainPage.ejs', {name:req.session.name, reservations:result});
                });
            }   
        });
    });

/*router.get('/login/success', (req,res,next) => {
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
   
});*/

//Register
router.post('/register', (req,res,next) => {
    const name = req.body.Name;
    const username = req.body.Username;
    const password = req.body.Password;
    const license = req.body.license;
    const confirmpass = req.body.conPass;
    const email = req.body.Email;
    const card = req.body.Card;
    const phone = req.body.Number;
    var confirmEmail = req.body.conEmail;

    
   var query = "INSERT INTO Users (Username,Password,Name,License,Phone,CardNum,Email) VALUES ('" +username + "','" + password + "','" + name + "','" + license+ "','"+card+ "','"+phone+"','"+email+"')";
   //console.log(query);

   /*
    req.checkBody('Name','Name is required').notEmpty();
    req.checkBody('Email','Email is required').notEmpty();
    req.checkBody('Email','Email is not valid').isEmail();
    req.checkBody('Username','Username is required').notEmpty();
    req.checkBody('Password','Password is required').notEmpty();
    req.checkBody('conPass','Passwords do not match').equals(req.body.Password);*/

    if(password !== confirmpass && email !== confirmEmail)
    {
        res.render('RegistrationForm.ejs', {error:"Passwords and Emails don't match"});
    }
    else if(password !== confirmpass){
        res.render('RegistrationForm.ejs', {error:"Passwords don't match"});
    }
     else if(email !== confirmEmail){
        // res.render('RegistrationForm.ejs', {error:"Emails don't match"});
    }
    // else{
        
    // }
    /*let errors = req.validationErrors();
    
    if(errors){
        req.session.errors= errors;
        req.session.success = false;
        res.render('RegistrationForm.ejs');
        console.log(errors);
    }else{*/
        let newUser = new User({
            name:name,
            email:email,
            username:username,
            password:password
        });
        //console.log(newUser);
        con.query(query,(err, result, fields) =>{
            if (err)throw err;
            });   
            //res.render('RegistrationForm.ejs');

        var logUsername = username;
        var logPass = password;
        var logQuery = "SELECT * FROM Users WHERE Username = '" + logUsername + "' and Password = '" + logPass + "'";
        con.query(logQuery,(err, result, fields) =>{
    
        if (err)throw err;
        if (result == null)
            {
               // res.render('loginpage.ejs', {error: "Username does not exist or password is invalid"});
            }
        else
            { 
                req.session.userID = result[0].idUsers;
                req.session.name = result[0].Name;
                //res.redirect('/login/success');

                var reservations = null;
                var resQuery = "SELECT * FROM Reservations WHERE userID = "+ req.session.userID;
                console.log(resQuery);
                var months = ["January", "Feburary", ", March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
                con.query(resQuery, (err, result, fields) => {
                    for (var r in result)
                    {
                        //console.log(r);
                    }  
                    res.render('AccountMainPage.ejs', {name:req.session.name, reservations:result});
                });
            }   
        });
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
    //}
    
});

//Register page
router.get('/registerpage', (req,res,next) =>{
    res.render('RegistrationForm.ejs');
});


//Parking map
router.get('/map', async(req,res,next) => { 
    //const data = await getStatus();
    getStatus(function(data){
    console.log(data);
    res.render('ParkingMap.ejs',{data: data,});
    })
})


module.exports = router;