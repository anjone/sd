import { Component, OnInit, Input } from '@angular/core';

import { HackernewsApiService } from '../hackernews-api.service';

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.scss']
})
export class ItemComponent implements OnInit {
  @Input() item;

  constructor(private _hackNewsAPIService: HackernewsApiService) { }

  ngOnInit() {

  }

}
