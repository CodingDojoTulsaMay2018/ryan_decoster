const mongoose = require("mongoose");
const User = mongoose.model("User");

module.exports = {
    // display user with json data
    index: (req, res) => {
        User.find({}, function(err, user){
            if (err){
                console.log(err)
            }
            res.json(user)
        }).sort({_id: -1})
    },

    // send user to create route and redirect back to index
    create: (req, res) => {
        var newUser = new User({first_name: req.params.first_name, last_name: req.params.last_name})
        newUser.save(function(err){
            if (err){
                console.log(err)
            }
            return res.redirect('/')
        })
    },

    // remove user and redirect back to index
    remove: (req, res) => {
        User.remove({first_name: req.params.first_name, last_name: req.params.last_name}, function(err){
            if (err){
                res.json(err)
            }
            res.redirect('/')
        })
    },

    // show one user only
    show: (req, res) => {
        User.findOne({first_name: req.params.first_name, last_name: req.params.last_name}, function(err, user) {
            if (err){
                res.json(err)
            }
            res.json(user)
        })
    }
}