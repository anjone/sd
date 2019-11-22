import { Injectable } from '@angular/core';
import { IUser, User } from './user';
import { BehaviorSubject, Observable, throwError as observableThrowError } from 'rxjs';
import { CacheService } from 'src/app/auth/cache.service';
import { IAuthStatus, AuthService } from 'src/app/auth/auth.service';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { transformError } from 'src/app/common/common';
import { environment } from 'src/environments/environment';

export interface IUsers {
  items: IUser[];
  total: number;
}

export interface IUserService {
  currentUser: BehaviorSubject<IUser>;
  getCurrentUser(): Observable<IUser>;
  getUser(id): Observable<IUser>;
  updateUser(user: IUser): Observable<IUser>;
  getUsers(pageSize: number, searchText: string, pagesToSkip: number): Observable<IUsers>;
}

@Injectable({
  providedIn: 'root'
})
export class UserService extends CacheService implements IUserService {
  currentUser = new BehaviorSubject<IUser>(this.getItem('user') || new User());
  private currentAuthStatus: IAuthStatus;

  getCurrentUser(): Observable<IUser> {
    const userObservable = this.getUser(this.currentAuthStatus.userId).pipe(
      catchError(transformError)
    );
    userObservable.subscribe(
      user => this.currentUser.next(user),
      err => observableThrowError(err)
    );

    return userObservable;
  }

  getUser(id: any): Observable<IUser> {
    return this.httpClient.get<IUser>(`${environment.baseUrl}/v1/user/${id}`);
  }

  updateUser(user: IUser): Observable<IUser> {
    this.setItem('draft-user', user);
    const updateResponse = this.httpClient.put<IUser>(
      `${environment.baseUrl}/v1/user/${user.id || 0}`,
      user
    ).pipe(catchError(transformError));

    updateResponse.subscribe(
      res => {
        this.currentUser.next(res);
        this.removeItem('draft-user');
      },
      err => observableThrowError(err)
    );

    return updateResponse;
  }

  getUsers(pageSize: number, searchText = '', pagesToSkip = 0): Observable<IUsers> {
    return this.httpClient.get<IUsers>(
      `${environment.baseUrl}/v1/users`,
      {
        params: {
          search: searchText,
          offset: pagesToSkip.toString(),
          limit: pageSize.toString(),
        },
      }
    );
  }

  constructor(private httpClient: HttpClient, private authService: AuthService) {
    super();
    this.currentUser.subscribe(user => this.setItem('user', user));
    this.authService.authStatus.subscribe(
      authStatus => (this.currentAuthStatus = authStatus)
    );
  }
}
