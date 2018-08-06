const users = require("./../controllers/quotes");

module.exports = (app) =>{
    app.get("/", users.index),
    app.get('/quotes', users.show)
    app.post('/create', users.create)
}

