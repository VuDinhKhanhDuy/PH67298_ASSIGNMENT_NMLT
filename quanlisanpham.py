import json

def load_data():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(products):
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=4, ensure_ascii=False)