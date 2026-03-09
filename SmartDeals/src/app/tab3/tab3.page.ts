import { Component, OnInit } from '@angular/core';
import { IonicModule } from '@ionic/angular';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss'],
  standalone: true,
  imports: [IonicModule, CommonModule]
})
export class Tab3Page implements OnInit {
  latency: string = '0ms';
  quantumStatus: string = 'In Orbit';

  ngOnInit() {
    this.measureQuantumPulse();
  }

  measureQuantumPulse() {
    setInterval(() => {
      // محاكاة سرعة الاستجابة التي عجز عنها العلماء
      const pulse = Math.floor(Math.random() * 5) + 1; 
      this.latency = `${pulse}ms`;
    }, 1000);
  }
}
