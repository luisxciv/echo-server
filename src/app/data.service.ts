import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  // BASE_URL = 'http://localhost:8080/data';
  BASE_URL = 'http://127.0.0.1:8083/data';

  constructor(private http: HttpClient) { }

  get(data?: any) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Origin': '*'
    })
    const url = this.BASE_URL + '/' + data;
    return this.http.get(url, { headers });
  }

  post(data?: any) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'POST',
      'Access-Control-Allow-Origin': '*'
    });
    const body = { data };
    return this.http.post(this.BASE_URL, body, { headers });
  }

  put(data?: any) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'PUT',
      'Access-Control-Allow-Origin': '*'
    });
    const body = { data };
    return this.http.put(this.BASE_URL, body, { headers });
  }

  delete(data?: any) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'DELETE',
      'Access-Control-Allow-Origin': '*'
    });
    const url = this.BASE_URL + '/' + data;
    return this.http.delete(url, { headers });
  }

  patch(data?: any) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'PATCH',
      'Access-Control-Allow-Origin': '*'
    });
    const body = { data };
    return this.http.patch(this.BASE_URL, body, { headers });
  }
}
