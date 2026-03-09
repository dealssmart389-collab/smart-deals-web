import { Component, OnInit } from '@angular/core';
import { IonicModule, AlertController, ToastController } from '@ionic/angular';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss'],
  standalone: true,
  imports: [IonicModule]
})
export class Tab3Page implements OnInit {
  quantumLevel: number = 99.99;

  constructor(
    private alertCtrl: AlertController,
    private toastCtrl: ToastController
  ) {}

  ngOnInit() {
    this.activateNeuralPath();
  }

  async activateNeuralPath() {
    const toast = await this.toastCtrl.create({
      message: '⚡ تم تفعيل المسار العصبي للقائد منير بن علال',
      duration: 3000,
      color: 'dark',
      position: 'bottom'
    });
    toast.present();
  }

  async executeCommand(title: string) {
    const alert = await this.alertCtrl.create({
      header: '☣️ خوارزمية القيادة السيادية',
      subHeader: title,
      message: `تحليل المصفوفة: مستقر | الكفاءة: ${this.quantumLevel}%`,
      cssClass: 'quantum-alert',
      buttons: ['تأكيد السيادة']
    });
    await alert.present();
  }
}

