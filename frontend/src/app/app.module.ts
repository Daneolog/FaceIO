import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { ListComponent } from './list/list.component';
import { DetailComponent } from './detail/detail.component';
import { HttpClientModule } from '@angular/common/http';
import { PromotionsComponent } from './promotions/promotions.component';
import { PromoDetailComponent } from './promo-detail/promo-detail.component';

const routes: Routes = [
  { path: 'main', component: ListComponent },
  { path: 'detail/:id', component: DetailComponent },
  { path: 'promos', component: PromotionsComponent },
  { path: 'promos/:id', component: PromoDetailComponent },
  { path: '**', redirectTo: 'main' }
];

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    ListComponent,
    DetailComponent,
    PromotionsComponent,
    PromoDetailComponent
  ],
  imports: [RouterModule.forRoot(routes), BrowserModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
