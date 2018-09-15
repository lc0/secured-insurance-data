import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DataServiceService {

  private picturesUrl = 'http://localhost:5000/getImageCategories';  // URL to web api

  constructor(private http: HttpClient) { } 

  getCategoriesFromPhotos(){
    return [
      {data: [65, 59, 80, 81, 56, 55, 40], label: 'Number of pictures'}
    ];
  }

  getDictCategories () {  
    let headers : any[];
    let counts : any[];
    
    this.http.get(this.picturesUrl)
    .subscribe((data: any) => {
      headers = data['headers'];
      counts = data['counts'];
    });

    return {"headers": headers, "counts": counts};

  }
  

}
