const mongoose = require("mongoose");

const ReptilesSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Name field is required."]}, 
    species: {type: String, required: [true, "Species field is required."]},
    personality: {type: String, required: [true, "Personality field is required."]},
    age: {type: Number, required: [true, "Age field is required."]},
   }, {timestamps: true})

mongoose.model('Reptile', ReptilesSchema);