import { Component } from '@angular/core';
import { InteractionService } from '../services/interaction.service';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html'
})
export class Tab1Page {
  constructor(public interaction: InteractionService) {}

  openNeuralSettings() {
    console.log('⚡ فتح الإعدادات عبر الاتصال العصبي...');
    // هنا نضع كود إظهار لوحة التحكم مباشرة
    this.interaction.logClick('Settings Portal');
  }
}