<ion-card>
  <ion-card-header>
    <ion-card-title>لوحة التحكم في العنان 🔱</ion-card-title>
  </ion-card-header>
  <ion-card-content>
    <ion-item>
      <ion-label position="floating">رسالة الإعلان</ion-label>
      <ion-input [(ngModel)]="adMessage" placeholder="اكتب عرضك هنا..."></ion-input>
    </ion-item>
    <ion-button expand="full" (click)="sendTelegramAd()">
      إرسال عبر البوت 🚀
    </ion-button>
  </ion-card-content>
</ion-card>
