module.exports = (app) =>{

    app.get("/", (req, res)=>{
        return res.render('index')
    })

    app.post("/submit", (req, res)=>{
        req.session.name = req.body.name,
        req.session.location = req.body.location,
        req.session.stack = req.body.stack,
        req.session.comment = req.body.comment
        return res.redirect("/results");
    })

    app.get("/results", (req, res)=>{
        return res.render('results', { session: req.session });
    })
}