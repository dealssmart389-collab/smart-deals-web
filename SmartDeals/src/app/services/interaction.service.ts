import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class InteractionService {
  logClick(buttonName: string) {
    console.log('⚡ تم النقر على: ' + buttonName);
    // إرسال تنبيه صوتي في الترمكس
    // window.fetch('http://localhost:8080/alert?btn=' + buttonName);
  }
}