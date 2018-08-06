const mongoose = require("mongoose");
const Quote = mongoose.model("Quote");

module.exports = {
    index: (req, res) => {
        res.render("index");
    }, 

    show: (req, res) => {
        Quote.find({}, (err, quotesFromDB)=>{
            if(err) {
                console.log(err);
            } else {
                console.log(quotesFromDB);
                res.render("quotes", {quotes: quotesFromDB});
            }
        }).sort({createdAt: -1})
    }, 
    
    create: (req, res) => {
        const quote = new Quote(req.body);
        quote.save(function(err){
            if(err){
                // if there is an error upon saving, use console.log to see what is in the err object 
                console.log("We have an error!", err);
                // adjust the code below as needed to create a flash message with the tag and content you would like
                for(var key in err.errors){
                    req.flash('registration', err.errors[key].message);
                }
                // redirect the user to an appropriate route
                res.redirect('/');
            }
            else {
                res.redirect('/');
            }
        });
    }
}