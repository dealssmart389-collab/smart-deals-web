import { Component } from '@angular/core';

@Component({ selector: 'app-tab2', templateUrl: 'tab2.page.html' })
export class Tab2Page {
  products = [
    { name: 'Redmi Note 15 Pro+', price: '4500 DH', image: 'https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400', tag: 'New' },
    { name: 'Apple Watch Ultra 3', price: '8200 DH', image: 'https://images.unsplash.com/photo-1544117518-2b476dd354d2?w=400', tag: 'Limited' }
  ];
  constructor() {}
}