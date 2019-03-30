import { Component, OnInit } from '@angular/core';
import { DatabaseService, PromotionsDict } from '../services/database.service';

@Component({
  selector: 'app-promotions',
  templateUrl: './promotions.component.html',
  styleUrls: ['./promotions.component.scss']
})
export class PromotionsComponent implements OnInit {
  promotions: PromotionsDict;

  constructor(private database: DatabaseService) {}

  ngOnInit() {
    this.database.getPromotions().subscribe(data => {
      this.promotions = data;
      console.log(this.promotions);
    });
  }
}
