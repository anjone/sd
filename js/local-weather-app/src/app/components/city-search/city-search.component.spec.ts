import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CitySearchComponent } from './city-search.component';
import { MaterialModule } from 'src/app/material.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { WeatherServiceFake } from 'src/app/services/weather/weather.service.fake';
import { WeatherService } from 'src/app/services/weather/weather.service';

describe('CitySearchComponent', () => {
  let component: CitySearchComponent;
  let fixture: ComponentFixture<CitySearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CitySearchComponent ],
      providers: [{ provide: WeatherService, useClass: WeatherServiceFake }],
      imports: [MaterialModule, NoopAnimationsModule, FormsModule, ReactiveFormsModule],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CitySearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
