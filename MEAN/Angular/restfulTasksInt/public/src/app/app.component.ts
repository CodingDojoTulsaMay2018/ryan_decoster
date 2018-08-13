import { Component, OnInit } from '@angular/core';
import { HttpService } from './http.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  newTask: any;

  constructor(private _httpService: HttpService){}
    
    ngOnInit(){
      this.newTask = { title: "", description: ""};
    }

    tasks: any;
    task: any;
    shouldDisplaySection: boolean;

    onSubmit(){
      let observable = this._httpService.createTasks(this.newTask);
      observable.subscribe(data => {
        console.log("Created new task!", data);
        this.newTask = { title: "", description: ""};
      });
      this.getTasksFromService();
    }

    getTasksFromService(){
      let observable = this._httpService.getTasks();
      observable.subscribe(data => {
        console.log("Got our tasks!", data);
        this.tasks = data;
      });
    }

    onButtonClick(task){
      this.task = task;
      console.log("Button clicked!");
    }

    hideSection($event){
      $event.stopPropagation();
      this.shouldDisplaySection = false;
    }

    showSection(task){
      this.shouldDisplaySection = true;
      this.task = task;
    }
}