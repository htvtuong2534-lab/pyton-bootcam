import os
from .io_untils import load_tasks

def main():
    # Đường dẫn tới file CSV mẫu (giả sử bạn để file mẫu tên là tasks.csv trong thư mục w2)
    sample_csv_path = os.path.join(os.path.dirname(__file__), "tasks.csv")
    
    print(f"Đang đọc dữ liệu từ: {sample_csv_path}")
    try:
        # Gọi hàm load_tasks đã viết ở phần W2-2
        tasks = load_tasks(sample_csv_path)
        print("\n--- DANH SÁCH TASKS ĐÃ TẢI THÀNH CÔNG ---")
        for t in tasks:
            print(t)
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

if __name__ == "__main__":
    main()