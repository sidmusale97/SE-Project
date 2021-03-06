var express = require('express');
var app = express();
var path = require('path');
var bodyparser = require('body-parser');
var session = require('express-session');

var port = 8000;

const index = require('./routes/index');
const users = require('./routes/users');
const reservation = require('./routes/reservation');
const entrance = require('./routes/Entrance');
const parkmap = require('./routes/parkmap');
const admin = require('./routes/admin')
const dynamicprice = require('./routes/dynamicprice');

//Setting View engine
app.set('view engine','ejs');
app.set('views', path.join(__dirname, '/views'));
app.engine('html', require('ejs').renderFile);

//Set static folder
app.use('/public',express.static(path.join(__dirname, 'public')));

//Body Parser Middle ware
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({extended: false}));

//Middleware for Express Sessions
app.use(session({
    secret: 'sec',
    resave: true,
    saveUninitialized: false
}));

//Set up routes
app.use('/', index);
app.use('/users', users);
app.use('/reservation', reservation);
app.use('/entrance', entrance);
app.use('/map', parkmap);
app.use('/dynamicprice', dynamicprice);
app.use('/admin', admin)


app.listen(port, function(){
    console.log("server on port: " + port);
});