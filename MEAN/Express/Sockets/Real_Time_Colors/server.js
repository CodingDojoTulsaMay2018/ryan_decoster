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
var color;
io.on('connection', function (socket) {
    // emits initially on connection to whatever the current color is at
    io.emit('response', {response: color});
    socket.on('green', function (data) {
        // recieves emit from client
        color = "green";
        console.log("Color is the color: " + color)
        io.emit('response', { response: color });
        console.log("Emitting from server.")
        // emits back response to client
    });
    socket.on('blue', function (data) {
        color = "blue";
        io.emit('response', { response: color });
    });
    socket.on('pink', function (data) {
        color = "pink";
        io.emit('response', { response: color });
    });
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, '/static')));
app.use(express.static(path.join(__dirname, "/static/css")));
app.use(session({
    secret: 'tulsadojo',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
}))

app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs'); 

require("./server/config/routes")(app);

