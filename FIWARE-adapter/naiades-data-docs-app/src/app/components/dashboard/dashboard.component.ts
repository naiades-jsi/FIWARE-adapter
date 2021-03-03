import { Component, OnInit } from '@angular/core';
import { Entity } from 'src/app/models/entity';

import { entities } from '../../models/entities';

@Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html',
    styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

    entities: Entity[] = [];
    constructor() { }

    public onOptionsSelected(value: string): void {
        console.log(value);
    }

    ngOnInit(): void {
        this.entities = entities;
    }

}
