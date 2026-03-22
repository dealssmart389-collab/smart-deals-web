import json

def add_product(name, price, stock, platform="Jumia"):
    product = {"name": name, "price": price, "stock": stock, "platform": platform}
    with open('inventory.json', 'a+') as f:
        f.write(json.dumps(product) + '\n')
    print(f"✅ تم إضافة {name} إلى مخازن Smart Deals")

if __name__ == "__main__":
    add_product("Smart Watch Ultra", "299 DH", 15)
