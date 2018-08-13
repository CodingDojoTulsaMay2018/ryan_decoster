import { Component, OnInit } from '@angular/core';
import { HttpService } from './http.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {

  constructor(private _httpService: HttpService){}
    
    ngOnInit(){}

    tasks: any;
    task: any;

    getTasksFromService(){
      let observable = this._httpService.getAllTasks();
      observable.subscribe(data => {
        console.log("Got our tasks!", data);
        this.tasks = data;
      });
    }

    info(task){
      this.task = task;
    }
}