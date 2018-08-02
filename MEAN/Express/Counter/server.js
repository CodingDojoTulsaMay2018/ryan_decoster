var express = require("express");
var path = require("path");
var bodyParser = require('body-parser');
var session = require('express-session');

var app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, '/static')));
app.use(session({
    secret: 'tulsa',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
}))

app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs'); 

require("./Server/Config/routes")(app);

app.listen(8000, function() {
  console.log("listening on port 8000");
})