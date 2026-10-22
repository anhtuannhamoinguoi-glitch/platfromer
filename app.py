"""SHADOWBOUND — Streamlit launcher. Game logic lives in game.html."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).resolve().parent
GAME_FILE = BASE_DIR / "game.html"
GAME_HEIGHT = 820

st.set_page_config(
    page_title="Shadowbound: Sinh Tồn Trong Bóng Tối",
    page_icon="🌑",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Rajdhani:wght@500;600;700&display=swap');
    .stApp { background: radial-gradient(ellipse at 50% -15%, #20252b 0%, #0d1115 48%, #050708 100%); color: #ddd8c9; }
    h1 { color: #e6dfcc !important; letter-spacing: 5px; text-shadow: 0 2px #554b3a, 0 0 24px #b89b6540; font-family: 'Cinzel', serif !important; font-weight: 800 !important; }
    h2, h3 { color: #d8d0bd !important; font-family: 'Cinzel', serif !important; }
    [data-testid="stMarkdownContainer"] p { color: #bdb8aa; }
    [data-testid="stCaptionContainer"] { color: #8f918d; }
    div[data-testid="stVerticalBlock"] > div:has(iframe) { border: 1px solid #494438; border-radius: 4px; box-shadow: 0 0 0 1px #080a0b, 0 18px 48px #000b; overflow: hidden; }
    hr { border-color: #39362e !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("SHADOWBOUND")
st.caption("A DARK SOULSLIKE JOURNEY  ·  3 VÙNG ĐẤT  ·  1 KẺ CANH GIỮ HƯ VÔ")
st.markdown(
    "**Điều khiển** — A/D hoặc ←/→: di chuyển · Space/W/↑: nhảy · J: tấn công · M: âm thanh · R: hồi sinh tại checkpoint sau khi thất bại. Có nút cảm ứng trên điện thoại."
)

if not GAME_FILE.is_file():
    st.error("Không tìm thấy game.html. Hãy đặt app.py và game.html trong cùng thư mục repository.")
    st.stop()

with GAME_FILE.open("r", encoding="utf-8") as game_file:
    game_html = game_file.read()

components.html(game_html, height=GAME_HEIGHT, scrolling=False)

st.markdown("---")
st.subheader("🕹️ Shadowbound — Bản nâng cấp đồ họa")
st.markdown(
    """
    - Vượt qua 3 khu vực: **Rừng Tàn**, **Hầm Ngục** và **Đấu Trường**.
    - Thu thập linh hồn, tránh hố, gai, đá lăn và bẫy phun lửa.
    - Đánh bại boss ở màn cuối để chiến thắng.
    - Có checkpoint, lưu/tải tiến trình, cửa hàng, cheat `/67` và điều khiển cảm ứng.
    - Đồ họa pixel art Canvas; nhạc nền và hiệu ứng âm thanh được nhúng trong `game.html`.
    - Dữ liệu lưu trong trình duyệt trên thiết bị hiện tại, chưa đồng bộ giữa nhiều máy.
    """
)
