import { NgModule } from '@angular/core';
import { MatStepperModule } from '@angular/material/stepper';
import { MatRadioModule } from '@angular/material/radio';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatSelectModule } from '@angular/material/select';
import { MatDividerModule } from '@angular/material/divider';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatNativeDateModule } from '@angular/material/core';
import { MatLineModule } from '@angular/material/core'


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
