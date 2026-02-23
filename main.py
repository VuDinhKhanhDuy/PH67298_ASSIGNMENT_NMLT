
import quanlisanpham as pm

def main():
    # Tải dữ liệu ngay khi chương trình bắt đầu
    danh_sach_sp = pm.load_data()
    
    # Vòng lặp hiển thị menu chính
    while True:
        print("\n" + "="*40)
        print("   QUẢN LÝ KHO LAPTOP POLYLAP")
        print("="*40)
        print("1. Thêm sản phẩm mới")
        print("2. Cập nhật thông tin sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Tìm kiếm sản phẩm theo tên")
        print("5. Hiển thị toàn bộ sản phẩm")
        print("0. Thoát và Lưu dữ liệu")
        print("="*40)
        
        lua_chon = input("Vui lòng chọn chức năng (0-5): ")
        
        if lua_chon == '1':
            danh_sach_sp = pm.add_product(danh_sach_sp)
        elif lua_chon == '2':
            pm.update_product(danh_sach_sp)
        elif lua_chon == '3':
            pm.delete_product(danh_sach_sp)
        elif lua_chon == '4':
            pm.search_product_by_name(danh_sach_sp)
        elif lua_chon == '5':
            pm.display_all_products(danh_sach_sp)
        elif lua_chon == '0':
            # Gọi hàm lưu dữ liệu trước khi kết thúc
            pm.save_data(danh_sach_sp)
            print("Dữ liệu đã được lưu. Tạm biệt!")
            break # Thoát vòng lặp while
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 0 đến 5!")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()