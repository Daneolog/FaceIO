import { Component, OnInit, OnDestroy, ChangeDetectorRef } from '@angular/core';
import { DatabaseService } from '../services/database.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit, OnDestroy {
  faces = [];
  interval;

  constructor(private database: DatabaseService, private cdRef: ChangeDetectorRef) {
    this.interval = setInterval(
      () =>
        this.getDbChanges(),
      1000
    );
    this.getDbChanges();
  }

  getDbChanges() {
    this.database.getFaces().subscribe((data: any[]) => {
      this.faces = data;
      console.log(data);
      // console.log('Fetching');
      // if (this.faces.length === data.length) {
      //   for (let i = 0; i < this.faces.length; i++) {
      //     const old = data[i];
      //     const newface = this.faces[i];
      //     let change = false;
      //     ['wasAvailable', 'name', 'pfp', 'isCustomer'].forEach(val => {
      //       if (old[val] !== newface[val]) {
      //         console.log(val);
      //         change = true;
      //       }
      //     });
      //     if (change) {
      //       this.faces = data;
      //       console.log(data);
      //     }
      //   }
      // } else {
      //   this.faces = data;
      //   console.log(data);
      // }
    });
  }

  ngOnInit() {}

  ngOnDestroy() {
    clearInterval(this.interval);
  }
}
