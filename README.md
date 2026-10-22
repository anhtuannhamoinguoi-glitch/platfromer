# SHADOWBOUND — Bản mã nguồn cải thiện

Game platformer Dark Fantasy dùng **Python + Streamlit + HTML/CSS/JavaScript Canvas**.

## Cấu trúc

```text
SHADOWBOUND/
├── app.py
├── game.html
├── requirements.txt
└── README.md
```

## Chạy trên máy tính

1. Cài Python 3.10 trở lên.
2. Mở Terminal/CMD trong thư mục dự án.
3. Cài thư viện:

   ```bash
   pip install -r requirements.txt
   ```

4. Chạy:

   ```bash
   streamlit run app.py
   ```

## Đưa lên GitHub và Streamlit Cloud

1. Tải cả bốn file lên thư mục gốc của repository GitHub.
2. Commit changes.
3. Mở https://share.streamlit.io/ và chọn **Create app**.
4. Chọn repository, nhánh `main`, file chính `app.py`.
5. Nhấn **Deploy**.

`app.py` và `game.html` phải nằm cùng thư mục. Không tải riêng `app.py`, vì phần game được đọc từ `game.html`.

## Điều khiển

- `A` / `D` hoặc `←` / `→`: di chuyển.
- `Space`, `W` hoặc `↑`: nhảy.
- `J`: tấn công.
- `M`: bật/tắt âm thanh.
- `R`: chơi lại / hồi sinh theo trạng thái game.
- Nhập `/67`: bật chế độ bất tử và vô hạn linh hồn.
- Trên điện thoại: dùng nút cảm ứng; nên xoay ngang màn hình.

## Các phần được cải thiện

- Tăng chiều cao vùng nhúng và bật cuộn để giảm nguy cơ cắt mất nút lưu/tải ở cuối game.
- Kiểm tra `game.html` tồn tại, đọc được và có cấu trúc game cơ bản trước khi nhúng.
- Bổ sung metadata trang và CSS cho màn hình hẹp.
- Giữ nguyên các cơ chế gameplay hiện có trong `game.html`.

## Lưu ý

Checkpoint, ô lưu và kỷ lục nằm trong bộ nhớ trình duyệt trên thiết bị hiện tại; chưa đồng bộ giữa các thiết bị. Cần kiểm thử gameplay thực tế sau khi triển khai.
