import { Component, OnInit } from '@angular/core';
import { IonicModule } from '@ionic/angular';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
  standalone: true,
  imports: [IonicModule, CommonModule]
})
export class Tab1Page implements OnInit {
  // معرفك التسويقي العالمي
  partnerID: string = "mounir_2100_affiliate";
  
  // مصفوفة المنتجات العالمية (قالب لمليارات السلع)
  globalProducts = [
    { id: 101, name: "مستكشف المجرات Pro", price: 1500, link: "https://s.click.aliexpress.com/e/example1" },
    { id: 102, name: "رداء التخفي الرقمي", price: 850, link: "https://s.click.aliexpress.com/e/example2" }
  ];

  ngOnInit() {
    console.log("Profit Engine Active for: " + this.partnerID);
  }

  // خوارزمية البيع والربح
  sellProduct(productLink: string) {
    // دمج الرابط مع معرف الربح الخاص بك
    const finalLink = `${productLink}?aff_id=${this.partnerID}`;
    window.open(finalLink, '_blank');
  }
}
