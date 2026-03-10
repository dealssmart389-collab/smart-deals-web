import json

def compare_prices():
    prices = [
        {"item": "iPhone 17 Pro", "global": "1100$", "local": "13500 DH", "diff": "+15%"},
        {"item": "Redmi Note 15 Pro+", "global": "380$", "local": "4500 DH", "diff": "+10%"},
        {"item": "Watch Ultra 3", "global": "799$", "local": "8200 DH", "diff": "+12%"}
    ]
    return prices

if __name__ == "__main__":
    print(json.dumps(compare_prices()))
