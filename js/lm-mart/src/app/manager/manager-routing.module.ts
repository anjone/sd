import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ManagerComponent } from './manager.component';
import { ManagerHomeComponent } from './manager-home/manager-home.component';
import { UserManagementComponent } from './user-management/user-management.component';
import { ReceiptLookupComponent } from './receipt-lookup/receipt-lookup.component';
import { AuthGuardService } from '../auth/auth-guard.service';
import { Role } from '../auth/role.enum';


const routes: Routes = [{
  path: '', component: ManagerComponent, children: [
    { path: '', redirectTo: '/manager/home', pathMatch: 'full' },
    {
      path: 'home',
      component: ManagerHomeComponent,
      canActivate: [AuthGuardService],
      data: {
        expectedRole: Role.Manager,
      }
    },
    {
      path: 'users',
      component: UserManagementComponent,
      children: [

      ],
      canActivate: [AuthGuardService],
      canActivateChild: [AuthGuardService],
      data: {
        expectedRole: Role.Manager,
      }
    },
    { path: 'receipts', component: ReceiptLookupComponent },
  ]
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ManagerRoutingModule { }
