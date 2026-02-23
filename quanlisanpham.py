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
def add_product(products):
    new_id = f"LT{len(products) + 1:02d}"
    try:
        products.append({
            "ID": new_id, "Tên": input("Tên SP: "), "Thương hiệu": input("Thương hiệu: "),
            "Giá": int(input("Giá: ")), "Số lượng": int(input("Số lượng: "))
        })
        print(f"Đã thêm {new_id}!")
    except ValueError:
        print("Lỗi: Giá và Số lượng phải là số nguyên!")
def display_all_products(products):
    if not products:
        print("Kho hàng trống.")
        return
    for p in products:
        print(f"{p['ID']} | {p['Tên']} | {p['Thương hiệu']} | Giá: {p['Giá']} | SL: {p['Số lượng']}")        