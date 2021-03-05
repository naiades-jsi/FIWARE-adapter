import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../environments/environment';
import { DataSummary } from '../models/dataSummary';
import { interval } from 'rxjs';
import { first } from 'rxjs/operators';

@Injectable({
    providedIn: 'root'
})

export class EntitiesService {
    private serverApiUrl = environment.apiUrl;
    private fiwareApiUrl = environment.fiwareApiUrl;
    private source = interval(5000);
    private pythonServerStatus = false;
    private fiwareApiStatus = false;

    constructor(private http: HttpClient){
        this.source.subscribe(() => {
            this.http
                .get(`http://${this.serverApiUrl}/ping`, { observe: 'response' })
                .pipe(first())
                .subscribe(resp => {
                    if (resp.status === 200){
                        this.pythonServerStatus = true;
                    } else {
                        this.pythonServerStatus = false;
                    }
                }, err => this.pythonServerStatus = false);
            // this.http
            //     .get(`http://${this.fiwareApiUrl}/v2/health`, { observe: 'response' })
            //     .pipe(first())
            //     .subscribe(resp => {
            //         if (resp.status === 200){
            //             this.fiwareApiStatus = true;
            //         } else {
            //             this.fiwareApiStatus = false;
            //         }
            //     }, err => this.fiwareApiStatus = false);
        });
    }

    public getFirstEntity(entityId: string, service: string): Promise<DataSummary> {
        const url = `http://${this.serverApiUrl}/entitySummary?entityId=${entityId}&service=${service}`;
        const res = this.http
                        .get(url)
                        .toPromise()
                        .catch(this.handleError);
        return res;
    }

    public getServerStatus(): boolean {
        return this.pythonServerStatus;
    }

    public getFiwareApiStatus(): boolean {
        return this.fiwareApiStatus;
    }

    private handleError(error: any): Promise<any> {
        console.error('An error occured', error.error.errmsg || error);
        return Promise.reject(error.error.errmsg || error);
    }
}
