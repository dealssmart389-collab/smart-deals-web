import { Component } from '@angular/core';
import { IonicModule, LoadingController } from '@ionic/angular';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
  standalone: true,
  imports: [IonicModule, CommonModule, FormsModule]
})
export class Tab1Page {
  searchQuery: string = '';
  radarActive: boolean = false;
  foundItems: any[] = [];

  constructor(private loadingCtrl: LoadingController) {}

  async activateRadar() {
    if (!this.searchQuery) return;
    
    this.radarActive = true;
    const loading = await this.loadingCtrl.create({
      message: '📡 جاري اختراق قواعد بيانات التجارة العالمية...',
      spinner: 'bubbles',
      duration: 1500
    });
    await loading.present();

    // محاكاة جلب ملايين البيانات في ثانية
    setTimeout(() => {
      this.foundItems = [
        { name: 'منتج فضائي من AliExpress', price: '120 DH', deal: 'خصم 40%' },
        { name: 'خدمة كونية من Amazon', price: '250 DH', deal: 'شحن مجاني' },
        { name: 'منتزه رقمي من Jumia', price: '45 DH', deal: 'عرض محدود' }
      ];
      loading.dismiss();
    }, 1500);
  }
}
