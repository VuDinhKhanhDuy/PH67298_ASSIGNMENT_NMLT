import json

# 1. Tải dữ liệu
def load_data():
    """Đọc file products.json, trả về list rỗng nếu file chưa tồn tại."""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError: 
        return []

# 2. Lưu dữ liệu
def save_data(products):
    """Lưu danh sách vào file json."""
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

# 3. Thêm sản phẩm
def add_product(products):
    """Thêm sản phẩm và tự động tạo ID."""
    new_id = f"LT{len(products) + 1:02d}" 
    try:
        products.append({
            "ID": new_id,
            "Tên": input("Nhập tên laptop: "),
            "Thương hiệu": input("Nhập thương hiệu: "),
            "Giá": int(input("Nhập giá bán (VNĐ): ")),
            "Số lượng": int(input("Nhập số lượng tồn kho: "))
        })
        print(f"--> Đã thêm sản phẩm thành công với mã {new_id}!")
    except ValueError:
        print("--> LỖI: Giá và Số lượng bắt buộc phải là số nguyên!")
    return products

# 4. Cập nhật sản phẩm
def update_product(products):
    """Tìm theo ID và cập nhật thông tin."""
    pid = input("Nhập mã ID sản phẩm cần cập nhật: ").strip().upper()
    for p in products:
        if p["ID"] == pid:
            print(f"Đang sửa thông tin cho: {p['Tên']}")
            p["Tên"] = input(f"Tên mới ({p['Tên']}): ") or p["Tên"]
            p["Thương hiệu"] = input(f"Thương hiệu ({p['Thương hiệu']}): ") or p["Thương hiệu"]
            try:
                gia = input(f"Giá mới ({p['Giá']}): ")
                if gia: p["Giá"] = int(gia)
                sl = input(f"Số lượng mới ({p['Số lượng']}): ")
                if sl: p["Số lượng"] = int(sl)
                print("--> Đã cập nhật thành công!")
            except ValueError:
                print("--> LỖI: Giá và Số lượng phải là số!")
            return
    print("--> LỖI: Không tìm thấy mã sản phẩm này!")

# 5. Xóa sản phẩm
def delete_product(products):
    """Xóa sản phẩm theo ID."""
    pid = input("Nhập mã ID sản phẩm cần xóa: ").strip().upper()
    for i, p in enumerate(products):
        if p["ID"] == pid:
            del products[i]
            print("--> Đã xóa sản phẩm khỏi kho!")
            return
    print("--> LỖI: Không tìm thấy mã sản phẩm này!")

# 6. Tìm kiếm sản phẩm
def search_product_by_name(products):
    """Tìm kiếm không phân biệt hoa/thường."""
    keyword = input("Nhập từ khóa tên sản phẩm: ").lower()
    found = [p for p in products if keyword in p["Tên"].lower()]
    if found:
        display_all_products(found)
    else:
        print("--> Không có sản phẩm nào khớp với từ khóa!")

# 7. Hiển thị danh sách
def display_all_products(products):
    """In danh sách dạng bảng."""
    if not products:
        print("--> Kho hàng hiện đang trống.")
        return
    
    print(f"\n{'ID':<6} | {'Tên sản phẩm':<25} | {'Hãng':<12} | {'Giá':<12} | {'SL':<5}")
    print("-" * 70)
    for p in products:
        print(f"{p['ID']:<6} | {p['Tên']:<25} | {p['Thương hiệu']:<12} | {p['Giá']:<12} | {p['Số lượng']:<5}")
    print("-" * 70)