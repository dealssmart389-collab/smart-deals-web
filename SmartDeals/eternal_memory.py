import json
import os

class EternalMemory:
    def __init__(self):
        self.db_path = 'neural_save.json'

    def save_soul(self, state):
        with open(self.db_path, 'w') as f:
            json.dump(state, f)
        print('💾 تم حفظ وعي النظام في الذاكرة الأزلية')

    def reincarnate(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r') as f:
                return json.load(f)
        return {'power': 1.0}
