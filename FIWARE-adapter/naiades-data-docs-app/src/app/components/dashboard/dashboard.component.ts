import { Component, OnInit } from '@angular/core';
import { DataSummary } from 'src/app/models/dataSummary';
import { Entity } from 'src/app/models/entity';
import { entities } from '../../models/entities';
import { EntitiesService } from '../../services/entities.service';

@Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html',
    styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
    // http://jsfiddle.net/KJQ9K/554/
    // http://jsfiddle.net/unLSJ/

    entities: Entity[] = [];
    public dataSummary: DataSummary | undefined;
    constructor(private entitiesService: EntitiesService) { }

    private async getDataSummary(index: number): Promise<void> {
        const entity = this.entities[index];
        const res = await this.entitiesService.getFirstEntity(entity.entityId, entity.service);
        console.log(res);
    }

    public onOptionsSelected(idx: string): void {
        this.getDataSummary(Number(idx));
    }

    ngOnInit(): void {
        this.entities = entities;
        this.getDataSummary(0);
    }

}
