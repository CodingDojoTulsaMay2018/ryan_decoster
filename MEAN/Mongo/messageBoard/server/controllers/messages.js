const mongoose = require("mongoose");
const Message = mongoose.model("Message");
const Comment = mongoose.model("Comment");
mongoose.Promise = global.Promise;

module.exports = {
    // display all messages and comments with that message
    index: (req, res) => {
        Message.find({}).populate("_comments").exec(function(errors, messagesFromDB) {
            console.log("I'm making a comment yo.")
            if(errors) {
                console.log(errors);
            } else {
                res.render("index", {messages: messagesFromDB});
            }
        }
    )},
    
    // action route for creating a message
    postMessage: (req, res) => {
        const message = new Message({
            user: req.body.user,
            message: req.body.message
        });
        message.save(function(errorMessage){
            if(errorMessage){
                // if there is an error upon saving, use console.log to see what is in the err object 
                console.log("We have an error!", errorMessage);
                // adjust the code below as needed to create a flash message with the tag and content you would like
                for(var key in errorMessage.errors){
                    req.flash('registration', errorMessage.errors[key].message);
                }
                // redirect the user to an appropriate route
                res.redirect('/');
            }
            else {
                res.redirect('/');
            }
        });
    },

    // action route for creating a comment
    postComment: (req, res) => {
        Message.findOne({_id: req.params.id}, (errorComment, message) => {
            if (errorComment){
                console.log(errorComment)
            }
            else {
                var comment = new Comment({
                    user: req.body.user,
                    comment: req.body.comment,
                    _message: req.params.id
                });
                console.log(comment)
                comment.save(function(err){
                    if(err){
                        for(var key in err.errors){
                            req.flash('registration', err.errors[key].message);
                        }
                        res.redirect('/');
                    }
                    else {
                        message._comments.push(comment._id);
                        message.save();
                        res.redirect('/');
                    }
                });
            }
        })
    },
}