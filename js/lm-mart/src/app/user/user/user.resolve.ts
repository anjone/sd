import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot } from '@angular/router';
import { IUser } from './user';
import { UserService } from './user.service';


@Injectable()
export class UserResolve implements Resolve<IUser> {
  resolve(route: ActivatedRouteSnapshot) {
    return this.userService.getUser(route.paramMap.get('userId'));
  }
  constructor(private userService: UserService) {}

}
