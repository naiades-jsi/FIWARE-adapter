import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpRequest, HttpEvent } from '@angular/common/http';

import { environment } from '../../environments/environment';
import { Entity } from '../models/entity';
import { Observable } from 'rxjs';
import { DataSummary } from '../models/dataSummary';

@Injectable({
    providedIn: 'root'
})

export class EntitiesService {
    private apiUrl = environment.apiUrl;

    constructor(private http: HttpClient){}

    public getFirstEntity(entityId: string, service: string): Promise<DataSummary> {
        const url = `http://${this.apiUrl}/entitySummary?entityId=${entityId}&service=${service}`;
        const res = this.http
                        .get(url)
                        .toPromise()
                        .catch(this.handleError);
        return res;
    }

    private handleError(error: any): Promise<any> {
        console.error('An error occured', error.error.errmsg || error);
        return Promise.reject(error.error.errmsg || error);
    }
}
