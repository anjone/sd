import { Component, OnInit, Input } from '@angular/core';
import { IUser, User } from '../user/user';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-view-user',
  templateUrl: './view-user.component.html',
  styleUrls: ['./view-user.component.scss']
})
export class ViewUserComponent implements OnInit {
  @Input()
  user: IUser;

  currentUser = new User();

  get editMode() {
    return !this.user;
  }

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    if (this.user) {
      this.currentUser = User.BuildUser(this.user);
    }

    if (this.route.snapshot && this.route.snapshot.data) {
      this.currentUser = User.BuildUser(this.route.snapshot.data.user);
      this.currentUser.dateOfBirth = Date.now();
    }
  }

}
