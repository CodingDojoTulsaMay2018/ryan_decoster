const express = require("express");
const path = require("path");
const bodyParser = require('body-parser');
const app = express();
const port = 8000;
   
app.use(bodyParser.json());
app.use(express.static( __dirname + '/public/dist/public' ));

app.listen(port, () => {
    console.log(`all systems go on port ${port}!`);
});