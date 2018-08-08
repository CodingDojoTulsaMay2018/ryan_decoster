const express = require("express");
const path = require("path");
const bodyParser = require('body-parser');
const session = require('express-session');
const app = express();
const port = 8000;
const flash = require('express-flash');
   
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs'); 
app.use(flash());
app.use(session({
    secret: 'tulsadojo',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: null }
}))

require("./server/config/mongoose");
require("./server/config/routes")(app);

app.listen(port, () => {
    console.log(`all systems go on port ${port}!`);
});