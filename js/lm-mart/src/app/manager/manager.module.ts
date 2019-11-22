import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ManagerRoutingModule } from './manager-routing.module';
import { ManagerHomeComponent } from './manager-home/manager-home.component';
import { ManagerComponent } from './manager.component';
import { MaterialModule } from '../material.module';
import { UserManagementComponent } from './user-management/user-management.component';
import { ReceiptLookupComponent } from './receipt-lookup/receipt-lookup.component';
import { UserTableComponent } from './user-table/user-table.component';
import { ManagerMaterialModule } from './manager.material.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SharedComponentsModule } from '../shared-components.module';
import { FlexLayoutModule } from '@angular/flex-layout';
import { AuthGuardService } from '../auth/auth-guard.service';
import { UserService } from '../user/user/user.service';
import { UserResolve } from '../user/user/user.resolve';


@NgModule({
  declarations: [
    ManagerHomeComponent,
    ManagerComponent,
    UserManagementComponent,
    ReceiptLookupComponent,
    UserTableComponent
  ],
  imports: [
    CommonModule,
    ManagerRoutingModule,
    ManagerMaterialModule,
    MaterialModule,
    FormsModule,
    ReactiveFormsModule,
    SharedComponentsModule,
    FlexLayoutModule,
  ],
  providers: [
    AuthGuardService,
    UserService,
    UserResolve,
  ]
})
export class ManagerModule { }
