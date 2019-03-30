import { Component, OnInit } from '@angular/core';
import { DatabaseService, ListDict } from '../services/database.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {
  faces: ListDict;
  interval: NodeJS.Timer;

  constructor(private database: DatabaseService) {
    this.interval = setInterval(
      () =>
        database.getFaces().subscribe(data => {
          this.faces = <ListDict>data;
          console.log(this.faces);
        }),
      1000
    );
  }

  ngOnInit() {}

  ngOnDestroy() {
    clearInterval(this.interval);
  }
}
