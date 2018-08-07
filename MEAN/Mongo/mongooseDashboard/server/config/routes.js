const reptiles = require("./../controllers/reptiles");

module.exports = (app) =>{
    app.get("/", reptiles.index)
    app.get('/reptiles/:id', reptiles.showRep)
    app.get('/new', reptiles.newRep)
    app.post('/create', reptiles.create)
    app.get('/edit/:id', reptiles.edit)
    app.post('/reptiles/:id', reptiles.update)
    app.get('/destroy/:id', reptiles.delete)
}

