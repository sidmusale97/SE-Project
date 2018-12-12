const express = require('express');
const router = express.Router();
const config = require('../config/database');
const getStatus = require('./parkmap');
var con = config.database;

router.get('/home', (req,res,next) => {
    res.render('admin.ejs')
});



module.exports = router;