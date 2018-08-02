module.exports = (app) =>{

    app.get("/", (req, res)=>{
        if('count' in req.session){
            req.session.count++;
        }
        else {
            req.session.count = 1;
        }
        return res.render('index', { session: req.session})
    })

    app.post("/reset", (req, res)=>{
        req.session.count = 0;
        return res.redirect("/");
    })

    app.post("/double", (req, res)=>{
        req.session.count +=1;
        return res.redirect('/');
    })
}