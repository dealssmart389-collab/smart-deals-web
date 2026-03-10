import { Component } from '@angular/core';
import { NeuralSpine } from '../services/neural-spine.service';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html'
})
export class Tab1Page {
  constructor(private spine: NeuralSpine) {
    this.spine.processInteraction('Main Hub');
  }
}