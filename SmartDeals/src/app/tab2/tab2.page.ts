import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page {
  currentProduct: any = {
    title: 'ابحث عن منتجك المفضل',
    price: '0.00',
    image: 'assets/placeholder.png',
    url: ''
  };

  constructor(private http: HttpClient) {}

  // دالة البحث وجلب البيانات بلمح البصر
  fetchProduct(productUrl: string) {
    const apiUrl = "http://127.0.0.1:5000/fetch_ali_details";
    this.http.post(apiUrl, { url: productUrl }).subscribe((res: any) => {
      if (res.ok) {
        this.currentProduct = {
          title: res.title,
          image: res.image,
          url: res.url,
          price: "جاري التحديث..." // يمكنك إضافة منطق لجلب السعر لاحقاً
        };
      }
    });
  }

  // دالة إتمام الدفع الكوني
  buyNow(url: string) {
    if (url) {
      window.open(url, '_system');
    }
  }
}
