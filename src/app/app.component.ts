import { Component } from '@angular/core';
import { DataService } from './data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'postman';
  method = 'GET';
  gender;
  name;
  data;
  getResponse;
  responseTime;
  constructor(private dataService: DataService) {

  }

  handleSubmit() {
    const beforeTimestamp = Date.now();

    if (this.method === 'GET') {
      this.dataService.get(this.data).subscribe(res => {
        const afterTimeStamp = Date.now();
        const diff = afterTimeStamp - beforeTimestamp;
        this.responseTime = diff;
        this.getResponse = res;
      });
    } else if (this.method === 'PUT') {
      this.dataService.put(this.data).subscribe(res => {
        const afterTimeStamp = Date.now();
        const diff = afterTimeStamp - beforeTimestamp;
        this.responseTime = diff;
        this.getResponse = res;
      });
    } else if (this.method === 'POST') {
      this.dataService.post(this.data).subscribe(res => {
        const afterTimeStamp = Date.now();
        const diff = afterTimeStamp - beforeTimestamp;
        this.responseTime = diff;
        this.getResponse = res;
      });
    } else if (this.method === 'DELETE') {
      this.dataService.delete(this.data).subscribe(res => {
        const afterTimeStamp = Date.now();
        const diff = afterTimeStamp - beforeTimestamp;
        this.responseTime = diff;
        this.getResponse = res;
      });
    } else if (this.method === 'PATCH') {
      this.dataService.patch(this.data).subscribe(res => {
        const afterTimeStamp = Date.now();
        const diff = afterTimeStamp - beforeTimestamp;
        this.responseTime = diff;
        this.getResponse = res;
      });
    }
  }
}
