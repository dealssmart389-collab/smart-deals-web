import json

def check_global_updates():
    alerts = [
        {"id": 101, "title": "إصدار جديد!", "body": "وصل الآن Redmi Note 15 Ultra إلى المخازن العالمية.", "type": "product"},
        {"id": 102, "title": "تنبيه أمني", "body": "نظام المناعة نشط وقام بتطهير العروق بنجاح.", "type": "security"}
    ]
    return alerts

if __name__ == "__main__":
    print(json.dumps(check_global_updates()))
