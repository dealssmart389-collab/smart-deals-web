def check_safety_rule(action):
    rules = {"السرعة": "يجب عدم تجاوز 60 كم/س", "الإشارة": "توقف عند الأحمر"}
    return rules.get(action, "قاعدة غير مسجلة")

print("🚀 Driving AI 2026 Core: Online")
print(f"قاعدة السرعة: {check_safety_rule('السرعة')}")
