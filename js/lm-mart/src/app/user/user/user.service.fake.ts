import { Injectable } from '@angular/core';
import { IUserService, IUsers } from './user.service';
import { BehaviorSubject, Observable, of } from 'rxjs';
import { IUser, User } from './user';


@Injectable()
export class UserServiceFake implements IUserService {
  currentUser = new BehaviorSubject<IUser>(new User());

  getCurrentUser(): Observable<IUser> {
    return of(new User());
  }

  getUser(id: any): Observable<IUser> {
    return of(new User((id = id)));
  }

  updateUser(user: IUser): Observable<IUser> {
    return of(user);
  }

  getUsers(pageSize: number, searchText: string, pagesToSkip: number): Observable<IUsers> {
    return of({
      total: 1,
      items: [new User()],
    } as IUsers);
  }

}
