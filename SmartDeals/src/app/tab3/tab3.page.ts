import { Component } from '@angular/core';
import { IonicModule, ToastController } from '@ionic/angular';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss'],
  standalone: true,
  imports: [IonicModule]
})
export class Tab3Page {
  // معرف البوت الخاص بك MyDrivingAI_Bot
  telegramBotToken: string = 'YOUR_BOT_TOKEN_HERE';
  chatId: string = 'YOUR_CHAT_ID_HERE';

  constructor(private toastCtrl: ToastController) {}

  async sendIntelToCommander(message: string) {
    const url = `https://api.telegram.org/bot${this.telegramBotToken}/sendMessage?chat_id=${this.chatId}&text=${encodeURIComponent(message)}`;
    
    fetch(url).then(async () => {
      const toast = await this.toastCtrl.create({
        message: '🚀 تم إرسال التقرير الاستخباراتي للقائد بن علال',
        duration: 2000,
        color: 'success'
      });
      toast.present();
    });
  }
}
