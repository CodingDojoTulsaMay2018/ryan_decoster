import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  constructor(private _http: HttpClient) {
    this.getTasks()
    // this.createTasks({
    //   "title": "Oscar the Grouch",
    //   "description": "I am also green."
    // })
    // this.removeTasks("5b6c72b4f83cf28b819926c4")
    this.updateTasks("5b6c72b4f83cf28b819926c4", {
      "title": "Count Dracula",
      "description": "I like to count."
    })
    // this.showTasks("5b6c72b4f83cf28b819926c4")
  }
  getTasks(){
    // our http response is an Observable, store it in a variable
    let tempObservable = this._http.get('/tasks');
    // subscribe to the Observable and provide the code we would like to do with our data from the response
    tempObservable.subscribe(data => console.log("Got our tasks!", data));
  }
  createTasks(task){
    let tempObservable = this._http.post('/tasks', task);
    tempObservable.subscribe(data => console.log("Created a task!", data));
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