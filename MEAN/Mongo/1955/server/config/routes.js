const user = require("./../controllers/users");

module.exports = (app) =>{
    app.get("/", user.index)
    app.get('/:first_name%20:last_name', user.show)
    app.get('/new/:first_name%20:last_name', user.create)
    app.get('/remove/:first_name%20:last_name', user.remove)
}

