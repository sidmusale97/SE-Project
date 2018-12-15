/*
written by: Siddharth Musale
tested by: Siddharth Musale
debugged by: Siddharth Musale
*/
var express = require('express');
var router = express.Router();


router.get('/', function(req,res,next){
    res.render('index.ejs', {error:req.session.errors});
    req.session.errors = null;
});

module.exports = router;