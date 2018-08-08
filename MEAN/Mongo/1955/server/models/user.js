const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
    first_name: String, 
    last_name: String,
}, {timestamps: true})

mongoose.model('User', UserSchema);