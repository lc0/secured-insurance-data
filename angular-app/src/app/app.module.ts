import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeartChartComponent } from './heart-chart/heart-chart.component';
import { ChartsModule } from 'ng2-charts';
import { PicturesChartComponent } from './pictures-chart/pictures-chart.component';
import { HttpClientModule }    from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    HeartChartComponent,
    PicturesChartComponent
  ],
  imports: [
    BrowserModule,
    ChartsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
