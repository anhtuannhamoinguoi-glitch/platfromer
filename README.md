# SHADOWBOUND — Dark Fantasy Audio Edition

Game platformer Canvas/JavaScript chạy trong Streamlit, có nhạc nền Dark Fantasy dạng vòng lặp và các hiệu ứng WAV: kiếm chém, nhặt xu, nhảy, nhận sát thương, hồi máu, bẫy va chạm, boss, checkpoint, chiến thắng và game over.

## Chạy trên máy
1. Cài Python 3.10+.
2. `pip install -r requirements.txt`
3. `streamlit run app.py`

## Đưa lên GitHub / Streamlit Community Cloud
Tải lên `app.py`, `requirements.txt` và toàn bộ thư mục `assets/sounds/`. Đặt `app.py` ở thư mục gốc repository.

## Điều khiển âm thanh
Bấm **BẮT ĐẦU HÀNH TRÌNH** để cho phép trình duyệt phát âm thanh. Nút **♪ ĐANG BẬT/TẮT** hoặc phím **M** để tắt/bật; thanh Âm lượng chỉnh nhạc và hiệu ứng cùng lúc.

Âm thanh WAV được nhúng dạng Base64 vào HTML lúc Streamlit khởi tạo để trình duyệt không phải truy cập đường dẫn file cục bộ. Nếu thiếu file asset, game vẫn chạy và các tiếng tổng hợp Web Audio hiện có vẫn là phương án dự phòng.
