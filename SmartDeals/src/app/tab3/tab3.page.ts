import { Component, OnInit } from '@angular/core';
import { IonicModule, AlertController } from '@ionic/angular';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss'],
  standalone: true,
  imports: [IonicModule]
})
export class Tab3Page implements OnInit {
  systemUptime: string = '00:00:00';
  
  constructor(private alertCtrl: AlertController) {}

  ngOnInit() {
    this.startSystemClock();
  }

  // خوارزمية حساب زمن السيادة
  startSystemClock() {
    setInterval(() => {
      const now = new Date();
      this.systemUptime = now.toLocaleTimeString();
    }, 1000);
  }

  async launchProtocol(protocolName: string) {
    const alert = await this.alertCtrl.create({
      header: '☣️ بروتوكول السيادة 2100',
      message: `تم تفعيل نظام: ${protocolName} بنجاح كلي.`,
      buttons: ['إدراك']
    });
    await alert.present();
  }
}
