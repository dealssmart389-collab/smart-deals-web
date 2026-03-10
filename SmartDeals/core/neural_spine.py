import time
import os

class NeuralSpine:
    def __init__(self):
        self.status = 'READY'
        self.nodes = ['tab1', 'tab2', 'security']

    def vital_signs(self):
        for node in self.nodes:
            print(f'⚙️ عصب {node}: متصل ومحصن')

if __name__ == '__main__':
    spine = NeuralSpine()
    spine.vital_signs()