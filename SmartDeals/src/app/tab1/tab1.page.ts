import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})
export class Tab1Page {
  constructor(private http: HttpClient) {}

  triggerBot() {
    const adMessage = "🚀 إشعار متقدم: العنان يغزو الأسواق العالمية الآن!";
    this.http.post('http://127.0.0.1:5000/send_ad', { message: adMessage })
      .subscribe(
        res => console.log('تم الإرسال بنجاح!'),
        err => console.error('فشل الاتصال، تأكد من تشغيل app_bridge.py')
      );
  }
}
