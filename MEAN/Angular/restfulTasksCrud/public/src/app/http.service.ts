import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class HttpService {
  constructor(private _http: HttpClient) {}
  getTasks(){
    return this._http.get('/tasks');
  }
  createTasks(task){
    return this._http.post('/tasks', task);
  }
  deleteTask(task){
    return this._http.delete(`/tasks/${task._id}`, task)
  }
  editTask(task){
    return this._http.put(`/tasks/${task._id}`, task)
  }
}