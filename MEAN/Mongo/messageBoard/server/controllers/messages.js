const mongoose = require("mongoose");
const Comment = mongoose.model("Comment");
const Message = mongoose.model("Message");
mongoose.Promise = global.Promise;

module.exports = {
    // display all messages and comments with that message
    index: (req, res) => {
        // .populate allows use of subdocuments within a model
        Message.find({}).populate("_comments").exec(function(errors, messagesFromDB) {
            if(errors) {
                console.log(errors);
            } else {
                res.render("index", {posts: messagesFromDB});
            }
        }
    )},
    
    // action route for creating a message
    postMessage: (req, res) => {
        const message = new Message({
            user: req.body.user,
            message: req.body.message
        });
        message.save(function(err){
            if(err){
                console.log("We have an error!", err);
                for(var key in err.errors){
                    req.flash('registration', err.errors[key].message);
                }
                console.log("above redirect**********")
                res.redirect('/');
            }
            else {
                res.redirect('/');
            }
        });
    },

    // action route for creating a comment
    postComment: (req, res) => {
        // find message id first
        Message.findOne({_id: req.params.id}, (errorComment, message) => {
            if (errorComment){
                console.log(errorComment)
            }
            else {
                // create comment and save
                var comment = new Comment({
                    user: req.body.user,
                    comment: req.body.comment,
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
                        // push comment into the array within the message and save
                        message._comments.push(comment);
                        message.save();
                        res.redirect('/');
                    }
                });
            }
        })
    },
}