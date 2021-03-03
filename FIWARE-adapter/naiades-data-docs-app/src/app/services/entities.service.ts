import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { environment } from '../../environments/environment';
import { Entity } from '../models/entity';

@Injectable({
    providedIn: 'root'
})

export class EntitiesService {
    private apiUrl = environment.apiUrl;
    private apiPort = environment.apiPort;

    constructor(private http: HttpClient){}

    public getFirstEntity(entityId: string, service: string): Promise<Entity> {
        const url = `http://${this.apiUrl}:${this.apiPort}/v2/entities/${entityId}?limit=1`;
        const headers = new HttpHeaders({
            'Fiware-ServicePath': '/',
            'Fiware-Service': service,
            'Content-Type': 'application/json'
        });
        const res = this.http
                        .get(url, {headers})
                        .toPromise()
                        .catch(this.handleError);
        return res;
    }

    public getLastEntity(entityId: string, service: string): Promise<Entity> {
        const url = `http://${this.apiUrl}:${this.apiPort}/v2/entities/${entityId}?lastN=1`;
        const headers = new HttpHeaders({
            'Fiware-ServicePath': '/',
            'Fiware-Service': service,
            'Content-Type': 'application/json'
        });
        const res = this.http
                        .get(url, {headers})
                        .toPromise()
                        .catch(this.handleError);
        return res;
    }

    public getAllSamplesCount(entityId: string, service: string, attribute: string): Promise<Entity> {
        const url = `http://${this.apiUrl}:${this.apiPort}/v2/entities/${entityId}?attrs=${attribute}&aggrMethod=count`;
        const headers = new HttpHeaders({
            'Fiware-ServicePath': '/',
            'Fiware-Service': service,
            'Content-Type': 'application/json'
        });
        const res = this.http
                        .get(url, {headers})
                        .toPromise()
                        .catch(this.handleError);
        return res;
    }

    private handleError(error: any): Promise<any> {
        console.error('An error occured', error.error.errmsg || error);
        return Promise.reject(error.error.errmsg || error);
    }
}
