import { Component, OnInit } from '@angular/core';
import { DataServiceService } from '../data-service.service';

@Component({
  selector: 'pictures-chart',
  templateUrl: './pictures-chart.component.html',
  styleUrls: ['./pictures-chart.component.css']
})
export class PicturesChartComponent implements OnInit {

  pics: any[];

  ngOnInit(){
    this.pics = this.dataService.getDictCategories();
  }


  constructor(private dataService: DataServiceService){
  }

  public barChartOptions:any = {
    scaleShowVerticalLines: false,
    responsive: true,
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  };

  public barChartLabels:string[] = ['cat', 'dogs','octopus'];
  public barChartType:string = 'bar';
  public barChartLegend:boolean = true;
  public barChartData:any[] = [
    {data: [65, 62, 65], label: 'Most used words'}
  ];
 
  // events
  public chartClicked(e:any):void {
    console.log(e);
    
  }
 
  public chartHovered(e:any):void {
    console.log(e);
  }
 
  public randomize():void {
    // Only Change 3 values
    console.log(this.pics);
    console.log(this.barChartData);
    let data = [
      Math.round(Math.random() * 100),
      59,
      80,
      (Math.random() * 100),
      56,
      (Math.random() * 100),
      40];
    let clone = JSON.parse(JSON.stringify(this.barChartData));
    clone[0].data = data;
    this.barChartData = clone;
    /**
     * (My guess), for Angular to recognize the change in the dataset
     * it has to change the dataset variable directly,
     * so one way around it, is to clone the data, change it and then
     * assign it;
     */
  }

}
