const board = require("./../controllers/messages");

module.exports = (app) =>{
    app.get("/", board.index)
    app.post("/postMessage", board.postMessage)
    app.post("/postComment/:id", board.postComment)
}

