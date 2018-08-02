var express = require("express");
var path = require("path");
var bodyParser = require('body-parser');
var session = require('express-session');
var app = express();
var port = 8000;
var server = app.listen(port, () => {
    console.log("listening on port 8000");
});
var io = require('socket.io').listen(server);

io.on('connection', function (socket) {
    socket.on('post_form', function (data) {
        var random_number = Math.floor((Math.random() * 1000) + 1);
        // emitters
        socket.emit('updated_message', { response: data });
        socket.emit('random_number', { response: random_number });
    });
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, '/static')));
app.use(session({
    secret: 'tulsadojo',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
}))

app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs'); 

require("./server/config/routes")(app);

