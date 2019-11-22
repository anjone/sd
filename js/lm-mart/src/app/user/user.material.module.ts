import { NgModule } from '@angular/core';
import {
  MatStepperModule,
  MatRadioModule,
  MatDatepickerModule,
  MatSelectModule,
  MatDividerModule,
  MatAutocompleteModule,
  MatNativeDateModule,
  MatLineModule
} from '@angular/material';

@NgModule({
  imports: [
    MatStepperModule,
    MatRadioModule,
    MatDatepickerModule,
    MatSelectModule,
    MatDividerModule,
    MatAutocompleteModule,
    MatNativeDateModule,
    MatLineModule,
  ],
  exports: [
    MatStepperModule,
    MatRadioModule,
    MatDatepickerModule,
    MatSelectModule,
    MatDividerModule,
    MatAutocompleteModule,
    MatNativeDateModule,
    MatLineModule,
  ],
})
export class UserMaterialModule {}
