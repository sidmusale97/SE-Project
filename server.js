var express = require('express');
var app = express();
var path = require('path');
var bodyparser = require('body-parser');

var port = 8000;

var index = require('./routes/index');
const users = require('./routes/users');


//Setting View engine
app.set('view engine','ejs');
app.set('views', path.join(__dirname, '/views'));
app.engine('html', require('ejs').renderFile);

//Set static folder
app.use(express.static(path.join(__dirname, 'public')));

//Body Parser Middle ware
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({extended: false}));

app.use('/', index);
app.use('/users', users);

app.listen(port, function(){
    console.log("server on port: " + port);
});