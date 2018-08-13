const mongoose = require("mongoose");
const Task = mongoose.model("Task");

module.exports = {
    // display all tasks
    index: (req, res) => {
        Task.find({}, function(err, tasks){
            if (err){
                console.log(err)
            }
            res.json(tasks)
        }).sort({_id: -1})
    },

    // create a new task using a post route
    create: (req, res) => {
        Task.create(req.body, (err, task) => {
            if (err){
                res.json(err)
            }
            res.json(task)
        })
    },

    // remove task using a delete route
    remove: (req, res) => {
        Task.findByIdAndRemove(req.params.id, (err) => {
            if (err){
                res.json(err)
            }
            res.json({success: true})
        })
    },

    // show one task only by the id
    show: (req, res) => {
        Task.findById(req.params.id,(err, user) => {
            if (err){
                res.json(err)
            }
            res.json(user)
        })
    },

    // update task by id using a put route
    update: (req, res) => {
        Task.findByIdAndUpdate(req.params.id, {$set: req.body}, (err, user) => {
            if (err){
                res.json(err)
            }
            res.json({updated: true})
        })
    },

}