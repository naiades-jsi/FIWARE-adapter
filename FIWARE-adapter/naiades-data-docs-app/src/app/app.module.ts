import { NgModule } from '@angular/core';
import { AppRouters } from './app.routes';
import { HttpClientModule } from '@angular/common/http';
import { NgxChildProcessModule } from 'ngx-childprocess';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { DashboardComponent } from './components/dashboard/dashboard.component';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent
  ],
  imports: [
    NgbModule,
    AppRouters,
    BrowserModule,
    HttpClientModule,
    NgxChildProcessModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
