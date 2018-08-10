const express = require("express");
const path = require("path");
const bodyParser = require('body-parser');
const app = express();
const port = 8000;
   
app.use(bodyParser.json());
app.use(express.static( __dirname + '/public/dist/public' ));
app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs'); 

require("./server/config/mongoose");
require("./server/config/routes")(app);

app.listen(port, () => {
    console.log(`all systems go on port ${port}!`);
});