import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { ListComponent } from './list/list.component';
import { DetailComponent } from './detail/detail.component';
import { HttpClientModule } from '@angular/common/http';

const routes: Routes = [
  { path: 'main', component: ListComponent },
  { path: 'detail/:id', component: DetailComponent },
  { path: '**', redirectTo: 'main' }
];

@NgModule({
  declarations: [AppComponent, HeaderComponent, ListComponent, DetailComponent],
  imports: [RouterModule.forRoot(routes), BrowserModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
