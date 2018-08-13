const user = require("./../controllers/users");

module.exports = (app) =>{
    app.get("/tasks", user.index)
    app.get('/tasks/:id', user.show)
    app.post('/tasks', user.create)
    app.delete('/tasks/:id', user.remove)
    app.put('/tasks/:id', user.update)
}

