import { Component } from '@angular/core';
import { IonicModule, AlertController } from '@ionic/angular';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss'],
  standalone: true,
  imports: [IonicModule]
})
export class Tab3Page {
  constructor(private alertController: AlertController) {}

  async commandAction(title: string) {
    const alert = await this.alertController.create({
      header: 'بروتوكول 2100',
      message: `تم تفعيل أمر: ${title}`,
      buttons: ['تأكيد السيادة']
    });
    await alert.present();
  }
}
