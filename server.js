var express = require('express');
var app = express();
var path = require('path');
var bodyparser = require('body-parser');
var login = require('./routes/loginroutes');



//test
//Setting View engine
app.set('view engine','ejs');
app.set('views', path.join(__dirname, '/views'));

//Body Parser Middle ware
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({extended: false}));


// viewed at http://localhost:8080
app.get('/', function(req, res) {
    res.render(path.join(__dirname + '/views/index.ejs'));
});

    console.log(req.body);
    res.render(path.join(__dirname, '/views/pages/AccountMainPage.ejs'));
});

app.get('/ReservationForm', function(req,res){
    res.render(path.join(__dirname, '/views/pages/ReservationForm.ejs'));
});

    res.render(path.join(__dirname,'/views/pages/RegistrationForm.ejs'));
});


app.listen(8080);