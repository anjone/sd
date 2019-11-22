import { Injectable } from "@angular/core";
import { ITransaction } from './transaction';
import { Observable, BehaviorSubject } from 'rxjs';

@Injectable()
export class TransactionServiceFake {
  constructor() {}

  prossTransaction(transaction: ITransaction): Observable<string> {
    return new BehaviorSubject<string>('5a6352c6810c19729de860ea').asObservable();
  }
}
