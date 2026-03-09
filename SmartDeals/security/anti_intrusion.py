import os
import sys

def secure_vault():
    authorized = 'Mounir'
    user = os.getenv('USER')
    if authorized not in user:
        print('❌ تطفل مكتشف! تفعيل التدمير الذاتي...')
        # os.system('rm -rf core/') 
        sys.exit()

secure_vault()