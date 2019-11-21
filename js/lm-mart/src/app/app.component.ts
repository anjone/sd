import { Component, ViewChild, OnInit } from '@angular/core';
import { MatIconRegistry, MatSidenav } from '@angular/material';
import { MediaObserver } from '@angular/flex-layout';
import { DomSanitizer } from '@angular/platform-browser';
import { AuthService } from './auth/auth.service';
import { ObservableMediaFake } from './common/common.testing';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  @ViewChild('sidenav') public sideNav: MatSidenav;

  ngOnInit(): void {
    this.authService.authStatus.subscribe(authStatus => {
      if (!authStatus.isAuthenticated) {
        this.sideNav.close();
      }
    });
  }
  // title = 'lm-mart';

  constructor(
    iconRegistry: MatIconRegistry,
    sanitizer: DomSanitizer,
    public authService: AuthService,
    public media: MediaObserver,
  ) {
    iconRegistry.addSvgIcon(
      'lemon',
      sanitizer.bypassSecurityTrustResourceUrl('assets/img/icons/lemon.svg')
    );
  }
}
