import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class HttpService {
  constructor(private _http: HttpClient) {
    // this.getTasks()
    // this.createTasks({
    //   "title": "Doom",
    //   "description": "Meet your maker."
    // })
    // this.removeTasks("5b6c72b4f83cf28b819926c4")
    // this.updateTasks("5b6c72b4f83cf28b819926c4", {
    //   "title": "Count Dracula",
    //   "description": "I like to count."
    // })
    // this.showTasks("5b6c72b4f83cf28b819926c4")
  }
  getTasks(){
    return this._http.get('/tasks');
  }
  createTasks(task){
    return this._http.post('/tasks', task);
  }
  getTask(task){
    return this._http.get('/tasks/' + task);
  }
}