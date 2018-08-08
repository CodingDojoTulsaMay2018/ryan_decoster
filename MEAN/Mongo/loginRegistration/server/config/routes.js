const user = require("./../controllers/users");

module.exports = (app) =>{
    app.get("/", user.index)
    app.post("/register", user.register)
    app.post("/login", user.login)
    app.get('/success', user.success)
    app.get('/logout', user.logout)
}

