import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UserRoutingModule } from './user-routing.module';
import { ProfileComponent } from './profile/profile.component';
import { LogoutComponent } from './logout/logout.component';
import { MaterialModule } from '../material.module';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { FlexLayoutModule } from '@angular/flex-layout';
import { UserMaterialModule } from './user.material.module';
import { SharedComponentsModule } from '../shared-components.module';
import { UserService } from './user/user.service';
import { AuthGuardService } from '../auth/auth-guard.service';


@NgModule({
  declarations: [
    ProfileComponent,
    LogoutComponent,
  ],
  imports: [
    CommonModule,
    UserRoutingModule,
    MaterialModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    FlexLayoutModule,
    UserMaterialModule,
    SharedComponentsModule,
  ],
  providers: [
    UserService,
    AuthGuardService,
  ]
})
export class UserModule { }
