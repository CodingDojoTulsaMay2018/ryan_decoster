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
    let tempObservable = this._http.post('/tasks', task);
    tempObservable.subscribe(data => console.log("Created a task!", data));
    // return this._http.post('/tasks', task);
  }
  removeTasks(id){
    let tempObservable = this._http.delete('/tasks/' + id);
    tempObservable.subscribe(data => console.log("Deleted a task!", data));
  }
  updateTasks(id, data){
    let tempObservable = this._http.put('/tasks/' + id, data);
    tempObservable.subscribe(data => console.log("Updated the task!", data));
  }
  showTasks(id){
    let tempObservable = this._http.get('/tasks/' + id);
    tempObservable.subscribe(data => console.log("Found our task!", data));
  }
}