const mongoose = require("mongoose");
var uniqueValidator = require('mongoose-unique-validator');

const UserSchema = new mongoose.Schema({
    first_name: {
        type: String, 
        required: [true, 'First name is required.'],
        validate: {
            validator: function(value) {
                return /^[a-zA-Z]+$/.test(value)
            },
            message: 'Please enter a valid first name.'
        },
        minlength: [2, 'First name must be more than 2 characters.'],
        maxlength: [20, 'First name must be less than 20 characters.']
    }, 

    last_name: {
        type: String, 
        required: [true, 'Last name is required.'],
        validate: {
            validator: function(value) {
                return /^[a-zA-Z]+$/.test(value)
            },
            message: 'Please enter a valid last name.'
        },
        minlength: [2, 'Last name must be more than 2 characters.'],
        maxlength: [20, 'Last name must be less than 20 characters.']
    }, 

    email: {
        type: String, 
        required: [true, "Email is required."],
        unique: true,
        validate: {
            validator: function(email) {
                return /^[a-zA-Z0-9.!#$%&’*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email);
            },
            message: 'Please enter a valid email.',
        },
        maxlength: [120, 'Email must be less than 120 characters.']
    }, 

    password: {
        type: String, 
        required: [true, "Password field is required."],
        validate: {
            validator: function(password) {
                return /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])/.test(password)
            },
            message: 'Password must contain 1 lowercase letter, 1 uppercase letter, and 1 number.'
        },
        minlength: [8, 'Password must be at least 8 characters.'],
        maxlength: [120, 'Password must be less than 120 characters.'],
    },

    birthday: {
        type: Date, 
        required: [true, "Birthday field is required."],
        validate: {
            validator: function(date) {
                return date instanceof Date;
            },
            message: 'Please enter a valid date.',
            validator: function(date) {
                return date < Date.now()
            },
            message: 'Date cannot be in the future.',
            validator: function(birthday) {
                var ageDifMs = Date.now() - birthday.getTime();
                var ageDate = new Date(ageDifMs);
                var result = Math.abs(ageDate.getUTCFullYear() - 1970);
                if (result > 17) {
                    return true
                }
                return false
            },
            message: 'Must be older than 18 years old.'
        }
    },

}, {timestamps: true})

UserSchema.plugin(uniqueValidator, { message: 'Email already exists.' });
mongoose.model('User', UserSchema);