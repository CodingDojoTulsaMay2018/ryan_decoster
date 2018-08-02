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
    var count = undefined;
    socket.on('epic_clicked', function (data) {
        if (!count){
            count = 1;
        }
        else {
            count++;
        }
        // emitter
        socket.emit('epic_response', { response: count });
    });
    socket.on('reset_clicked', function (data) {
        // emitter
        count = 0;
        socket.emit('epic_response', { response: count });
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

