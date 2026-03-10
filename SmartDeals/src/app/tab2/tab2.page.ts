import { Component } from '@angular/core';
import { InteractionService } from '../services/interaction.service';

@Component({ selector: 'app-tab2', templateUrl: 'tab2.page.html' })
export class Tab2Page {
  constructor(public blood: InteractionService) {}
}