import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class NeuralBranch {
  activate(btn: string) {
    console.log('⚡ نبض عصبي من: ' + btn);
  }
}