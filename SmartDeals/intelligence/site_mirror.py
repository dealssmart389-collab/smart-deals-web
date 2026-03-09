import os

def check_site_status():
    status = os.system('curl -s -o /dev/null -w "%{http_code}" https://dealssmart389-collab.github.io/smart-deals-web/')
    if status == 200:
        print('🌍 المرآة الرقمية: بوابة 2100 متصلة وبالكامل تحت السيطرة')

check_site_status()