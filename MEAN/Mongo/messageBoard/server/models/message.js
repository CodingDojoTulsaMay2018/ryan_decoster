const mongoose = require("mongoose");
const Schema = mongoose.Schema

const CommentsSchema = new mongoose.Schema({
    user: {type: String, required: [true, "User field is required."]}, 
    comment: {type: String, required: [true, "Comment field is required."]},
    }, {timestamps: true})
    
mongoose.model('Comment', CommentsSchema);

const MessagesSchema = new mongoose.Schema({
    user: {type: String, required: [true, "User field is required."]}, 
    message: {type: String, required: [true, "Message field is required."]},
    _comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
    }, {timestamps: true})

mongoose.model('Message', MessagesSchema);