const mongoose = require("mongoose");
const User = mongoose.model("User");
const bcrypt = require('bcrypt');

module.exports = {
    // display login and registration forms
    index: (req, res) => {
        res.render('index')
    },
    
    // action route for registering a user
    register: (req, res) => {
        const newUser = new User(req.body);
            newUser.save(function(err){
                if(err){
                    console.log("We have an error!", err);
                    for(var key in err.errors){
                        req.flash('registration', err.errors[key].message);
                    }
                    res.redirect('/');
                }
                else {
                    req.session.user_id = newUser._id;
                    req.session.name = newUser.first_name;
                    newUser.password = bcrypt.hashSync(newUser.password, 10)
                    newUser.save()
                    console.log(`Session ID: ${req.session.user_id}`)
                    res.redirect('/success');
                }
            });
    },

    // action route for logging in
    login: (req, res) => {
        User.findOne({email:req.body.email}, (err, userFromDB)=>{           
            if(userFromDB == null){
                console.log("Invalid email or password")
                res.redirect("/")
            }
            else{                 
                passwordIsValid = bcrypt.compareSync(req.body.password, userFromDB.password)
                if(passwordIsValid){    
                    console.log('Login successful!')
                    req.session.user_id = userFromDB._id;
                    console.log(`Session ID: ${req.session.user_id}`)
                    req.session.name = userFromDB.first_name;            
                    console.log(`Session Name: ${req.session.name}`)
                    res.redirect('/success');
                }
                else{
                    console.log("Invalid Password");              
                    res.redirect("/")
                }               
            }
        })      
    },

    success: (req, res) => {
        res.render('success', {name: req.session.name})
    },

    logout: (req, res) => {
        delete req.session.user_id
        console.log(req.session.user_id)
        return res.redirect('/')
    }
}