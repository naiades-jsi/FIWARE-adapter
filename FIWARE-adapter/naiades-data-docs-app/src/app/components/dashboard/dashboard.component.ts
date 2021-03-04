import { Component, OnInit } from '@angular/core';

import { Entity } from 'src/app/models/entity';
import { entities } from '../../models/entities';
import { DataSummary } from 'src/app/models/dataSummary';
import { EntitiesService } from '../../services/entities.service';

@Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html',
    styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
    timer: any;
    entities: Entity[] = [];
    public dataSummary: DataSummary;

    constructor(private entitiesService: EntitiesService) {
        this.dataSummary = {
            http_status: -1,
            first_date: '',
            sample_count: -1,
            last_date: '',
            sample_json: ''
        };
    }

    private async getDataSummary(index: number): Promise<void> {
        const entity = this.entities[index];
        await this.entitiesService
                    .getFirstEntity(entity.entityId, entity.service)
                    .then((data) => {
                        this.dataSummary = data;
                        this.dataSummary.sample_json = JSON.stringify(this.dataSummary.sample_json);

                        this.timer = setInterval(() => {
                            if (document.getElementById('jsonString') != null) {
                                this.syntaxHighlight(JSON.stringify(JSON.parse(data.sample_json), undefined, 4));
                            }
                        },  100);
                    });
    }

    private syntaxHighlight(json: string): void {
        clearInterval(this.timer);
        json = json.substring(1, json.length - 1);
        json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        const element = document.getElementById('jsonString');
        if (element){
            element.innerHTML = json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g,
                (match: string) => {
                    let color = 'darkorange';
                    if (/^"/.test(match)) {
                        if (/:$/.test(match)) {
                            color = 'green';
                        } else {
                            color = 'blue';
                        }
                    } else if (/true|false/.test(match)) {
                        color = 'red';
                    } else if (/null/.test(match)) {
                        color = 'magenta';
                    }
                    return '<span style=\"color: ' + color + ';\">' + match + '</span>';
                }
            );
        }
    }
    public onOptionsSelected(idx: string): void {
        this.getDataSummary(Number(idx));
    }

    ngOnInit(): void {
        this.entities = entities;
        this.getDataSummary(0);
    }
}
