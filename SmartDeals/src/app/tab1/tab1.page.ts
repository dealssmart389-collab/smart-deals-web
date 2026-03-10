import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ToastController } from '@ionic/angular';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})
export class Tab1Page {
  dealMessage: string = "";

  constructor(private http: HttpClient, private toast: ToastController) {}

  async sendDeal() {
    const apiUrl = "http://127.0.0.1:5000/send_deal";
    
    this.http.post(apiUrl, { message: this.dealMessage }).subscribe(
      async (res: any) => {
        const toast = await this.toast.create({
          message: '✅ تم النشر بنجاح!',
          duration: 2000,
          color: 'success',
          position: 'top'
        });
        toast.present();
        this.dealMessage = ""; 
      },
      async (err) => {
        const toast = await this.toast.create({
          message: '❌ فشل الإرسال: تأكد من تشغيل السيرفر في Termux',
          duration: 3000,
          color: 'danger',
          position: 'top'
        });
        toast.present();
      }
    );
  }
}
