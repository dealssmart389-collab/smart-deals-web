import { Component } from '@angular/core';
import { InteractionService } from '../services/interaction.service';

@Component({ selector: 'app-tab3', templateUrl: 'tab3.page.html' })
export class Tab3Page {
  constructor(public blood: InteractionService) {}
}