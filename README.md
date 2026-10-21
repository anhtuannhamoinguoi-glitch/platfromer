# SHADOWBOUND — bản nâng cấp Streamlit

## Chạy trên Windows
1. Cài Python 3.10 trở lên.
2. Đặt `app.py` và `requirements.txt` trong cùng một thư mục.
3. Mở CMD/PowerShell tại thư mục đó và chạy:
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   streamlit run app.py
   ```
4. Trình duyệt sẽ mở game. Nếu không tự mở, truy cập `http://localhost:8501`.

## Điều khiển
- Máy tính: A/D hoặc phím mũi tên để di chuyển; Space/W/↑ để nhảy; J để đánh; M bật/tắt âm thanh; R hồi sinh tại checkpoint sau khi chết. Sau khi chiến thắng, R bắt đầu lại từ đầu.
- Điện thoại/tablet: dùng các nút cảm ứng bên dưới màn chơi. Chạm một lần vào game để trình duyệt cho phép âm thanh phát.
- Mật mã bí mật hiện có: gõ `/67` để bật/tắt bất tử và vô hạn xu.

## Tính năng mới
- Checkpoint tại các điểm mốc ở từng màn, tự lưu trong `localStorage`; nút tiếp tục từ checkpoint ở menu.
- Boss bắn đạn linh hồn và tăng nhịp tấn công khi còn dưới nửa máu.
- Nút điều khiển cảm ứng, viewport cho màn hình nhỏ.
- Lưu thủ công từng màn được bổ sung dữ liệu checkpoint và kiểm tra dữ liệu trước khi tải.
- Đồ họa và âm thanh vẫn được tạo bằng Canvas/Web Audio, không cần tải thêm ảnh hoặc tệp âm thanh ngoài.

## Lưu ý
- Tiến trình được lưu trong trình duyệt trên thiết bị hiện tại; xóa dữ liệu trang web hoặc đổi trình duyệt có thể làm mất save.
- Vì game chạy trong iframe của Streamlit, khi triển khai trực tuyến cần đảm bảo trình duyệt cho phép `localStorage` trong iframe. Chạy local trên `localhost` thường là cách kiểm tra dễ nhất.
- Nếu sửa CSS/JS trong `app.py`, hãy lưu file rồi tải lại trang.
