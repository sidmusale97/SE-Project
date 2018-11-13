var express = require('express');
var router = express.Router();


router.get('/entrance', function(req,res,next){
    res.render('EntranceGate.ejs');
});

module.exports = router;