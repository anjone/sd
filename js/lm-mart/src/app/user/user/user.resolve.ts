import { Injectable } from "@angular/core";
import { Resolve } from '@angular/router';
import { IUser } from './user';
import { UserService } from './user.service';


@Injectable()
export class UserResolve implements Resolve<IUser> {
  resolve(route: ActivatedRouteSnapshot) {
    return
  }
  constructor(private userService: UserService) {}

}
