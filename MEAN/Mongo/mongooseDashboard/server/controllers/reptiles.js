const mongoose = require("mongoose");
const Reptile = mongoose.model("Reptile");
mongoose.Promise = global.Promise;

module.exports = {
    // display all reptiles
    index: (req, res) => {
        Reptile.find({}, (err, reptilesFromDB)=>{
            if(err) {
                console.log(err);
            } else {
                res.render("index", {reptiles: reptilesFromDB});
            }
        })
    },

    // displays info about one reptile
    showRep: (req, res) => {
        Reptile.findOne({_id:req.params.id}, (err, reptilesFromDB)=>{
            if(err) {
                console.log(err);
            } else {
                console.log(reptilesFromDB);
                res.render("show", {reptile: reptilesFromDB});
            }
        });
    }, 
    
    // displays form for making a new reptile
    newRep: (req, res) => {
        res.render("newRep");
    }, 
    
    // action route for creating a reptile
    create: (req, res) => {
        const reptile = new Reptile(req.body);
        reptile.save(function(err){
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
    },

    // displays form to edit existing reptile
    edit: (req, res) => {
        Reptile.findOne({_id:req.params.id}, (err, reptilesFromDB)=>{
            if(err) {
                console.log(err);
            } else {
                console.log(reptilesFromDB);
                res.render('edit', {reptile: reptilesFromDB});
            }
        });
    },  

    // action route for editing an existing reptile
    update: (req, res) => {
        Reptile.update({_id: req.params.id}, req.body, (err, reptilesFromDB) => {
            if(err) {
                console.log(err);
            } else {
                console.log(reptilesFromDB);
                res.redirect(`/reptiles/${req.params.id}`);
            }
        });
    },

    // action route for deleting a reptile
    delete: (req, res) => {
        Reptile.remove({_id: req.params.id}, (err, reptilesFromDB) => {
            if(err) {
                console.log(err);
            } else {
                console.log(reptilesFromDB);
                res.redirect('/');
            }
        });
    },
}