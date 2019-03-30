import { Component, OnInit } from '@angular/core';
import { Person } from '../models/person.model';
import { DatabaseService, ListDict } from '../services/database.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {
  faces: ListDict;

  constructor(private database: DatabaseService) {
    database.getFaces().subscribe(data => {
      this.faces = <ListDict>data;
      console.log(this.faces);
    });
  }

  ngOnInit() {}
}
