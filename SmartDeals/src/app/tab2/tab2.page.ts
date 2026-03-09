import { Component } from '@angular/core';
import { IonicModule } from '@ionic/angular';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss'],
  standalone: true,
  imports: [IonicModule, CommonModule]
})
export class Tab2Page {
  // مصفوفة كونية مهيأة لاستقبال ملايين المنتجات
  cosmicProducts = [
    { id: 1, name: 'منتزه أندروميدا الرقمي', price: 500000, category: 'منتزهات' },
    { id: 2, name: 'سحابة التخزين السديمية', price: 1200, category: 'بضائع' }
  ];

  constructor() {}

  calculateTotal() {
    return this.cosmicProducts.reduce((acc, prod) => acc + prod.price, 0);
  }
}
