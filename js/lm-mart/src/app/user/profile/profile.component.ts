import { Component, OnInit } from '@angular/core';

import { Role as UserRole } from '../../auth/role.enum';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Observable } from 'rxjs';
import { IUSState } from './data';
import { Router } from '@angular/router';
import { UserService } from '../user/user.service';
import { AuthService } from 'src/app/auth/auth.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  Role = UserRole;
  PhoneTypes = $enum(PhoneType).getKeys();
  userForm: FormGroup;
  states: Observable<IUSState[]>;
  userError: '';
  currentUserRole = this.Role.None;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private userService: UserService,
    private authService: AuthService
  ) { }

  ngOnInit() {
  }

}
