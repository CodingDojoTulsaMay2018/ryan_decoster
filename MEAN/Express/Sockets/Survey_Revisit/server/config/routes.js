module.exports = (app) =>{

    app.get("/", (req, res)=>{
        return res.render('index')
    })
}