import { Component, OnInit } from '@angular/core';
import { HttpService } from './http.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {

  newTask: any;
  editTask: any;

  constructor(private _httpService: HttpService){}
    ngOnInit(){
      this.getTasksFromService();
      this.newTask = { title: "", description: ""};
      this.editTask = { title: "", description: ""};
    }

    tasks: any;
    task: any;
    isEdit: boolean = false;

    onSubmit(){
      let observable = this._httpService.createTasks(this.newTask);
      observable.subscribe(data => {
        console.log("Created new task!", data);
        this.newTask = { title: "", description: ""};
      });
      this.getTasksFromService();
    }
 
    toggleEdit(task){
      this.editTask = {_id: task._id, title: task.title, description: task.description}
      console.log(task._id)
      this.isEdit = !this.isEdit;
    }

    getTasksFromService(){
      let observable = this._httpService.getTasks();
      observable.subscribe(data => {
        console.log("Got our tasks!", data);
        this.tasks = data;
      });
    }

    deleteTask(task){
      let observable = this._httpService.deleteTask(task);
      observable.subscribe(data => {
        console.log("Deleted task!", data);
      });
      this.getTasksFromService()
    }
    
    updateTask(){
      let observable = this._httpService.editTask(this.editTask);
      observable.subscribe(data => {
        this.editTask = {
          title: this.editTask.title,
          description: this.editTask.description
        }
        console.log("Updated successfully!", data);
      })
      this.getTasksFromService()
    }
}