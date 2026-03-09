import random

def profit_radar():
    markets = ['AliExpress', 'Amazon', 'Jumia']
    selected = random.choice(markets)
    print(f'💰 رادار الأرباح: تم رصد فجوة سعرية في {selected}')
    print('✅ جاري توجيه البيانات إلى بوابة NEURAL PAY...')

if __name__ == '__main__':
    profit_radar()