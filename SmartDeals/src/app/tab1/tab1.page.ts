import { Component, OnInit } from '@angular/core';
import { IonicModule } from '@ionic/angular';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
  standalone: true,
  imports: [IonicModule, CommonModule]
})
export class Tab1Page implements OnInit {
  // السعر الأساسي بالدرهم المغربي
  basePriceMAD: number = 9999;
  dynamicPrice: number = 9999;
  exchangeRate: number = 0.098; // معامل التحويل للدولار
  
  ngOnInit() {
    this.igniteQuantumPricing();
  }

  // خوارزمية التذبذب الرياضي - تجعل لغات البرمجة ترتجف
  igniteQuantumPricing() {
    setInterval(() => {
      // استخدام دالة الجيب (Sine Wave) لمحاكاة نبض السوق الرقمي
      const time = Date.now() / 1000;
      const oscillation = Math.sin(time) * 50; 
      this.dynamicPrice = Math.round(this.basePriceMAD + oscillation);
    }, 100); // تحديث كل 100 مللي ثانية لنبض حي
  }

  get priceInUSD() {
    return (this.dynamicPrice * this.exchangeRate).toFixed(2);
  }
}
