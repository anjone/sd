import { TestBed } from '@angular/core/testing';

import { UserService } from './user.service';
import { commonTestingModules } from 'src/app/common/common.testing';
import { AuthService } from 'src/app/auth/auth.service';
import { AuthServiceFake } from 'src/app/auth/auth.service.fake';
import { UiService } from 'src/app/common/ui.service';

describe('UserService', () => {
  beforeEach(() => TestBed.configureTestingModule({
    imports: [commonTestingModules],
    providers: [
      UserService,
      { provide: AuthService, useClass: AuthServiceFake },
      UiService,
    ]
  }));

  it('should be created', () => {
    const service: UserService = TestBed.get(UserService);
    expect(service).toBeTruthy();
  });
});
