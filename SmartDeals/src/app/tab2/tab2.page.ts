import { Component } from '@angular/core';
import { IonicModule, AlertController } from '@ionic/angular';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss'],
  standalone: true,
  imports: [IonicModule]
})
export class Tab2Page {
  constructor(private alertController: AlertController) {}

  async confirmPayment() {
    const alert = await this.alertController.create({
      header: 'تأكيد العملية الكونية',
      message: 'تم تفعيل نظام Visa لعام 2100 بنجاح!',
      buttons: ['إغلاق']
    });
    await alert.present();
  }
}
