import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DataServiceService {

  private picturesUrl = 'http://9d06ab5b.ngrok.io/getImageCategories';  // URL to web api

  constructor(private http: HttpClient) { } 

  getCategoriesFromPhotos(){
    return [
      {data: [65, 59, 80, 81, 56, 55, 40], label: 'Number of pictures'}
    ];
  }

  getDictCategories (): Observable<any[]> {
    return this.http.get<any[]>(this.picturesUrl)
      .pipe(
        catchError(this.handleError('getHeroes', []))
      );

  }
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
   
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead   
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

}
