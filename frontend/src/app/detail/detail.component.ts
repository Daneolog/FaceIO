import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import {
  DatabaseService,
  ListDict,
  NamesDict
} from '../services/database.service';
import { Person } from '../models/person.model';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.scss']
})
export class DetailComponent implements OnInit {
  id: string;
  customer: Person;
  names: NamesDict;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private databaseService: DatabaseService
  ) {}

  ngOnInit() {
    this.id = this.route.snapshot.paramMap.get('id');

    this.databaseService.getCustomer(this.id).subscribe(data => {
      if ((<any>data).isCustomer == false) {
        this.customer = null;
      } else {
        this.customer = <Person>data;
      }
      console.log(this.customer);
    });
    this.databaseService.getNames().subscribe(data => {
      this.names = <NamesDict>data;
      console.log(this.names);
    });
  }

  select(tid: string) {
    this.databaseService.assignFace(this.id, tid).subscribe(data => {
      this.customer = <any>data;
      console.log(this.customer);
    });
  }

  addInterest(value: string) {
    console.log(value);
    this.customer.interests.push(value);
    this.databaseService.appendInterest(this.id, value).subscribe(data => {
      console.log('yay added');
    });
  }
}
