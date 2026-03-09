import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html'
})
export class Tab2Page implements OnInit {
  universal_count: number = 1;

  ngOnInit() {
    setInterval(() => {
      this.universal_count *= 1.000001; 
    }, 10);
  }
}