import { Component } from '@angular/core';
import { InteractionService } from '../services/interaction.service';

@Component({ selector: 'app-tab1', templateUrl: 'tab1.page.html' })
export class Tab1Page {
  constructor(public blood: InteractionService) {}
}