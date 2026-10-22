from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SHADOWBOUND", page_icon="🌑", layout="wide")
st.markdown("""<style>.stApp{background:#080b0e;color:#ddd8c9}h1{letter-spacing:5px;color:#e6dfcc}iframe{border:1px solid #494438;border-radius:5px}</style>""", unsafe_allow_html=True)
st.title("SHADOWBOUND")
st.caption("DARK FANTASY PLATFORMER · 3 VÙNG ĐẤT · 1 KẺ CANH GIỮ HƯ VÔ")
st.markdown("**Điều khiển:** A/D hoặc ←/→ di chuyển · Space/W/↑ nhảy · J tấn công · M âm thanh · R chơi lại. Điện thoại có nút cảm ứng.")

file = Path(__file__).with_name("game.html")
if not file.is_file():
    st.error("Thiếu game.html. Hãy tải app.py và game.html lên cùng thư mục GitHub.")
    st.stop()
try:
    html = file.read_text(encoding="utf-8")
except OSError as error:
    st.error(f"Không đọc được game.html: {error}")
    st.stop()
if "<canvas" not in html or "<script" not in html:
    st.error("game.html không đầy đủ hoặc không hợp lệ.")
    st.stop()
components.html(html, height=1080, scrolling=True)
st.caption("Mẹo: xoay ngang điện thoại để có vùng chơi rộng hơn. Tiến trình lưu trên trình duyệt của thiết bị hiện tại.")
