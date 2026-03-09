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
  systemStatus: string = 'نشط';
  quantumLevel: number = 99.9;

  constructor(
    private alertCtrl: AlertController,
    private toastCtrl: ToastController
  ) {}

  ngOnInit() {
    this.initCommandCenter();
  }

  async initCommandCenter() {
    const toast = await this.toastCtrl.create({
      message: 'تم تفعيل البروتوكول العصبي لمنير بن علال',
      duration: 2000,
      color: 'tertiary',
      position: 'top'
    });
    toast.present();
  }

  async executeQuantumAction(cmd: string) {
    const alert = await this.alertCtrl.create({
      header: '☣️ خوارزمية القيادة السيادية',
      subHeader: `الأمر: ${cmd}`,
      message: `جاري تحليل المصفوفة الرياضية... الحالة: ${this.quantumLevel}% كفاءة.`,
      cssClass: 'quantum-alert',
      buttons: [{ text: 'تأكيد السيادة', handler: () => { console.log('Command Executed'); } }]
    });
    await alert.present();
  }
}

