/*
written by: Siddharth Musale
tested by: Siddharth Musale
debugged by: Siddharth Musale
*/
const express = require('express');
const router = express.Router();
const config = require('../config/database');
const getStatus = require('./parkmap');
var con = config.database;

router.get('/home', (req,res,next) => {
    var query = "select hour(StartTime) as hour, count(*) as quantity from ParkingHistory group by hour(Starttime) order by hour(Starttime) asc";
    var hours = [];
    var quants = [];
    con.query(query, (err,result,fields) => {
        if(err)throw err;
        else{
            
            for (i in result)
            {
                hours.push(result[i].hour);
                quants.push(result[i].quantity)
            }
            res.render('admin.ejs', {hours: hours, quants: quants});
        }
    })
});

router.get('/spots', (req,res,next) => {
    var query = "select SpotID, Occupied, Reserved from ParkingSpots";
    var spot = [];
    var occupied = [];
    var reserved = [];
    con.query(query, (err,result,fields) => {
        if(err)throw err;
        else{
            for (i in result)
            {
                spot.push(result[i].SpotID);
                occupied.push(result[i].Occupied)
                reserved.push(result[i].Reserved)
            }
            res.render('AdminSpots.ejs', {spot: spot, occ: occupied, reserved:reserved});
        }
    })
});

router.post('/spots/updated', (req,res,next) => {
    var query = "Update ParkingSpots set Reserved =" + req.body.reserve + ", Occupied = " + req.body.occ + " where SpotID = " + req.body.spot;
    con.query(query, (err,result,fields) => {
        if(err)
        {
            throw err;
        }
        else{
            console.log('1 doc updated')
        }
        res.redirect('/admin/spots')
    })
});

router.get('/reservations', (req,res,next) => {
    var query = "select * from Reservations";
    var resID = [];
    var uID = [];
    var time = [];
    var checkIn = [];
    var spot = []
    con.query(query, (err,result,fields) => {
        if(err)throw err;
        else{
            for (i in result)
            {
                resID.push(result[i].idReservations);
                uID.push(result[i].userID);
                time.push(result[i].DateTime);
                checkIn.push(result[i].CheckIn);
                spot.push(result[i].ParkingSpot);
            }
            res.render('AdminReservations.ejs', {resID: resID, uID: uID, time:time, checkIn:checkIn, spot:spot});
        }
    })
});

router.post('/reservations/updated', (req,res,next) => {
    var query = "Update Reservations set userID =" + req.body.uID + ", DateTime = '" + req.body.time + "' ,CheckIn = " + req.body.checkIn + " ,ParkingSpot = " + req.body.spot +" where idReservations = " + req.body.resID;
    console.log(query);
    con.query(query, (err,result,fields) => {
        if(err)
        {
            throw err;
        }
        else{
            console.log('1 doc updated')
        }
        res.redirect('/admin/reservations')
    })
});
router.post('/reservations/deleted', (req,res,next) => {
    var query = "delete from Reservations where idReservations = " + req.body.resID;
    console.log(query);
    con.query(query, (err,result,fields) => {
        if(err)
        {
            throw err;
        }
        else{
            console.log('1 doc deleted')
        }
        res.redirect('/admin/reservations')
    })
})

router.get('/users', (req,res,next) => {
    var query = "select * from Users";
    var uID = [];
    var username = [];
    var pass = [];
    var name = [];
    var license = [];
    var phone = [];
    var card = [];
    var email = [];
    con.query(query, (err,result,fields) => {
        if(err)throw err;
        else{
            for (i in result)
            {
                uID.push(result[i].idUsers);
                username.push(result[i].Username);
                pass.push(result[i].Password);
                name.push(result[i].Name);
                license.push(result[i].License);
                phone.push(result[i].Phone);
                card.push(result[i].CardNum)
                email.push(result[i].Email);
            }
            res.render('AdminUsers.ejs', {uID: uID, username: username, pass:pass, name:name, license:license, phone:phone,card:card,email:email});
        }
    })
});

router.post('/users/updated', (req,res,next) => {
    var query = "Update Users set Username = '" + req.body.username + "', Password = '" + req.body.pass + "' ,Name = '" + req.body.name + "' ,License = '" + req.body.license +"', Phone = '" + req.body.phone + "', CardNum = '" + req.body.card + "', Email = '" + req.body.email + "'where idUsers = " + req.body.uID;
    console.log(query);
    con.query(query, (err,result,fields) => {
        if(err)
        {
            throw err;
        }
        else{
            console.log('1 doc updated')
        }
        res.redirect('/admin/users')
    })
});
router.post('/users/deleted', (req,res,next) => {
    var query = "delete from Reservations where idUsers = " + req.body.uID;
    con.query(query, (err,result,fields) => {
        if(err)
        {
            throw err;
        }
        else{
            console.log('1 doc deleted')
        }
        res.redirect('/admin/users')
    })
})

module.exports = router;