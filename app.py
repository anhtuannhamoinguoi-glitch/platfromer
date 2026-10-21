import streamlit as st
import streamlit.components.v1 as components

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
    """
    **Điều khiển** — A/D hoặc ←/→: di chuyển · Space/W/↑: nhảy · J: tấn công · M: âm thanh · R: hồi sinh tại checkpoint sau khi thất bại. Có nút cảm ứng trên điện thoại.
    """
)

game_html = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
*{box-sizing:border-box}
html,body{margin:0;background:#080a0b;color:#d8d2c3;font-family:Georgia,'Courier New',monospace}
.wrap{width:100%;max-width:1000px;margin:auto;padding:9px;background:linear-gradient(145deg,#171923,#080a10 45%,#15101d);border:1px solid #756044;border-radius:7px;box-shadow:0 0 0 1px #030404,0 0 26px #9b5de522,inset 0 0 28px #c2a56a12}
.hud{display:grid;grid-template-columns:minmax(210px,1.5fr) minmax(100px,.7fr) minmax(120px,.8fr);gap:8px;align-items:center;padding:8px 4px 10px;color:#d8d2c3;font-size:12px;letter-spacing:.5px}
.status{display:flex;flex-direction:column;gap:5px;min-width:0}.label{font-size:10px;letter-spacing:2px;color:#999487;text-transform:uppercase}.bar{height:12px;background:#211b19;border:1px solid #5b493a;padding:2px;box-shadow:inset 0 1px 3px #000}.bar-fill{height:100%;width:100%;background:linear-gradient(90deg,#6d171b,#a42b2b 65%,#d14b3d);transition:width .12s linear}.subbar{height:5px;background:#171d21;border:1px solid #3b4649;padding:1px}.subfill{height:100%;width:100%;background:#657f91;transition:width .12s linear}.stat{border-left:1px solid #4a4438;padding:4px 10px;min-height:34px}.stat b{display:block;color:#e2d9c4;font-size:15px;font-weight:normal;letter-spacing:1px}.stat small{display:block;color:#8e8a7e;font-size:9px;letter-spacing:1.5px;margin-bottom:3px}.right-stats{display:flex;justify-content:flex-end;gap:12px}.stat em{font-style:normal;color:#c7a96b}
.stage{position:relative;border:1px solid #817052;background:#050708;line-height:0;overflow:hidden;box-shadow:inset 0 0 34px #000,0 0 24px #7c3aed18}canvas{display:block;width:100%;height:auto;background:#101319;image-rendering:pixelated;outline:none;filter:saturate(1.12) contrast(1.04);}
.hint{font-size:10px;line-height:1.7;color:#8d8a80;padding:9px 4px 2px;text-align:center;letter-spacing:.4px;border-top:1px solid #292821;margin-top:5px}
.menu{position:absolute;inset:0;z-index:3;display:flex;align-items:center;justify-content:center;background:linear-gradient(90deg,rgba(4,6,7,.92),rgba(5,7,8,.56) 58%,rgba(4,6,7,.2));line-height:1.4}.menu-card{width:54%;padding:22px 24px;border-left:2px solid #a58a55;background:linear-gradient(90deg,rgba(9,11,12,.92),rgba(9,11,12,.45));text-shadow:0 2px #000}.eyebrow{font-size:9px;letter-spacing:4px;color:#b59a65;margin-bottom:10px}.menu-title{font:700 clamp(22px,4vw,42px) Georgia,serif;letter-spacing:3px;color:#e4ddca;text-shadow:0 3px #342b20,0 0 18px #c3a26733}.menu-sub{font-size:10px;letter-spacing:2px;color:#9a978b;margin:8px 0 20px}.rule{height:1px;background:linear-gradient(90deg,#a58a55,transparent);margin:15px 0}.start-btn{display:block;width:100%;padding:12px 15px;background:#8e2527;border:1px solid #d0a66b;color:#f4e8cd;font:700 12px Georgia,serif;letter-spacing:3px;cursor:pointer;box-shadow:0 3px 0 #351516;transition:background .15s,transform .15s}.start-btn:hover{background:#aa3031;transform:translateY(-1px)}.difficulty{display:flex;gap:6px;margin:14px 0 4px}.diff-btn{flex:1;padding:9px 4px;background:#17191b;border:1px solid #514838;color:#bdb8aa;font:600 10px Georgia,serif;letter-spacing:1px;cursor:pointer}.diff-btn.active{background:#3a2823;border-color:#c7a96b;color:#f4e8cd;box-shadow:inset 0 -2px #a33b36}.diff-desc{font-size:9px;color:#999487;min-height:14px;margin-top:6px}.menu-note{font-size:10px;color:#a09a8b;margin-top:13px;letter-spacing:.5px}.corner{position:absolute;right:14px;bottom:12px;color:#b8a779;font-size:9px;letter-spacing:2px;opacity:.85}
.save-panel{padding:10px 8px;margin-top:9px;border:1px solid #494438;background:linear-gradient(120deg,#10131a,#17121c);color:#cfc5ad;font-size:11px;line-height:1.4}.save-title{font-size:11px;letter-spacing:2px;color:#e3c47f;margin-bottom:8px}.save-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}.save-slot{padding:8px;border:1px solid #514838;background:#0b0e12;text-align:center}.save-slot b{display:block;color:#e3d8c2;font-size:11px;margin-bottom:5px}.save-status{display:block;min-height:26px;color:#8e9b9d;font-size:9px;margin:5px 0}.save-actions{display:flex;gap:5px}.save-btn{flex:1;padding:7px 4px;border:1px solid #76613d;background:#252019;color:#e9d9b8;font:600 9px Georgia,serif;cursor:pointer;letter-spacing:.4px}.save-btn:hover:not(:disabled){background:#483222}.save-btn:disabled{opacity:.35;cursor:not-allowed}.save-note{color:#8f918d;font-size:9px;margin-top:8px}@media(max-width:600px){.save-grid{grid-template-columns:1fr}.save-slot{display:grid;grid-template-columns:1fr;}.save-status{min-height:0}}
.mobile-controls{display:none;grid-template-columns:repeat(4,minmax(0,1fr));gap:7px;padding:8px 0 2px;touch-action:none}.touch-btn{min-height:45px;border:1px solid #76613d;background:linear-gradient(145deg,#292333,#11131a);color:#f0dfbd;font:700 12px Georgia,serif;letter-spacing:1px;border-radius:5px;touch-action:none;user-select:none;-webkit-user-select:none}.touch-btn:active,.touch-btn.pressed{background:#68402e;border-color:#e7bd75;transform:translateY(1px)}@media(max-width:760px),(pointer:coarse){.mobile-controls{display:grid}.wrap{padding:5px}.hud{font-size:11px}.stage{touch-action:pan-y}.hint{font-size:9px}}
.shop-item{padding:11px 8px;background:linear-gradient(160deg,#211b2c,#100f19);border:1px solid #65503c;box-shadow:inset 0 0 18px #a855f711;text-align:center;line-height:1.45;display:flex;flex-direction:column;align-items:center;gap:7px}.shop-item b{font-size:11px;letter-spacing:.5px;color:#f0dfbd}.shop-item p{font-size:10px;color:#aaa2b7;min-height:30px;margin:0}.shop-item small{font-size:10px;color:#e5bd70}.shop-icon{font-size:28px;color:#e6c47e;text-shadow:0 0 14px #e6c47e66}.buy-btn{padding:9px 6px;margin-top:auto;font-size:10px;letter-spacing:1px}.buy-btn:disabled{opacity:.38;cursor:not-allowed;filter:grayscale(1)}
@media(max-width:600px){.hud{grid-template-columns:1fr 1fr}.right-stats{justify-content:flex-start}.menu-card{width:76%;padding:12px}.menu-sub{margin-bottom:10px}.menu-note{display:none}.shop-grid{grid-template-columns:1fr!important;max-height:320px;overflow:auto}.shop-item{display:grid;grid-template-columns:32px 1fr;align-items:center;text-align:left}.shop-item p,.shop-item small,.shop-item button{grid-column:2}.shop-item p{min-height:0}}
</style>
</head>
<body>
<div class="wrap">
  <div class="hud">
    <div class="status"><span class="label">Sinh mệnh · <span id="hptext">3 / 3</span></span><div class="bar"><div class="bar-fill" id="healthbar"></div></div><div class="subbar"><div class="subfill" id="staminabar"></div></div></div>
    <div class="stat"><small>KHU VỰC</small><b id="level">I · Rừng Tàn</b></div>
    <div class="right-stats"><div class="stat"><small>LINH HỒN</small><b><em id="coins">◈ 0</em></b></div><div class="stat"><small>KỶ LỤC</small><b id="best">0</b></div></div>
  </div>
  <div class="stage">
    <canvas id="game" width="960" height="540" tabindex="0" aria-label="Game Shadowbound"></canvas>
    <div class="menu" id="mainmenu"><div class="menu-card"><div class="eyebrow">THE LAST LIGHT IS FADING</div><div class="menu-title">SHADOWBOUND</div><div class="menu-sub">A SOULSLIKE PIXEL ADVENTURE</div><div class="rule"></div><div class="eyebrow">CHỌN ĐỘ KHÓ</div><div class="difficulty"><button class="diff-btn" data-diff="easy">DỄ</button><button class="diff-btn active" data-diff="normal">TRUNG BÌNH</button><button class="diff-btn" data-diff="hard">KHÓ</button></div><div class="diff-desc" id="diffdesc">Thử thách cân bằng, phù hợp để làm quen.</div><button class="start-btn" id="startbtn">BẮT ĐẦU HÀNH TRÌNH</button><button class="start-btn" id="resumebtn" style="margin-top:9px;background:#263c3c;">TIẾP TỤC TỪ CHECKPOINT</button><div class="menu-note">Ba vùng đất. Một lời nguyền. Không có đường quay lại.</div></div><div class="corner">WASD / ARROWS · SPACE · J</div></div>
    <div class="menu" id="shopmenu" style="display:none;background:rgba(4,5,12,.93);">
      <div class="menu-card" style="width:min(760px,94%);border-left-color:#e0b45f;background:linear-gradient(110deg,rgba(15,12,25,.98),rgba(25,16,35,.96));">
        <div class="eyebrow">THE FORGOTTEN MERCHANT</div>
        <div class="menu-title" style="font-size:clamp(22px,3vw,34px);">KẺ BUÔN LINH HỒN</div>
        <div class="menu-sub">MUA VẬT PHẨM TRƯỚC KHI BƯỚC VÀO VÙNG ĐẤT TIẾP THEO</div>
        <div class="rule"></div>
        <div style="font-size:12px;color:#e8d6aa;margin-bottom:8px;">◈ LINH HỒN: <b id="shopcoins">0</b>　 ·　 ĐIỂM: <b id="shopscore">0</b></div>
        <div class="shop-grid" style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:14px 0;">
          <div class="shop-item"><div class="shop-icon">✚</div><b>THÊM SINH MỆNH</b><p>+1 máu tối đa, hồi thêm 1 máu.</p><small id="hpprice">Giá: 25 linh hồn</small><button class="start-btn buy-btn" data-item="hp">MUA</button></div>
          <div class="shop-item"><div class="shop-icon">⚔</div><b>LƯỠI KIẾM CƯỜNG HÓA</b><p>Đòn đánh gây thêm sát thương lên boss.</p><small id="dmgprice">Giá: 35 linh hồn</small><button class="start-btn buy-btn" data-item="damage">MUA</button></div>
          <div class="shop-item"><div class="shop-icon">➤</div><b>BƯỚC CHÂN BÓNG TỐI</b><p>Tăng tốc độ di chuyển.</p><small id="spdprice">Giá: 20 linh hồn</small><button class="start-btn buy-btn" data-item="speed">MUA</button></div>
        </div>
        <div id="shopmessage" style="min-height:18px;font-size:11px;color:#e9c979;margin:8px 0;">Chọn vật phẩm để chuẩn bị cho chặng tiếp theo.</div>
        <button class="start-btn" id="continuebtn">TIẾP TỤC HÀNH TRÌNH →</button>
        <div class="menu-note">Vật phẩm đã mua được giữ trong suốt lượt chơi hiện tại.</div>
      </div>
    </div>
  </div>
  <div class="mobile-controls" aria-label="Điều khiển cảm ứng">
    <button class="touch-btn" data-touch="ArrowLeft" aria-label="Đi trái">◀</button>
    <button class="touch-btn" data-touch="ArrowRight" aria-label="Đi phải">▶</button>
    <button class="touch-btn jump-btn" data-touch=" " aria-label="Nhảy">NHẢY</button>
    <button class="touch-btn attack-btn" data-touch="j" aria-label="Tấn công">⚔ ĐÁNH</button>
  </div>
  <div class="save-panel">
    <div class="save-title">✦ LƯU / TẢI TIẾN TRÌNH TỪNG MÀN ✦</div>
    <div class="save-grid">
      <div class="save-slot"><b>I · RỪNG TÀN</b><span class="save-status" id="save-status-0">Chưa có dữ liệu lưu</span><div class="save-actions"><button class="save-btn" data-save="0">LƯU MÀN I</button><button class="save-btn" data-load="0">TẢI MÀN I</button></div></div>
      <div class="save-slot"><b>II · HẦM NGỤC</b><span class="save-status" id="save-status-1">Chưa có dữ liệu lưu</span><div class="save-actions"><button class="save-btn" data-save="1">LƯU MÀN II</button><button class="save-btn" data-load="1">TẢI MÀN II</button></div></div>
      <div class="save-slot"><b>III · ĐẤU TRƯỜNG</b><span class="save-status" id="save-status-2">Chưa có dữ liệu lưu</span><div class="save-actions"><button class="save-btn" data-save="2">LƯU MÀN III</button><button class="save-btn" data-load="2">TẢI MÀN III</button></div></div>
    </div>
    <div class="save-note" id="save-message">Mỗi màn có một ô lưu riêng; checkpoint tự lưu khi kích hoạt. Dữ liệu nằm trong trình duyệt trên thiết bị hiện tại.</div>
  </div>
  <div class="hint">A/D hoặc ←/→ DI CHUYỂN &nbsp; · &nbsp; SPACE NHẢY &nbsp; · &nbsp; J TẤN CÔNG &nbsp; · &nbsp; M ÂM THANH &nbsp; · &nbsp; R CHƠI LẠI &nbsp; · &nbsp; ĐÁ KHỔNG LỒ RƠI TỪ TRÊN XUỐNG (NGHỈ LÂU) / LỬA</div>
</div>
<script>
(() => {
"use strict";
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
ctx.imageSmoothingEnabled = false;
const W = canvas.width, H = canvas.height;
const keys = {};
let audioOn = true, audioCtx = null, lastTime = 0, gameOver = false, victory = false, started = false;
let difficulty = "normal";
const difficultySettings = {easy:{hp:5,enemy:0.78,trap:0.78,pause:1.45,desc:"Nhiều máu hơn, quái và bẫy chậm hơn."},normal:{hp:3,enemy:1,trap:1,pause:1,desc:"Thử thách cân bằng, phù hợp để làm quen."},hard:{hp:2,enemy:1.32,trap:1.28,pause:0.68,desc:"Ít máu, quái nhanh; lửa phun ở nhiều độ cao khác nhau."}};
let score = 0, coins = 0, levelIndex = 0, attackTimer = 0, invuln = 0, shake = 0;
let shopOpen = false, shopMessage = "";
let godMode = false, cheatBuffer = "";
const INFINITE_COINS = 999999999;
const AUTO_CHECKPOINT_KEY = "shadowbound_checkpoint_v2";
let activeCheckpoint = {x:70, y:350, label:"Khởi đầu"};
let checkpointNotice = 0;
let bossProjectiles = [];
let shopUpgrades = {hp:0, damage:0, speed:0};
let best = 0;
try { best = Number(localStorage.getItem("shadowbound_best") || 0); } catch(e) {}
const bestEl = document.getElementById("best");
bestEl.textContent = String(best);

const levels = [
 {name:"Rừng Tàn", length:2300, start:70, goal:2180, ground:430, checkpoints:[{x:700,y:370,label:"Bệ đá cổ"},{x:1510,y:300,label:"Tượng Vệ Thần"}],
  platforms:[[250,360,120],[470,310,120],[710,370,140],[960,320,120],[1210,360,140],[1490,300,130],[1770,350,130]],
  pits:[[390,455],[630,690],[880,930],[1110,1160],[1390,1440],[1660,1710],[1950,2010]],
  coinSpots:[[180,380],[290,315],[520,265],[760,325],[1010,275],[1260,315],[1540,255],[1810,305],[2050,385]],
  enemies:[330,780,1040,1570,1870],
  traps:[{type:"boulder",x:500,start:470,end:820,damage:1.2,size:104,speed:245,pause:4.8,rollTime:2.8},{type:"fire",x:1015,damage:0.65,period:3.2,active:1.15},{type:"fire",x:1760,damage:0.65,period:2.8,active:1.0}], boss:false},
 {name:"Hầm Ngục", length:2600, start:70, goal:2470, ground:430, checkpoints:[{x:1165,y:340,label:"Bàn thờ tro"},{x:1945,y:280,label:"Ấn phong ấn"}],
  platforms:[[210,350,120],[430,300,130],[680,350,120],[900,285,130],[1160,340,140],[1430,290,130],[1680,350,130],[1940,280,130],[2190,340,120]],
  pits:[[360,410],[620,670],[850,890],[1100,1150],[1390,1420],[1640,1670],[1900,1930],[2150,2180]],
  coinSpots:[[150,380],[250,305],[470,255],[720,305],[950,240],[1200,295],[1480,245],[1730,305],[1990,235],[2250,295]],
  enemies:[300,740,1020,1510,1810,2250],
  traps:[{type:"boulder",x:690,start:650,end:1010,damage:1.3,size:112,speed:260,pause:5.2,rollTime:3.0},{type:"fire",x:1210,damage:0.7,period:2.7,active:1.15},{type:"boulder",x:1690,start:1650,end:2010,damage:1.3,size:112,speed:260,pause:5.2,rollTime:3.0}], boss:false},
 {name:"Đấu Trường", length:1800, start:70, goal:1680, ground:430, checkpoints:[{x:800,y:350,label:"Cổng đấu trường"}],
  platforms:[[280,350,130],[540,300,130],[800,350,140],[1080,300,130],[1350,350,130]],
  pits:[[430,480],[700,750],[970,1020],[1240,1290]],
  coinSpots:[[180,380],[330,305],[590,255],[850,305],[1130,255],[1400,305],[1580,385]],
  enemies:[350,880],
  traps:[{type:"fire",x:620,damage:0.75,period:2.5,active:1.1},{type:"boulder",x:990,start:950,end:1290,damage:1.35,size:120,speed:275,pause:5.5,rollTime:3.2},
   {type:"laser",x:600,y:235,damage:0.95,period:2.8,active:1.55,bouncy:true,radius:42,vx:340,vy:230,points:[[600,235],[760,235]]}], boss:true}
];
let world, player, enemies, coinsList, particles, boss, traps;
let enemyArrows = [];

function makeWorld(index) {
 const d = levels[index];
 world = d;
 player = {x:d.start,y:350,w:24,h:34,vx:0,vy:0,grounded:false,face:1,hp:difficultySettings[difficulty].hp,maxHp:difficultySettings[difficulty].hp,anim:0};
 enemies = d.enemies.map((x,i)=>{
  // Alternate enemy roles across each level so both new archetypes appear in every region.
  const type=(i%2===0)?"archer":"tanker";
  return {type,x,y:390,w:type==="tanker"?34:26,h:type==="tanker"?38:30,
   vx:(i%2?1:-1)*(type==="tanker"?42:48)*difficultySettings[difficulty].enemy,
   vy:0,grounded:false,alive:true,home:x,range:type==="tanker"?110:95,hp:type==="tanker"?3:2,
   maxHp:type==="tanker"?3:2,shotCooldown:1.1+Math.random()*1.2,flash:0,
   jumpCooldown:.7+Math.random(),chargeCooldown:1.3+Math.random(),charging:0};
 });
 enemyArrows = [];
 coinsList = d.coinSpots.map(([x,y])=>({x,y,r:8,taken:false}));
 particles = [];
 bossProjectiles = [];
 enemyArrows = [];
 activeCheckpoint = {x:d.start, y:350, label:"Khởi đầu"};
 checkpointNotice = 0;
 traps = (d.traps || []).filter(t=>t.type!=="laser" || index===2).map((t,i)=>({...t,damage:t.damage*(difficulty==="easy"?0.78:difficulty==="hard"?1.2:1),period:t.period? t.period/difficultySettings[difficulty].trap:t.period,active:t.active,dropSpeed:(t.dropSpeed||620)*difficultySettings[difficulty].trap,baseX:t.x,dir:i%2===0?1:-1,phase:Math.random()*(t.period||2),rolling:false,state:"rest",y:t.type==="laser"?t.y:-(t.size||108)-10,flameHeight:t.type==="fire"?(difficulty==="hard"?[48,72,98,126][Math.floor(Math.random()*4)]:difficulty==="easy"?58:78):78,pauseTimer:(t.type==="boulder"?(t.pause||6)*difficultySettings[difficulty].pause*(0.8+Math.random()*0.35):0),rollTimer:0,hitCooldown:0,impactTimer:0,laserPhase:Math.random()*(t.period||2),laserOn:false,laserVx:t.vx||0,laserVy:t.vy||0}));
 boss = d.boss ? {x:1320,y:350,w:62,h:76,hp:8,maxHp:8,vx:70,alive:true,flash:0,attack:0} : null;
 gameOver = false; victory = false; attackTimer = 0; invuln = 0; shake = 0;
}
makeWorld(0);

function beep(freq=440,duration=.08,type="square",volume=.035) {
 if(!audioOn) return;
 try {
  audioCtx = audioCtx || new (window.AudioContext || window.webkitAudioContext)();
  if(audioCtx.state==="suspended") audioCtx.resume();
  const o=audioCtx.createOscillator(), g=audioCtx.createGain();
  o.type=type; o.frequency.value=freq; g.gain.value=volume;
  g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+duration);
  o.connect(g); g.connect(audioCtx.destination); o.start(); o.stop(audioCtx.currentTime+duration);
 } catch(e) {}
}
function noiseHit(){beep(110,.12,"sawtooth",.06)}
function addParticles(x,y,color,n=8){
 for(let i=0;i<n;i++) particles.push({x,y,vx:(Math.random()-.5)*180,vy:-Math.random()*150-20,life:.45,color});
}
function rect(x,y,w,h,color){ctx.fillStyle=color;ctx.fillRect(Math.round(x),Math.round(y),Math.round(w),Math.round(h));}
function text(str,x,y,size=16,color="#eef3fa",align="left"){
 ctx.fillStyle=color;ctx.font=`bold ${size}px monospace`;ctx.textAlign=align;ctx.fillText(str,x,y);
}
function hit(a,b){return a.x < b.x+b.w && a.x+a.w > b.x && a.y < b.y+b.h && a.y+a.h > b.y;}
function pitAt(x){return world.pits.some(p=>x+player.w>p[0] && x<p[1]);}
function floorAt(x){
 if(pitAt(x)) return H+100;
 return world.ground;
}
function platforms(){return world.platforms.map(p=>({x:p[0],y:p[1],w:p[2],h:16}));}
function damage(amount=1){
 if(godMode){player.hp=player.maxHp;invuln=.15;return;}
 if(invuln>0 || gameOver || victory) return;
 player.hp=Math.max(0,player.hp-amount); invuln=1.25; shake=.25; noiseHit(); addParticles(player.x+12,player.y+15,"#ff657a",12);
 if(player.hp<=0){gameOver=true; beep(90,.5,"sawtooth",.06);}
}
function attack(){
 if(!started || attackTimer>0 || gameOver || victory) return;
 attackTimer=.22; beep(240,.07,"square",.04);
 const range={x:player.face>0?player.x+player.w:player.x-28,y:player.y+5,w:30+shopUpgrades.damage*4,h:25};
 enemies.forEach(e=>{if(e.alive && hit(range,e)){e.alive=false;score+=100;addParticles(e.x+13,e.y+12,"#a9c6d9",12);beep(620,.09);}});
 if(boss && boss.alive && hit(range,boss)){boss.hp-=1+shopUpgrades.damage;boss.flash=.18;score+=25;addParticles(boss.x+boss.w/2,boss.y+25,"#fca5a5",8);beep(170,.08,"sawtooth",.05);if(boss.hp<=0){boss.alive=false;score+=1000;addParticles(boss.x+30,boss.y+30,"#e879f9",30);}}
}
function resetGame(){score=0;coins=0;levelIndex=0;shopOpen=false;shopUpgrades={hp:0,damage:0,speed:0};document.getElementById("shopmenu").style.display="none";makeWorld(0);beep(500,.08);}
function nextLevel(){
 if(levelIndex<levels.length-1){
  levelIndex++;shopOpen=true;
  document.getElementById("shopmenu").style.display="flex";
  updateShopUI();beep(700,.1);setTimeout(()=>beep(900,.1),110);
 } else {victory=true;score+=500;saveBest();}
}
function shopCost(item){
 const base={hp:25,damage:35,speed:20}[item];
 const step={hp:20,damage:25,speed:15}[item];
 return base+shopUpgrades[item]*step;
}
function updateShopUI(){
 document.getElementById("shopcoins").textContent=godMode?"∞ (VÔ HẠN)":coins;
 document.getElementById("shopscore").textContent=score;
 document.getElementById("hpprice").textContent="Giá: "+shopCost("hp")+" linh hồn";
 document.getElementById("dmgprice").textContent="Giá: "+shopCost("damage")+" linh hồn";
 document.getElementById("spdprice").textContent="Giá: "+shopCost("speed")+" linh hồn";
 document.querySelectorAll(".buy-btn").forEach(btn=>{
  const cost=shopCost(btn.dataset.item);
  btn.disabled=!godMode && coins<cost;
  btn.textContent=godMode?"MUA MIỄN PHÍ · ∞ ◈":(coins<cost?"CHƯA ĐỦ XU":"MUA · "+cost+" ◈");
 });
 document.getElementById("shopmessage").textContent=shopMessage||"Chọn vật phẩm để chuẩn bị cho chặng tiếp theo.";
}
function buyItem(item){
 const cost=shopCost(item);
 if(!godMode && coins<cost){shopMessage="Bạn chưa có đủ linh hồn để mua vật phẩm này.";beep(110,.1,"square");updateShopUI();return;}
 if(!godMode) coins-=cost; else coins=INFINITE_COINS;
 shopUpgrades[item]++;
 if(item==="hp"){player.maxHp++;player.hp=Math.min(player.maxHp,player.hp+1);}
 shopMessage=({hp:"Sinh mệnh được tăng cường!",damage:"Lưỡi kiếm phát sáng mạnh hơn!",speed:"Bước chân bóng tối đã được nâng cấp!"})[item];
 beep(740,.1,"triangle");updateShopUI();
}
function saveBest(){
 best=Math.max(best,score);
 try{localStorage.setItem("shadowbound_best",String(best));}catch(e){}
 bestEl.textContent=String(best);
}
function persistCheckpoint(){
 try{
  localStorage.setItem(AUTO_CHECKPOINT_KEY,JSON.stringify({version:2,savedAt:Date.now(),levelIndex,x:activeCheckpoint.x,y:activeCheckpoint.y,label:activeCheckpoint.label,difficulty,score,coins:godMode?0:coins,shopUpgrades}));
 }catch(e){}
}
function activateCheckpoint(cp){
 activeCheckpoint={x:cp.x,y:cp.y-34,label:cp.label||"Checkpoint"};
 checkpointNotice=2.1;
 persistCheckpoint();
 beep(660,.1,"triangle",.04);setTimeout(()=>beep(880,.12,"triangle",.035),90);
 document.getElementById("save-message").textContent="Checkpoint đã kích hoạt: "+activeCheckpoint.label+". Tiến trình được tự động lưu trên thiết bị này.";
}
function resumeCheckpoint(){
 let data=null;
 try{data=JSON.parse(localStorage.getItem(AUTO_CHECKPOINT_KEY)||"null");}catch(e){}
 if(!data || !Number.isInteger(data.levelIndex) || data.levelIndex<0 || data.levelIndex>=levels.length){
  document.getElementById("save-message").textContent="Chưa có checkpoint tự động hợp lệ. Hãy bắt đầu hành trình mới.";return;
 }
 difficulty=difficultySettings[data.difficulty]?data.difficulty:"normal";
 document.querySelectorAll(".diff-btn").forEach(btn=>btn.classList.toggle("active",btn.dataset.diff===difficulty));
 document.getElementById("diffdesc").textContent=difficultySettings[difficulty].desc;
 levelIndex=data.levelIndex;makeWorld(levelIndex);
 activeCheckpoint={x:Number(data.x)||levels[levelIndex].start,y:Number(data.y)||350,label:data.label||"Checkpoint"};
 player.x=activeCheckpoint.x;player.y=activeCheckpoint.y;player.vy=0;player.grounded=false;
 score=Number(data.score)||0;coins=godMode?INFINITE_COINS:(Number(data.coins)||0);shopUpgrades={hp:0,damage:0,speed:0,...(data.shopUpgrades||{})};
 started=true;gameOver=false;victory=false;shopOpen=false;
 document.getElementById("mainmenu").style.display="none";document.getElementById("shopmenu").style.display="none";
 document.getElementById("save-message").textContent="Đã tiếp tục từ checkpoint: "+activeCheckpoint.label+".";canvas.focus();beep(560,.1,"triangle");
}
function retryFromCheckpoint(){
 gameOver=false;victory=false;player.hp=player.maxHp;player.x=activeCheckpoint.x;player.y=activeCheckpoint.y;player.vx=0;player.vy=0;player.grounded=false;invuln=2;attackTimer=0;
 enemies.forEach(e=>{if(!e.alive){e.alive=true;e.x=e.home;e.vx=Math.abs(e.vx)*(Math.random()<.5?-1:1);}});
 if(boss && !boss.alive){boss.alive=true;boss.hp=boss.maxHp;boss.x=1320;boss.vx=70;boss.attack=0;}
 bossProjectiles=[];enemyArrows=[];
 traps.forEach(t=>{t.hitCooldown=0;if(t.type==="boulder"){t.state="rest";t.y=-(t.size||112)-10;t.pauseTimer=Math.max(1,t.pause||5);} });
 persistCheckpoint();beep(520,.1,"triangle");canvas.focus();
}
const saveKey = index => "shadowbound_save_level_" + index;
function refreshSaveSlots(){
 for(let i=0;i<levels.length;i++){
  const status=document.getElementById("save-status-"+i);
  const loadBtn=document.querySelector('[data-load="'+i+'"]');
  let data=null;
  try{data=JSON.parse(localStorage.getItem(saveKey(i))||"null");}catch(e){}
  if(data && data.savedAt){
   const date=new Date(data.savedAt);
   status.textContent="Đã lưu · "+date.toLocaleDateString("vi-VN")+" "+date.toLocaleTimeString("vi-VN",{hour:"2-digit",minute:"2-digit"})+" · "+Math.max(0,Math.floor(data.score||0))+" điểm";
   loadBtn.disabled=false;
  }else{status.textContent="Chưa có dữ liệu lưu";loadBtn.disabled=true;}
 }
}
function saveLevelSlot(index){
 if(!started || shopOpen || gameOver || victory || index!==levelIndex){
  document.getElementById("save-message").textContent="Bạn chỉ có thể lưu ô của màn đang chơi. Hãy vào màn đó và đóng cửa hàng trước khi lưu.";
  beep(130,.1,"square");return;
 }
 try{
  const data={version:1,savedAt:Date.now(),levelIndex:index,difficulty,score,coins,shopUpgrades,
   player:JSON.parse(JSON.stringify(player)),enemies:JSON.parse(JSON.stringify(enemies)),coinsList:JSON.parse(JSON.stringify(coinsList)),
   boss:boss?JSON.parse(JSON.stringify(boss)):null,traps:JSON.parse(JSON.stringify(traps)),checkpoint:JSON.parse(JSON.stringify(activeCheckpoint)),started:true};
  localStorage.setItem(saveKey(index),JSON.stringify(data));
  document.getElementById("save-message").textContent="Đã lưu tiến trình màn "+(index+1)+" ("+levels[index].name+") thành công.";
  refreshSaveSlots();beep(760,.1,"triangle");
 }catch(e){document.getElementById("save-message").textContent="Không lưu được. Trình duyệt có thể đang chặn bộ nhớ cục bộ.";}
}
function loadLevelSlot(index){
 let data=null;
 try{data=JSON.parse(localStorage.getItem(saveKey(index))||"null");}catch(e){}
 if(!data || data.levelIndex!==index || !data.player || !Number.isFinite(data.player.x) || !Number.isFinite(data.player.y) || !Number.isFinite(data.player.hp) || !Number.isFinite(data.player.maxHp) || !Array.isArray(data.enemies) || !Array.isArray(data.coinsList) || !Array.isArray(data.traps)){document.getElementById("save-message").textContent="Ô lưu màn này đang trống hoặc dữ liệu không hợp lệ. Hãy lưu lại tiến trình mới.";return;}
 try{
  difficulty=difficultySettings[data.difficulty]?data.difficulty:"normal";
  document.querySelectorAll(".diff-btn").forEach(btn=>btn.classList.toggle("active",btn.dataset.diff===difficulty));
  document.getElementById("diffdesc").textContent=difficultySettings[difficulty].desc;
  levelIndex=index;makeWorld(index);
  player=data.player;enemies=data.enemies;coinsList=data.coinsList;boss=data.boss;traps=data.traps;
  activeCheckpoint=data.checkpoint&&Number.isFinite(data.checkpoint.x)&&Number.isFinite(data.checkpoint.y)?data.checkpoint:{x:levels[index].start,y:350,label:"Khởi đầu"};
  score=data.score||0;coins=godMode?INFINITE_COINS:(data.coins||0);shopUpgrades=data.shopUpgrades||{hp:0,damage:0,speed:0};
  started=true;gameOver=false;victory=false;shopOpen=false;attackTimer=0;invuln=0;shake=0;
  document.getElementById("mainmenu").style.display="none";
  document.getElementById("shopmenu").style.display="none";
  document.getElementById("save-message").textContent="Đã tải tiến trình màn "+(index+1)+" ("+levels[index].name+").";
  canvas.focus();refreshSaveSlots();beep(560,.1,"triangle");
 }catch(e){document.getElementById("save-message").textContent="Không thể tải ô lưu này. Hãy thử lưu lại màn chơi.";}
}
document.querySelectorAll("[data-save]").forEach(btn=>btn.addEventListener("click",()=>saveLevelSlot(Number(btn.dataset.save))));
document.querySelectorAll("[data-load]").forEach(btn=>btn.addEventListener("click",()=>loadLevelSlot(Number(btn.dataset.load))));
function update(dt){
 if(!started || gameOver || victory || shopOpen) return;
 dt=Math.min(dt,.033);
 player.anim+=dt*10; attackTimer=Math.max(0,attackTimer-dt); invuln=Math.max(0,invuln-dt); shake=Math.max(0,shake-dt);
 const left=keys["ArrowLeft"]||keys["a"]||keys["A"], right=keys["ArrowRight"]||keys["d"]||keys["D"];
 const jump=keys[" "]||keys["ArrowUp"]||keys["w"]||keys["W"];
 const speed=220+shopUpgrades.speed*24, accel=1500+shopUpgrades.speed*100;
 if(left){player.vx-=accel*dt;player.face=-1;} if(right){player.vx+=accel*dt;player.face=1;}
 if(!left&&!right) player.vx*=Math.pow(.0008,dt);
 player.vx=Math.max(-speed,Math.min(speed,player.vx));
 if(jump && player.grounded){player.vy=-470;player.grounded=false;addParticles(player.x+player.w/2,player.y+player.h,"#a7b8ff",7);beep(360,.07,"square",.025);}
 player.vy+=1150*dt; player.vy=Math.min(player.vy,700);
 // horizontal movement and world boundaries
 player.x+=player.vx*dt; player.x=Math.max(0,Math.min(world.length-player.w,player.x));
 // Keep the prior grounded state for landing effects.
 const wasGrounded=player.grounded;
 // collide with platforms while falling
 const oldY=player.y; player.y+=player.vy*dt; player.grounded=false;
 const floor=floorAt(player.x+player.w/2);
 if(player.y+player.h>=floor && oldY+player.h<=floor+14 && floor<H+50){player.y=floor-player.h;player.vy=0;player.grounded=true;}
 for(const p of platforms()){
  if(player.vy>=0 && oldY+player.h<=p.y+5 && player.y+player.h>=p.y && player.x+player.w>p.x && player.x<p.x+p.w){
   player.y=p.y-player.h;player.vy=0;player.grounded=true;
  }
 }
 if(!wasGrounded && player.grounded){addParticles(player.x+player.w/2,player.y+player.h-1,"#a7b8ff",Math.abs(oldY-player.y)>28?10:5);if(Math.abs(oldY-player.y)>28)shake=Math.max(shake,.08);}
 if(player.y>H+80){
  if(!godMode){player.hp=Math.max(0,player.hp-1);noiseHit();shake=.2;}
  if(player.hp<=0){gameOver=true;beep(90,.5,"sawtooth",.06);}
  else {player.x=activeCheckpoint.x;player.y=activeCheckpoint.y;player.vx=0;player.vy=0;invuln=1.5;}
 }
 // Checkpoints only activate when reached on solid ground, preventing accidental activation mid-jump.
 (world.checkpoints||[]).forEach(cp=>{
  if(player.grounded && Math.abs(player.x-cp.x)<22 && activeCheckpoint.label!==cp.label){activateCheckpoint(cp);}
 });
 checkpointNotice=Math.max(0,checkpointNotice-dt);
 // collect coins
 coinsList.forEach(c=>{if(!c.taken && Math.abs((player.x+player.w/2)-c.x)<22 && Math.abs((player.y+player.h/2)-c.y)<25){c.taken=true;coins=godMode?INFINITE_COINS:coins+1;score+=10;beep(800,.06,"sine",.035);addParticles(c.x,c.y,"#ffd166",7);if(shopOpen)updateShopUI();}});
 // Enemy AI: archers fire aimed arrows; tankers leap onto raised platforms and shove the player.
 enemies.forEach(e=>{
  if(!e.alive)return;
  e.flash=Math.max(0,(e.flash||0)-dt);
  const dx=(player.x+player.w/2)-(e.x+e.w/2);
  const distance=Math.abs(dx);
  if(e.type==="archer"){
   // Keep a little distance from the player, but continue patrolling when far away.
   if(distance<250)e.vx*=Math.pow(.92,dt*60);
   else {e.x+=e.vx*dt;if(Math.abs(e.x-e.home)>e.range)e.vx*=-1;}
   e.shotCooldown-=dt;
   if(e.shotCooldown<=0 && distance<560){
    const dir=dx>=0?1:-1;
    const sx=e.x+e.w/2+dir*8, sy=e.y+12;
    const aimY=(player.y+player.h*.42)-sy;
    const len=Math.max(1,Math.hypot(dx,aimY));
    const arrowSpeed=difficulty==="hard"?370:310;
    enemyArrows.push({x:sx,y:sy,vx:dx/len*arrowSpeed,vy:aimY/len*arrowSpeed,life:2.3,damage:difficulty==="hard"?.8:.55,angle:Math.atan2(aimY,dx),trail:0});
    e.shotCooldown=(difficulty==="hard"?1.25:1.75)+Math.random()*.65;
    addParticles(sx,sy,"#ff8a65",3);beep(210,.035,"triangle",.012);
   }
  }else{
   // Tanker has a short wind-up, then charges with enough force to push the player.
   e.chargeCooldown-=dt;
   if(e.charging>0){
    e.charging-=dt;e.x+=e.vx*2.25*dt;
    if(e.charging<=0){e.vx=Math.sign(e.vx||1)*52*difficultySettings[difficulty].enemy;}
   }else{
    const dir=dx>=0?1:-1;
    e.x+=e.vx*dt;
    if(Math.abs(e.x-e.home)>e.range)e.vx*=-1;
    // Jump when a raised platform is directly ahead or the player is on higher ground.
    const foot=e.y+e.h;
    const nearPlatform=platforms().find(p=>{
     const ahead=dir>0?(p.x>e.x+e.w-3 && p.x<e.x+e.w+58):(p.x+p.w<e.x+3 && p.x+p.w>e.x-58);
     return ahead && p.y<foot-16 && p.y>foot-112;
    });
    const playerAbove=player.y+player.h<e.y+e.h-24 && distance<175;
    e.jumpCooldown-=dt;
    if(e.grounded && e.jumpCooldown<=0 && (nearPlatform||playerAbove)){
     e.vy=nearPlatform?-440:-390;e.grounded=false;
     e.jumpCooldown=1.25+Math.random()*.5;
     addParticles(e.x+e.w/2,e.y+e.h,"#d97706",5);
    }
    e.vy=Math.min(650,(e.vy||0)+1080*dt);
    const oldEnemyY=e.y;e.y+=e.vy*dt;e.grounded=false;
    const efloor=floorAt(e.x+e.w/2);
    if(e.y+e.h>=efloor && oldEnemyY+e.h<=efloor+18 && efloor<H+50){e.y=efloor-e.h;e.vy=0;e.grounded=true;}
    for(const p of platforms()){
     if(e.vy>=0 && oldEnemyY+e.h<=p.y+5 && e.y+e.h>=p.y && e.x+e.w>p.x && e.x<p.x+p.w){
      e.y=p.y-e.h;e.vy=0;e.grounded=true;
     }
    }
    if(e.chargeCooldown<=0 && distance<180 && distance>25){
     e.vx=dir*(difficulty==="hard"?220:185);e.charging=.42;e.chargeCooldown=2.1;
     addParticles(e.x+e.w/2,e.y+e.h-3,"#fb923c",7);shake=Math.max(shake,.07);
    }
   }
  }
  // Stay inside the level and collide with the player.
  e.x=Math.max(0,Math.min(world.length-e.w,e.x));
  const eb={x:e.x,y:e.y,w:e.w,h:e.h};
  if(hit(player,eb)){
   if(e.type==="tanker" && e.charging>0){
    if(!godMode && invuln<=0){
     player.hp=Math.max(0,player.hp-(difficulty==="hard"?1.1:.8));
     player.vx=Math.sign(dx||1)*(difficulty==="hard"?430:350);
     player.vy=-245;invuln=1.0;noiseHit();shake=.24;
     addParticles(player.x+player.w/2,player.y+player.h/2,"#fb923c",12);
     if(player.hp<=0){gameOver=true;beep(90,.5,"sawtooth",.06);}
    }
   }else if(player.vy>80 && oldY+player.h<e.y+12){
    e.hp-=1;e.flash=.15;player.vy=-300;score+=e.type==="tanker"?60:100;
    addParticles(e.x+e.w/2,e.y,"#a9c6d9",10);beep(500,.07);
    if(e.hp<=0)e.alive=false;
   }else damage();
  }
 });
 // Arrow projectiles keep moving independently and deal damage on impact.
 enemyArrows=enemyArrows.filter(a=>{
  a.life-=dt;a.x+=a.vx*dt;a.y+=a.vy*dt;a.trail=(a.trail||0)+dt;
  if(a.life<=0||a.x<cam-60||a.x>cam+W+60||a.y<-40||a.y>H+40)return false;
  if(hit(player,{x:a.x-5,y:a.y-3,w:10,h:6})){
   if(!godMode && invuln<=0){
    player.hp=Math.max(0,player.hp-a.damage);player.vx+=(a.vx>0?1:-1)*150;player.vy=-110;
    invuln=.8;noiseHit();addParticles(a.x,a.y,"#ff8a65",8);
    if(player.hp<=0){gameOver=true;beep(90,.5,"sawtooth",.06);}
   }
   return false;
  }
  return true;
 });
 if(boss && boss.alive){
  boss.x+=boss.vx*dt;
  if(boss.x<1150||boss.x>1550)boss.vx*=-1;
  boss.flash=Math.max(0,boss.flash-dt);
  boss.attack+=dt;
  const bossAttackInterval=boss.hp<=boss.maxHp/2?1.45:2.25;
  if(boss.attack>=bossAttackInterval){
   boss.attack=0;
   const dx=(player.x+player.w/2)-(boss.x+boss.w/2),dy=(player.y+player.h/2)-(boss.y+boss.h/2),len=Math.max(1,Math.hypot(dx,dy));
   bossProjectiles.push({x:boss.x+boss.w/2,y:boss.y+boss.h*.45,vx:dx/len*(boss.hp<=boss.maxHp/2?280:220),vy:dy/len*(boss.hp<=boss.maxHp/2?280:220),r:9,life:3,damage:1});
   addParticles(boss.x+boss.w/2,boss.y+25,"#d946ef",5);beep(boss.hp<=boss.maxHp/2?145:185,.1,"sawtooth",.035);
  }
  if(hit(player,boss)){if(player.vy>90 && oldY+player.h<boss.y+18){boss.hp--;player.vy=-330;boss.flash=.2;score+=25;beep(190,.08,"sawtooth");if(boss.hp<=0){boss.alive=false;score+=1000;}}else damage();}
 }
 // Boss soul bolts: dodge vertically or jump over them; the boss fires faster below half health.
 bossProjectiles=bossProjectiles.filter(p=>p.life>0 && p.x>-80 && p.x<world.length+80);
 bossProjectiles.forEach(p=>{
  p.x+=p.vx*dt;p.y+=p.vy*dt;p.life-=dt;p.vy+=80*dt;
  const box={x:p.x-p.r,y:p.y-p.r,w:p.r*2,h:p.r*2};
  if(hit(player,box)){damage(p.damage);p.life=0;addParticles(p.x,p.y,"#e879f9",10);}
 });
 // Traps: rolling boulders and timed flame vents. Damage values are different by trap.
 traps.forEach(t=>{
  t.hitCooldown=Math.max(0,t.hitCooldown-dt);
  if(t.type==="boulder"){
   // A giant boulder drops vertically from above after a long warning/rest interval.
   const size=t.size||112, landingY=world.ground-size;
   if(t.state==="rest"){
    t.y=-size-10;
    t.pauseTimer-=dt;
    if(t.pauseTimer<=0){t.state="drop";beep(95,.18,"sawtooth",.05);}
   } else if(t.state==="drop"){
    t.y+= (t.dropSpeed||620)*dt;
    if(t.y>=landingY){
     t.y=landingY;t.state="landed";t.impactTimer=.55;t.pauseTimer=.55;shake=.32;
     addParticles(t.x,world.ground-5,"#b8aaa0",24);beep(58,.28,"sawtooth",.065);
    }
   } else if(t.state==="landed"){
    t.pauseTimer-=dt;
    if(t.pauseTimer<=0){t.state="rest";t.y=-size-10;t.pauseTimer=t.pause||6.5;}
   }
   // Collision follows the falling rock, not just its final ground position.
   const b={x:t.x-size*.46,y:t.y+size*.06,w:size*.92,h:size*.88};
   if(t.state!=="rest" && hit(player,b)&&t.hitCooldown<=0){damage(t.damage);t.hitCooldown=1.35;addParticles(t.x,Math.max(0,t.y+size/2),"#b8aaa0",16);}
  } else if(t.type==="fire"){
   t.phase=(t.phase+dt)%t.period;
   t.flameOn=t.phase<t.active;
   const flameH=t.flameHeight||78;
   const flame={x:t.x-14,y:world.ground-flameH,w:28,h:flameH};
   if(t.flameOn&&hit(player,flame)&&t.hitCooldown<=0){damage(t.damage);t.hitCooldown=1.3;addParticles(t.x,world.ground-45,"#ff8738",10);beep(95,.12,"sawtooth",.045);}
  } else if(t.type==="laser"){
   // Level 3: a large laser orb bounces across the playable area and carries its beam with it.
   if(t.bouncy){
    const radius=t.radius||42;
    t.x+=t.laserVx*dt;t.y+=t.laserVy*dt;
    if(t.x<radius+8){t.x=radius+8;t.laserVx=Math.abs(t.laserVx);}
    if(t.x>world.length-radius-8){t.x=world.length-radius-8;t.laserVx=-Math.abs(t.laserVx);}
    if(t.y<radius+18){t.y=radius+18;t.laserVy=Math.abs(t.laserVy);}
    if(t.y>world.ground-radius-8){t.y=world.ground-radius-8;t.laserVy=-Math.abs(t.laserVy);}
    t.points=[[t.x-radius*2.6,t.y],[t.x+radius*2.6,t.y]];
   }
   // Laser pulses on/off; its route has at most three reflections at solid mirror objects.
   const period=t.period/(difficulty==="hard"?1.2:difficulty==="easy"?0.88:1);
   const active=t.active*(difficulty==="hard"?1.18:difficulty==="easy"?0.78:1);
   t.laserPhase=(t.laserPhase+dt)%period;
   t.laserOn=t.laserPhase<active;
   if(t.laserOn && t.hitCooldown<=0){
    const pts=t.points||[]; let hitBeam=false;
    const px=player.x+player.w/2,py=player.y+player.h/2;
    if(t.bouncy && Math.hypot(px-t.x,py-t.y)<(t.radius||42)+Math.max(player.w,player.h)*.35) hitBeam=true;
    for(let i=0;i<pts.length-1;i++){
     const a=pts[i],b=pts[i+1],dx=b[0]-a[0],dy=b[1]-a[1],len2=dx*dx+dy*dy;
     const u=Math.max(0,Math.min(1,((px-a[0])*dx+(py-a[1])*dy)/(len2||1)));
     const qx=a[0]+u*dx,qy=a[1]+u*dy;
     if(Math.hypot(px-qx,py-qy)<(t.bouncy?10:13)){hitBeam=true;break;}
    }
    if(hitBeam){damage(t.damage);t.hitCooldown=1.05;addParticles(player.x+12,player.y+16,"#ff4d6d",12);beep(150,.1,"sawtooth",.045);}
   }
  }
 });
 // exit
 if(player.x+player.w>world.goal && (!world.boss || !boss.alive)) nextLevel();
 particles=particles.filter(p=>p.life>0);
 particles.forEach(p=>{p.x+=p.vx*dt;p.y+=p.vy*dt;p.vy+=350*dt;p.life-=dt;});
}

function glow(x,y,r,color,alpha=1){
 const g=ctx.createRadialGradient(x,y,1,x,y,r);g.addColorStop(0,color);g.addColorStop(1,"rgba(0,0,0,0)");
 ctx.save();ctx.globalAlpha=alpha;ctx.fillStyle=g;ctx.fillRect(x-r,y-r,r*2,r*2);ctx.restore();
}
function drawDungeonBackground(cam){
 // MÀN II — HẦM NGỤC: trần đá thấp, tường cổ, cột nứt và dòng dung nham.
 const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,"#080e16");g.addColorStop(.55,"#18252c");g.addColorStop(1,"#351c1d");ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
 glow(180-cam*.025,345,220,"#ff4d24",.15);glow(700-cam*.018,390,250,"#e23c22",.12);
 // Distant rock layers
 for(let layer=0;layer<3;layer++){
  const par=.06+layer*.07, base=layer===0?250:layer===1?320:390, color=["#111b25","#17232b","#202a2c"][layer];
  ctx.fillStyle=color;ctx.beginPath();ctx.moveTo(0,base);
  for(let x=0;x<=W+80;x+=55){const y=base+Math.sin((x+cam*par)*.018+layer)*17+((Math.floor(x/55)*17)%23);ctx.lineTo(x,y);}
  ctx.lineTo(W,H);ctx.lineTo(0,H);ctx.closePath();ctx.fill();
 }
 // Massive masonry blocks scrolling at different depths
 for(let i=-1;i<12;i++){
  const x=((i*105-cam*.13)%(W+105)+(W+105))%(W+105)-40;
  const y=55+(i%3)*48;
  rect(x,y,78,38,"#26343a");rect(x+3,y+3,72,31,"#1b272e");rect(x+8,y+7,24,3,"#35434a");
  rect(x+78,y+15,27,4,"#0b1319");
 }
 // Heavy pillars, broken capitals, and hanging chains
 for(let i=-1;i<7;i++){
  const x=((i*175-cam*.22)%(W+175)+(W+175))%(W+175)-20;
  const top=95+(i%2)*35;
  rect(x,top,30,world?world.ground-top:335,"#29363b");rect(x+5,top,5,world?world.ground-top:335,"#3a4547");
  rect(x-8,top-8,46,12,"#465052");rect(x-3,top-13,36,5,"#657071");
  rect(x+12,top+35,3,45,"#172127");rect(x+10,top+80,7,3,"#586163");
  ctx.strokeStyle="#4a5353";ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x+55,0);ctx.lineTo(x+55,35+(i%4)*18);ctx.stroke();
 }
 // Glowing lava fissures in the far depth
 for(let i=0;i<8;i++){
  const x=((i*137-cam*.19)%(W+137)+(W+137))%(W+137);
  glow(x,398,45,"#ff4b20",.25);rect(x-13,394,28,3,"#ff6530");rect(x-5,389,4,5,"#ffb15c");
 }
 // Drifting ash
 for(let i=0;i<42;i++){
  const x=((i*83+performance.now()*.012*(i%3+1)-cam*.08)%(W+30)+(W+30))%(W+30)-10;
  const y=(i*47+performance.now()*.018*(i%2+1))%(H-45);
  rect(x,y,i%5===0?3:2,2,i%4===0?"#ff9b62":"#849093");
 }
}
function drawArenaBackground(cam){
 // MÀN III — ĐẤU TRƯỜNG: bầu trời đỏ thẫm, nguyệt thực, khán đài và cột đá đổ nát.
 const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,"#100b1b");g.addColorStop(.48,"#351725");g.addColorStop(1,"#642b25");ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
 const pulse=.8+.2*Math.sin(performance.now()*.001);
 glow(690,125,165,"#f0444e",.24*pulse);glow(690,125,82,"#e3a17b",.18);
 // Blood moon / eclipse
 ctx.fillStyle="#27131f";ctx.beginPath();ctx.arc(690,125,58,0,Math.PI*2);ctx.fill();ctx.fillStyle="#c45a58";ctx.beginPath();ctx.arc(690,125,47,0,Math.PI*2);ctx.fill();
 ctx.fillStyle="#5e2836";ctx.fillRect(655,97,20,7);ctx.fillRect(685,133,28,8);ctx.fillRect(708,110,12,5);
 // Tiered arena stands and tiny torch lights
 for(let row=0;row<4;row++){
  const y=235+row*34;ctx.fillStyle=["#241522","#301927","#3b2029","#48262b"][row];
  ctx.beginPath();ctx.moveTo(0,y+22);ctx.lineTo(W,y-10);ctx.lineTo(W,H);ctx.lineTo(0,H);ctx.closePath();ctx.fill();
  for(let i=0;i<18;i++){
   const x=((i*61-row*17-cam*(.035+row*.02))%(W+20)+(W+20))%(W+20);
   rect(x,y+(i%3)*4,3,4,(i+row)%4===0?"#ffb65f":(i%2?"#a64d54":"#70404d"));
  }
 }
 // Ancient arena arches and cracked pillars
 for(let i=-1;i<7;i++){
  const x=((i*170-cam*.16)%(W+170)+(W+170))%(W+170)-15;
  const h=125+(i%3)*32, y=world?world.ground-h:430-h;
  rect(x,y,27,h,"#3b3039");rect(x+5,y+5,5,h-8,"#55404a");rect(x-9,y-10,45,13,"#67505a");
  rect(x-4,y-15,35,5,"#927078");rect(x+13,y+Math.floor(h*.45),4,23,"#261b27");
  if(i%2===0){rect(x+31,y+35,20,5,"#6e3844");rect(x+47,y+40,4,27,"#7c303d");}
 }
 // Torn crimson banners and sparks
 for(let i=0;i<6;i++){
  const x=((i*145-cam*.24)%(W+145)+(W+145))%(W+145);
  rect(x,75,3,68,"#8e7470");rect(x+3,80,27,24,"#8e263a");rect(x+3,104,20,14,"#681b31");
  ctx.fillStyle="#b8424e";ctx.beginPath();ctx.moveTo(x+3,118);ctx.lineTo(x+13,112);ctx.lineTo(x+21,122);ctx.lineTo(x+30,116);ctx.lineTo(x+30,129);ctx.lineTo(x+3,129);ctx.closePath();ctx.fill();
 }
 for(let i=0;i<30;i++){
  const x=((i*97+performance.now()*.016*(i%3+1)-cam*.1)%(W+20)+(W+20))%(W+20);
  const y=(i*53-performance.now()*.025*(i%2+1)+H)%(H-35);
  glow(x,y,9,"#ff5c45",.18);rect(x,y,2,3,i%3===0?"#ffd17a":"#e96b52");
 }
}
function drawBackground(cam){
 if(levelIndex===1){drawDungeonBackground(cam);return;}
 if(levelIndex===2){drawArenaBackground(cam);return;}
 // MÀN I — RỪNG TÀN: bầu trời tím, trăng lạnh và rừng ma ám.
 // Night sky with a soft violet horizon
 const sky=ctx.createLinearGradient(0,0,0,H);sky.addColorStop(0,"#090d1d");sky.addColorStop(.55,"#171b35");sky.addColorStop(1,"#34213e");ctx.fillStyle=sky;ctx.fillRect(0,0,W,H);
 // Cinematic aurora ribbons and distant shafts of moonlight.
 const time = performance.now() * 0.00012;
 ctx.save();
 for(let i=0;i<4;i++){
  const x=((i*310 - cam*.035 + Math.sin(time+i)*65)% (W+180))-80;
  const beam=ctx.createLinearGradient(x,20,x+95,390);
  beam.addColorStop(0,"rgba(174,145,255,0)");
  beam.addColorStop(.48,"rgba(133,119,220,0.055)");
  beam.addColorStop(1,"rgba(174,145,255,0)");
  ctx.fillStyle=beam;ctx.beginPath();ctx.moveTo(x-25,0);ctx.lineTo(x+65,0);ctx.lineTo(x+180,390);ctx.lineTo(x+60,390);ctx.closePath();ctx.fill();
 }
 ctx.globalAlpha=.11;
 for(let i=0;i<3;i++){
  ctx.strokeStyle=["#6f7fe0","#a76ac9","#5265a8"][i];ctx.lineWidth=20-i*5;
  ctx.beginPath();
  for(let x=0;x<=W;x+=24){
   const y=95+i*34+Math.sin(x*.008+time*9+i*1.8)*20+Math.sin(x*.017-time*6)*8;
   if(x===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);
  }
  ctx.stroke();
 }
 ctx.restore();

 // distant stars, with a few twinkling pixels
 for(let i=0;i<95;i++){let x=((i*173)%W-cam*.09+W)%W,y=(i*71)%300;let tw=.45+.45*Math.sin(performance.now()/550+i);ctx.globalAlpha=tw;rect(x,y,i%9===0?3:2,i%9===0?3:2,i%4===0?"#e6d5ff":"#9faed8");}ctx.globalAlpha=1;
 // moon halo and pixel moon
 const mx=770-cam*.055,my=105;glow(mx,my,115,"#8c74d8",.26);glow(mx,my,54,"#b6a6ee",.24);
 rect(mx-28,my-28,56,56,"#d8d3f3");rect(mx-22,my-34,42,6,"#d8d3f3");rect(mx-34,my-20,6,40,"#d8d3f3");rect(mx+28,my-18,6,34,"#d8d3f3");
 rect(mx-17,my-13,12,7,"#b0aed7");rect(mx+7,my+7,15,9,"#b0aed7");rect(mx-6,my+18,8,5,"#b0aed7");
 // distant mountains
 for(let i=0;i<12;i++){let x=i*120-(cam*.14%120);ctx.fillStyle=i%2?"#20243d":"#171d32";ctx.beginPath();ctx.moveTo(x,430);ctx.lineTo(x+54,240+(i%4)*20);ctx.lineTo(x+130,430);ctx.fill();}
 // layered haunted forest silhouettes, parallax
 for(let layer=0;layer<2;layer++){
  const par=layer?.31:.22, base=layer?430:405, col=layer?"#111b2a":"#182235";
  for(let i=-2;i<14;i++){let x=i*94-(cam*par%94),h=95+((i*37+11)%5)*19;ctx.fillStyle=col;ctx.beginPath();ctx.moveTo(x+45,base-h);ctx.lineTo(x+17,base-20);ctx.lineTo(x+31,base-20);ctx.lineTo(x+5,base+8);ctx.lineTo(x+37,base+3);ctx.lineTo(x+37,base+25);ctx.lineTo(x+54,base+25);ctx.lineTo(x+54,base+3);ctx.lineTo(x+83,base+8);ctx.lineTo(x+60,base-20);ctx.lineTo(x+73,base-20);ctx.closePath();ctx.fill();rect(x+47,base+4,5,35,"#0b1421");}
 }
 // mist bands drift slowly across the bottom of the scene
 for(let i=0;i<5;i++){let x=((i*245-(performance.now()*.012)%1200)-100);glow(x,400+(i%3)*17,125,"#7580b7",.055);}
 // faint horizon lights
 for(let i=0;i<9;i++){let x=((i*131-cam*.19)%W+W)%W;glow(x,380,25,"#a78bfa",.12);rect(x,378,3,3,"#c4b5fd");}
}
function drawWorld(cam){
 // deep void below the platforms
 rect(0,world.ground+4,W,H-world.ground,"#090b15");
 let start=Math.floor(cam/80)*80;
 for(let x=start;x<cam+W+80;x+=80){
  const center=x+40;
  if(!world.pits.some(p=>center>p[0]&&center<p[1])){
   const floorBase=levelIndex===0?"#1d2c31":levelIndex===1?"#292d32":"#39272d";
   const floorTop=levelIndex===0?"#6a9a70":levelIndex===1?"#68777a":"#bd6252";
   const floorEdge=levelIndex===0?"#354f4a":levelIndex===1?"#414b50":"#6d393e";
   rect(x-cam,world.ground,80,H-world.ground,floorBase);
   rect(x-cam,world.ground,80,6,floorTop);rect(x-cam,world.ground+6,80,3,floorEdge);
   for(let k=0;k<9;k++){const xx=x-cam+(k*19)%76,yy=world.ground+16+(k*23)%88;rect(xx,yy,4+(k%3),3,levelIndex===0?(k%2?"#2b4140":"#142329"):levelIndex===1?(k%2?"#343a3e":"#171e23"):(k%2?"#573038":"#251b24"));}
   // Forest grass, dungeon rubble, or arena ash along the floor edge.
   for(let k=0;k<5;k++){let gx=x-cam+k*17+5;if(levelIndex===0)rect(gx,world.ground-3,2,5,k%2?"#9bc58a":"#507f69");else if(levelIndex===1){rect(gx,world.ground-3,4,3,"#727b7c");rect(gx+3,world.ground-5,2,2,"#3c484d");}else{rect(gx,world.ground-3,3,4,k%2?"#c76a57":"#78414a");}}
  }else{
   rect(x-cam,world.ground+5,80,H-world.ground,levelIndex===1?"#020508":"#10040c");glow(x-cam+40,world.ground+65,48,levelIndex===1?"#ff5428":"#f0444e",.15);
   rect(x-cam,world.ground+5,80,3,levelIndex===1?"#8b4538":"#9a3b4b");
  }
 }
 // platforms with stone edges and pixel cracks
 platforms().forEach((p,i)=>{
  const stoneBase=levelIndex===0?"#33364d":levelIndex===1?"#3b4549":"#49313d";
  const stoneTop=levelIndex===0?"#9d8bb7":levelIndex===1?"#9aa3a0":"#d08a73";
  const stoneEdge=levelIndex===0?"#625675":levelIndex===1?"#5b6669":"#80505a";
  rect(p.x-cam,p.y,p.w,p.h,stoneBase);rect(p.x-cam,p.y,p.w,4,stoneTop);rect(p.x-cam,p.y+4,p.w,3,stoneEdge);
  for(let x=9;x<p.w;x+=25){rect(p.x-cam+x,p.y+8,11,3,levelIndex===0?"#25293d":levelIndex===1?"#252d31":"#2d202b");rect(p.x-cam+x+5,p.y+11,4,2,levelIndex===0?"#4b465e":levelIndex===1?"#657071":"#a35c60");}
  for(let x=12;x<p.w;x+=47)rect(p.x-cam+x,p.y-3,3,3,stoneTop);
 });
 // Ancient runes etched into selected platforms.
 platforms().forEach((p,i)=>{
  if(i%2===0){
   const rx=p.x+p.w*.52-cam, ry=p.y+7;
   ctx.save();ctx.globalAlpha=.32+.14*Math.sin(performance.now()/260+i);
   ctx.strokeStyle="#b6a0e8";ctx.lineWidth=1;
   ctx.beginPath();ctx.moveTo(rx-5,ry);ctx.lineTo(rx,ry-3);ctx.lineTo(rx+5,ry);
   ctx.lineTo(rx,ry+4);ctx.closePath();ctx.stroke();
   ctx.beginPath();ctx.moveTo(rx,ry-2);ctx.lineTo(rx,ry+3);ctx.stroke();ctx.restore();
  }
 });
 // Floating spectral wisps that drift at different depths.
 for(let i=0;i<12;i++){
  const wx=((i*103+performance.now()*.018*(i%3+1)-cam*.16)%(W+80)+W+80)%(W+80)-20;
  const wy=215+(i*47)%190+Math.sin(performance.now()*.0015+i*2)*12;
  glow(wx,wy,20,i%3===0?"#e879f9":"#8b9cff",.12);
  rect(wx,wy,3,5,i%3===0?"#e9a8ff":"#b6c5ff");
  rect(wx+2,wy-3,2,3,"#e8e7ff");
 }
 // Dangling roots and dead branches frame the upper edge of the scene.
 for(let i=0;i<11;i++){
  const rx=((i*117-cam*.24)%W+W)%W;
  const len=18+(i*29)%42;
  ctx.fillStyle="#10131f";ctx.beginPath();ctx.moveTo(rx,0);ctx.lineTo(rx+8,0);ctx.lineTo(rx+4,len);ctx.lineTo(rx+1,len-5);ctx.closePath();ctx.fill();
  if(i%3===0){ctx.fillStyle="#28213b";ctx.beginPath();ctx.moveTo(rx+5,len*.45);ctx.lineTo(rx+19,len*.62);ctx.lineTo(rx+6,len*.7);ctx.fill();}
 }
 // Tiny bioluminescent mushrooms beside safe ground.
 for(let i=0;i<15;i++){
  const mx=((i*149-cam*.65)%W+W)%W, my=world.ground-4;
  if(!world.pits.some(p=>mx+cam>p[0]&&mx+cam<p[1])){
   rect(mx,my-7,3,7,"#b9a4cf");rect(mx-3,my-9,9,4,i%3===0?"#d87bda":"#7993c7");
   glow(mx+1,my-7,13,i%3===0?"#d946ef":"#818cf8",.22);
  }
 }
 // dangerous crystal spikes
 world.pits.forEach(p=>{for(let x=p[0]+4;x<p[1]-8;x+=16){glow(x-cam+8,world.ground-5,16,"#fb477e",.22);ctx.fillStyle="#e84e83";ctx.beginPath();ctx.moveTo(x-cam,world.ground+7);ctx.lineTo(x+8-cam,world.ground-12);ctx.lineTo(x+16-cam,world.ground+7);ctx.fill();ctx.fillStyle="#ffb4d0";ctx.beginPath();ctx.moveTo(x+6-cam,world.ground-7);ctx.lineTo(x+8-cam,world.ground-12);ctx.lineTo(x+10-cam,world.ground-7);ctx.fill();}});
 // New traps: chunky pixel boulders and warning-lit flame vents.
 traps.forEach(t=>{
  const x=t.x-cam;
  if(t.type==="boulder"){
   const size=t.size||112, bx=t.x-cam-size/2, by=t.y;
   // Show a faint vertical warning mark while the giant rock waits overhead.
   if(t.state==="rest"){
    ctx.globalAlpha=.35;rect(x-2,0,4,world.ground-size,"#8f7958");ctx.globalAlpha=1;
    const pulse=.25+.25*Math.sin(performance.now()/220);
    glow(x,Math.min(120,world.ground-size),size*.65,"#d4a66b",pulse*.2);
    rect(x-9,8,18,3,"#8f7958");
   }
   if(t.state!=="rest"){
    // Ground shadow grows darker on impact; the boulder itself falls from the top of the screen.
    ctx.globalAlpha=t.state==="landed"?.48:.18;rect(x-size*.58,world.ground-5,size*1.16,7,"#000000");ctx.globalAlpha=1;
    glow(x,by+size*.5,size*.75,t.state==="drop"?"#b4a18a":"#887b68",t.state==="drop"?.18:.24);
    rect(bx+size*.22,by+size*.04,size*.54,size*.08,"#756e63");
    rect(bx+size*.12,by+size*.12,size*.76,size*.15,"#625e57");
    rect(bx+size*.06,by+size*.27,size*.88,size*.43,"#514f4b");
    rect(bx+size*.12,by+size*.70,size*.76,size*.17,"#3d3d3c");
    rect(bx+size*.24,by+size*.87,size*.52,size*.08,"#292c2d");
    rect(bx+size*.20,by+size*.17,size*.22,size*.14,"#8a8174");
    rect(bx+size*.56,by+size*.31,size*.20,size*.12,"#777166");
    rect(bx+size*.16,by+size*.49,size*.18,size*.11,"#393b3b");
    rect(bx+size*.48,by+size*.62,size*.25,size*.13,"#686258");
    rect(bx+size*.34,by+size*.38,size*.09,size*.18,"#353737");
    rect(bx+size*.72,by+size*.18,size*.08,size*.08,"#a09786");
    if(t.state==="drop"){
     rect(bx-size*.18,by+size*.48,size*.13,4,"#aaa092");rect(bx+size*1.04,by+size*.34,size*.12,4,"#aaa092");
    }
   }
  } else if(t.type==="fire"){
   rect(x-17,world.ground-4,34,8,"#373b42");rect(x-12,world.ground-8,24,4,"#77736b");
   rect(x-5,world.ground-12,10,4,"#c06b39");
   const warning=t.phase>t.active-.35;
   if(t.flameOn){
    const fh=t.flameHeight||78;
    glow(x,world.ground-fh*.58,Math.max(28,fh*.48),"#ff5a22",.45);
    rect(x-9,world.ground-18,18,12,"#f06a2b");
    // Build the flame upward in pixel tiers; on HARD each vent has a different height.
    for(let yy=world.ground-24, tier=0; yy>world.ground-fh; yy-=14,tier++){
     const width=Math.max(4,18-tier*2+(tier%2?2:0));
     rect(x-width/2,yy,width,14,tier%2?"#ff9c36":"#ffd47b");
     if(width>7)rect(x-2,yy+3,4,Math.min(8,14),"#fff0b5");
    }
   }
   else if(warning){glow(x,world.ground-12,20,"#ff5a22",.18);rect(x-3,world.ground-17,6,4,"#ff9c36");}
  } else if(t.type==="laser"){
   const pts=t.points||[];
   if(t.bouncy){
    const cx=t.x-cam,cy=t.y,r=t.radius||42;
    // Wide pulsing beam plus a large glowing core.
    if(t.laserOn && pts.length>1){
     const a=pts[0],b=pts[1];
     ctx.save();ctx.strokeStyle="#ff244f";ctx.lineWidth=18;ctx.globalAlpha=.24;ctx.beginPath();ctx.moveTo(a[0]-cam,a[1]);ctx.lineTo(b[0]-cam,b[1]);ctx.stroke();
     ctx.strokeStyle="#ff3158";ctx.lineWidth=8;ctx.globalAlpha=.75;ctx.beginPath();ctx.moveTo(a[0]-cam,a[1]);ctx.lineTo(b[0]-cam,b[1]);ctx.stroke();
     ctx.strokeStyle="#ffe8ed";ctx.lineWidth=3;ctx.globalAlpha=.98;ctx.beginPath();ctx.moveTo(a[0]-cam,a[1]);ctx.lineTo(b[0]-cam,b[1]);ctx.stroke();ctx.restore();
    }
    glow(cx,cy,r*2.3,"#ff174f",t.laserOn?.65:.3);
    glow(cx,cy,r*1.25,"#ff496b",.7);
    ctx.save();ctx.translate(cx,cy);ctx.rotate(performance.now()/280);
    ctx.strokeStyle=t.laserOn?"#fff0f3":"#ff7f9b";ctx.lineWidth=5;
    ctx.beginPath();ctx.moveTo(-r*.78,0);ctx.lineTo(r*.78,0);ctx.moveTo(0,-r*.78);ctx.lineTo(0,r*.78);ctx.stroke();
    ctx.fillStyle=t.laserOn?"#fff0f3":"#ff8ca5";ctx.beginPath();ctx.arc(0,0,r*.62,0,Math.PI*2);ctx.fill();
    ctx.fillStyle="#b80f39";ctx.beginPath();ctx.arc(0,0,r*.3,0,Math.PI*2);ctx.fill();ctx.restore();
   } else {
   // Emitter and up to three solid reflectors along the authored laser route.
   pts.forEach((p,i)=>{
    const px=p[0]-cam,py=p[1];
    if(i===0){glow(px,py,28,"#ff334f",.35);rect(px-10,py-8,20,16,"#34363e");rect(px-6,py-4,12,8,t.laserOn?"#ff4d6d":"#74404b");}
    else if(i<pts.length-1){rect(px-7,py-7,14,14,"#55515b");rect(px-4,py-4,8,8,"#c6c0d0");rect(px-2,py-2,4,4,"#ff758f");}
   });
   if(t.laserOn&&pts.length>1){
    for(let i=0;i<pts.length-1;i++){
     const a=pts[i],b=pts[i+1],ax=a[0]-cam,bx=b[0]-cam;
     glow((ax+bx)/2,(a[1]+b[1])/2,22,"#ff244f",.2);
     ctx.save();ctx.strokeStyle="#ff3158";ctx.lineWidth=7;ctx.globalAlpha=.28;ctx.beginPath();ctx.moveTo(ax,a[1]);ctx.lineTo(bx,b[1]);ctx.stroke();
     ctx.strokeStyle="#ff496b";ctx.lineWidth=3;ctx.globalAlpha=.9;ctx.beginPath();ctx.moveTo(ax,a[1]);ctx.lineTo(bx,b[1]);ctx.stroke();
     ctx.strokeStyle="#ffe8ed";ctx.lineWidth=1;ctx.globalAlpha=.95;ctx.beginPath();ctx.moveTo(ax,a[1]);ctx.lineTo(bx,b[1]);ctx.stroke();ctx.restore();
    }
   } else if(pts.length>1){const a=pts[0],b=pts[1];ctx.save();ctx.strokeStyle="#ff526e";ctx.lineWidth=2;ctx.globalAlpha=.25;ctx.beginPath();ctx.moveTo(a[0]-cam,a[1]);ctx.lineTo(b[0]-cam,b[1]);ctx.stroke();ctx.restore();}
   }
  }
  // Countdown badge for every trap: tells the player when danger starts or ends.
  let timerLabel="", timerX=t.x-cam, timerY=world.ground-105, timerColor="#fbbf24";
  if(t.type==="boulder"){
   if(t.state==="rest"){timerLabel="ĐÁ RƠI: "+Math.max(0,Math.ceil(t.pauseTimer))+"s";timerY=42;timerColor="#f4c27a";}
   else if(t.state==="drop"){timerLabel="ĐANG RƠI!";timerY=Math.max(24,t.y-22);timerColor="#ff6868";}
   else {timerLabel="ĐÁ ĐÃ RƠI";timerY=world.ground-(t.size||112)-24;timerColor="#c4b5a5";}
  } else if(t.type==="fire"){
   if(t.flameOn){timerLabel="LỬA TẮT: "+Math.max(0,(t.active-t.phase)).toFixed(1)+"s";timerColor="#ff7b45";}
   else {timerLabel="LỬA SAU: "+Math.max(0,(t.period-t.phase)).toFixed(1)+"s";timerColor="#fbbf24";}
   timerY=world.ground-(t.flameHeight||78)-27;
  } else if(t.type==="laser"){
   const period=t.period/(difficulty==="hard"?1.2:difficulty==="easy"?0.88:1);
   const active=t.active*(difficulty==="hard"?1.18:difficulty==="easy"?0.78:1);
   if(t.laserOn){timerLabel="LASER TẮT: "+Math.max(0,(active-t.laserPhase)).toFixed(1)+"s";timerColor="#ff657f";}
   else {timerLabel="LASER SAU: "+Math.max(0,(period-t.laserPhase)).toFixed(1)+"s";timerColor="#ffd166";}
   timerY=(t.bouncy?t.y:(t.points&&t.points.length?t.points[0][1]:240))- (t.bouncy?((t.radius||42)+24):27);
  }
  if(timerLabel){
   ctx.save();ctx.font="bold 11px Courier New, monospace";ctx.textAlign="center";
   const tw=ctx.measureText(timerLabel).width, bw=tw+14, bh=19;
   timerX=Math.max(bw/2+2,Math.min(W-bw/2-2,timerX));timerY=Math.max(15,Math.min(H-24,timerY));
   ctx.fillStyle="#080a10";ctx.globalAlpha=.88;ctx.fillRect(timerX-bw/2,timerY-bh/2,bw,bh);ctx.globalAlpha=1;
   ctx.strokeStyle=timerColor;ctx.lineWidth=1;ctx.strokeRect(timerX-bw/2,timerY-bh/2,bw,bh);
   ctx.fillStyle=timerColor;ctx.fillText(timerLabel,timerX,timerY+4);ctx.restore();
  }
 });
 // Checkpoint shrines: lit when active, dormant otherwise.
 (world.checkpoints||[]).forEach(cp=>{
  const cx=cp.x-cam, cy=cp.y-24, active=activeCheckpoint.label===cp.label;
  glow(cx+12,cy+18,active?44:25,active?"#5eead4":"#8b7aa8",active?.42:.16);
  rect(cx+2,cy+12,20,23,active?"#276c68":"#393444");rect(cx+6,cy+5,12,9,active?"#8cf5dc":"#777083");
  rect(cx+9,cy+8,6,13,active?"#d7fff2":"#a9a0b8");
  if(active){ctx.strokeStyle="#a7fff0";ctx.lineWidth=2;ctx.beginPath();ctx.arc(cx+12,cy+16,18+Math.sin(performance.now()/160)*2,0,Math.PI*2);ctx.stroke();}
 });
 // Exit portal
 const gx=world.goal-cam, gy=world.ground-69, pulse=.7+.3*Math.sin(performance.now()/190);
 glow(gx+16,gy+38,65,"#a855f7",pulse);rect(gx-5,gy-4,42,73,"#4b2d70");rect(gx,gy,32,65,"#9b5de5");rect(gx+5,gy+5,22,55,"#201532");
 ctx.strokeStyle="#e9c8ff";ctx.lineWidth=3;ctx.strokeRect(gx+4,gy+3,24,59);rect(gx+10,gy+13,4,4,"#f3d7ff");rect(gx+20,gy+30,4,4,"#f3d7ff");
 // coins: glowing gold pixel coins
 coinsList.forEach(c=>{if(c.taken)return;let wob=Math.sin(performance.now()/180+c.x)*3,x=c.x-cam,y=c.y+wob;glow(x,y,23,"#fbbf24",.3);rect(x-6,y-8,12,16,"#e9a52e");rect(x-4,y-10,8,2,"#ffe8a1");rect(x-4,y-6,8,12,"#ffdc69");rect(x-1,y-5,3,10,"#fff4bc");rect(x-6,y+7,12,2,"#b87920");});
   // Enemy archetypes: archers with a drawn bow, and heavy tankers in plated armor.
  enemies.forEach(e=>{
   if(!e.alive)return;
   const x=e.x-cam,y=e.y,t=performance.now()*.012+e.home;
   const walk=Math.sin(t)*2.1, flash=e.flash>0;
   ctx.globalAlpha=.32;rect(x-3,world.ground-3,e.w+6,4,"#000");ctx.globalAlpha=1;
   if(e.type==="archer"){
    glow(x+13,y+13,34,"#fb456c",.18);
    // Ragged hood and thin, agile silhouette.
    ctx.fillStyle="#171522";ctx.beginPath();ctx.moveTo(x+3,y+7);ctx.lineTo(x+13,y-1);ctx.lineTo(x+23,y+7);ctx.lineTo(x+22,y+24);ctx.lineTo(x+17,y+30);ctx.lineTo(x+7,y+30);ctx.lineTo(x+2,y+22);ctx.closePath();ctx.fill();
    rect(x+5,y+5,15,12,flash?"#fff":"#5a526e");rect(x+6,y+10,4,4,"#ff536f");rect(x+15,y+10,4,4,"#ff536f");
    rect(x+6,y+18,14,9,"#343044");rect(x+7,y+27,5,4+walk,"#272334");rect(x+15,y+27,5,4-walk,"#272334");
    // Bow and nocked arrow, pointed toward the player.
    const face=player.x>e.x?1:-1,bx=x+13+face*8;
    ctx.strokeStyle="#c9a46a";ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(bx,y+8);ctx.quadraticCurveTo(bx+face*8,y+16,bx,y+25);ctx.stroke();
    ctx.strokeStyle="#e9d5a5";ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(bx,y+8);ctx.lineTo(bx,y+25);ctx.stroke();
    rect(bx+face*1,y+15,face*8,2,"#f0d7a0");rect(bx+face*8,y+13,face*3,2,"#fff1c2");
    glow(x+13,y+13,13,"#ff536f",.32);
   }else{
    // Heavy tanker: broad shoulders, iron helmet, reinforced chest and massive boots.
    glow(x+17,y+19,44,"#f97316",.18);
    ctx.fillStyle="#201a20";ctx.beginPath();ctx.moveTo(x+3,y+11);ctx.lineTo(x+6,y+2);ctx.lineTo(x+27,y+2);ctx.lineTo(x+32,y+12);ctx.lineTo(x+31,y+32);ctx.lineTo(x+25,y+38);ctx.lineTo(x+7,y+38);ctx.lineTo(x+1,y+31);ctx.closePath();ctx.fill();
    rect(x+7,y+4,20,13,flash?"#fff":"#6f625d");rect(x+5,y+9,24,7,"#9a8877");rect(x+9,y+12,5,4,"#ffb15c");rect(x+20,y+12,5,4,"#ffb15c");
    glow(x+11,y+14,12,"#fb923c",.55);glow(x+22,y+14,12,"#fb923c",.55);
    rect(x+4,y+18,27,13,flash?"#fff":"#5b4a45");rect(x+1,y+18,10,10,"#8b7768");rect(x+24,y+18,10,10,"#8b7768");
    rect(x+9,y+20,16,3,"#c4b5a5");rect(x+11,y+25,12,3,"#2c2528");
    rect(x+7,y+30,8,6+walk*.35,"#43363a");rect(x+20,y+30,8,6-walk*.35,"#43363a");
    rect(x+4,y+35+walk*.2,12,3,"#a18a78");rect(x+19,y+35-walk*.2,12,3,"#a18a78");
    // Shoulder spikes and a glowing chest sigil.
    for(let i=0;i<3;i++){ctx.fillStyle="#c4a78b";ctx.beginPath();ctx.moveTo(x+3+i*4,y+19);ctx.lineTo(x+5+i*4,y+13);ctx.lineTo(x+8+i*4,y+19);ctx.fill();}
    rect(x+16,y+22,4,5,"#fb923c");glow(x+18,y+24,12,"#fb923c",.4);
    if(e.charging>0){glow(x+17,y+25,45,"#fb923c",.25);rect(x-4,y+34,4,3,"#fb923c");rect(x+e.w,y+32,5,3,"#fb923c");}
  }
  });
  // Glowing arrows have a warm trail and a sharp metal tip.
  enemyArrows.forEach(a=>{
   const x=a.x-cam,y=a.y;
   ctx.save();ctx.translate(x,y);ctx.rotate(a.angle||0);
   glow(0,0,15,"#fb923c",.24);
   ctx.strokeStyle="#f6c77b";ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(-13,0);ctx.lineTo(7,0);ctx.stroke();
   ctx.fillStyle="#fff1c2";ctx.beginPath();ctx.moveTo(11,0);ctx.lineTo(4,-3);ctx.lineTo(4,3);ctx.closePath();ctx.fill();
   rect(-13,-2,4,4,"#b45309");ctx.restore();
  });
  // Boss: armored silhouette, animated crown, spectral mantle, chest rune and orbiting runes.
  if(boss&&boss.alive){
   const x=boss.x-cam,y=boss.y,t=performance.now()*.001,hover=Math.sin(t*2.4)*3,flash=boss.flash>0;
   ctx.globalAlpha=.4;rect(x-8,world.ground-4,78,5,"#000");ctx.globalAlpha=1;
   glow(x+31,y+37+hover,100,"#d946ef",.24+.05*Math.sin(t*3));
   ctx.fillStyle="#21152f";ctx.beginPath();ctx.moveTo(x+10,y+20+hover);ctx.lineTo(x+52,y+20+hover);ctx.lineTo(x+62,y+69);ctx.lineTo(x+49,y+62);ctx.lineTo(x+39,y+77);ctx.lineTo(x+29,y+66);ctx.lineTo(x+14,y+76);ctx.lineTo(x+5,y+61);ctx.closePath();ctx.fill();
   rect(x+8,y+17+hover,46,48,flash?"#ffd2e1":"#492650");rect(x+2,y+29+hover,58,32,flash?"#ffd2e1":"#281b3d");rect(x+12,y+5+hover,38,23,flash?"#ffd2e1":"#70366f");
   for(let i=0;i<5;i++){const cx=x+9+i*10;ctx.fillStyle=i%2?"#8d4b91":"#b45a9f";ctx.beginPath();ctx.moveTo(cx,y+8+hover);ctx.lineTo(cx+5,y-7-(i%2)*5+hover);ctx.lineTo(cx+10,y+8+hover);ctx.closePath();ctx.fill();rect(cx+4,y-5-(i%2)*5+hover,2,4,"#f0abfc");}
   rect(x+12,y+10+hover,38,14,"#201329");rect(x+15,y+15+hover,10,6,flash?"#fff":"#ff426f");rect(x+37,y+15+hover,10,6,flash?"#fff":"#ff426f");
   glow(x+20,y+18+hover,18,"#fb376b",.72);glow(x+42,y+18+hover,18,"#fb376b",.72);
   rect(x+26,y+36+hover,10,15,"#8c4b91");rect(x+29,y+39+hover,4,9,"#f0abfc");glow(x+31,y+44+hover,22,"#d946ef",.4);
   rect(x+2,y+28+hover,13,13,flash?"#ffd2e1":"#8c4b91");rect(x+47,y+28+hover,13,13,flash?"#ffd2e1":"#8c4b91");
   rect(x+6,y+39+hover,8,15,"#32213f");rect(x+48,y+39+hover,8,15,"#32213f");rect(x+7,y+62,14,12,"#191627");rect(x+42,y+62,14,12,"#191627");
   for(let i=0;i<3;i++){const a=t*1.7+i*Math.PI*2/3,rx=x+31+Math.cos(a)*43,ry=y+37+Math.sin(a)*27;glow(rx,ry,12,"#d8b4fe",.25);rect(rx-2,ry-2,4,4,"#e9d5ff");}
  }
// Animated boss projectiles, with a bright core and warning halo.
  bossProjectiles.forEach(p=>{const x=p.x-cam,pulse=1+.18*Math.sin(performance.now()*.02+p.x);glow(x,p.y,30,"#d946ef",.48);glow(x,p.y,14,"#f0abfc",.42);rect(x-p.r*pulse,p.y-p.r*pulse,p.r*2*pulse,p.r*2*pulse,"#8b2ba8");rect(x-3,p.y-3,6,6,"#ffe4ff");rect(x-12,p.y+4,4,3,"#c084fc");rect(x+8,p.y-7,3,3,"#f5d0fe");});
 if(checkpointNotice>0){
  ctx.save();ctx.globalAlpha=Math.min(1,checkpointNotice);rect(W/2-155,54,310,30,"#0b1a1a");ctx.strokeStyle="#5eead4";ctx.strokeRect(W/2-155,54,310,30);text("✦ CHECKPOINT: "+activeCheckpoint.label.toUpperCase()+" ✦",W/2,74,12,"#a7fff0","center");ctx.restore();
 }
   // Cinematic player sprite: animated cape, articulated limbs, armor highlights and sword trails.
  const px=player.x-cam, py=player.y, moving=player.grounded&&Math.abs(player.vx)>20, airborne=!player.grounded;
  const speedRatio=Math.min(1,Math.abs(player.vx)/240),runPhase=player.anim*1.55;
  const stride=moving?Math.sin(runPhase)*4:0,bob=moving?Math.abs(Math.sin(runPhase))*1.5:airborne?-2:Math.sin(performance.now()*.003)*.7;
  const attackProgress=attackTimer>0?1-Math.min(1,attackTimer/.22):0,face=player.face||1,fx=px+12,fy=py+18+bob;
  const shadowScale=Math.max(.35,1-Math.max(0,world.ground-(py+player.h))/210);
  ctx.globalAlpha=.32*shadowScale;ctx.beginPath();ctx.ellipse(fx,Math.min(world.ground-2,py+player.h+5),17*shadowScale,4*shadowScale,0,0,Math.PI*2);ctx.fillStyle="#000";ctx.fill();ctx.globalAlpha=1;
  glow(fx,fy,airborne?43:38,"#6d75ff",.12+speedRatio*.08+(attackTimer>0?.2:0));glow(fx,Math.min(world.ground-4,py+player.h),25,"#5ee9d2",.08);
  if(speedRatio>.72&&Math.floor(performance.now()/65)%2===0){ctx.globalAlpha=.16;rect(px-face*7,py+5,player.w,player.h,"#8b9cff");ctx.globalAlpha=1;}
  ctx.save();ctx.translate(fx,0);ctx.scale(face,1);ctx.translate(-fx,0);
  const bx=px,by=py+bob,capeWave=Math.sin(performance.now()*.012+player.vx*.01)*3+Math.min(5,Math.abs(player.vx)*.018);
  if(invuln>0&&Math.floor(performance.now()/65)%2===0)ctx.globalAlpha=.42;
  ctx.fillStyle="#24142f";ctx.beginPath();ctx.moveTo(bx+6,by+9);ctx.lineTo(bx+18,by+11);ctx.lineTo(bx+23+capeWave,by+23);ctx.lineTo(bx+17+capeWave,by+21);ctx.lineTo(bx+14+capeWave,by+31);ctx.lineTo(bx+9,by+25);ctx.lineTo(bx+3+capeWave*.5,by+28);ctx.closePath();ctx.fill();
  rect(bx+7,by+12,9,14,"#5c2879");rect(bx+9,by+14,6,10,"#9b3f9b");
  rect(bx+1,by+16+stride*.25,5,10,"#202940");rect(bx+1,by+15+stride*.25,6,5,"#697b9d");
  const legA=airborne?-2:stride,legB=airborne?3:-stride;
  rect(bx+5,by+26,6,7+legA*.45,"#667895");rect(bx+14,by+26,6,7+legB*.45,"#667895");
  rect(bx+2,by+31+legA*.45,9,3,"#20273d");rect(bx+13,by+31+legB*.45,9,3,"#20273d");
  rect(bx+4,by+29+legA*.35,6,2,"#a4b6d1");rect(bx+14,by+29+legB*.35,6,2,"#a4b6d1");
  rect(bx+4,by+12,16,15,"#202940");rect(bx+3,by+14,5,10,"#414f70");rect(bx+16,by+14,6,10,"#414f70");
  rect(bx+6,by+13,12,12,"#526482");rect(bx+7,by+14,10,3,"#8494b2");rect(bx+8,by+18,8,2,"#29364e");rect(bx+10,by+19,4,4,"#8be9ff");glow(bx+12,by+21,11,"#5ee7ff",.34);
  rect(bx+5,by+25,14,3,"#d4a65b");rect(bx+10,by+25,4,3,"#fff0ad");rect(bx+8,by+8,8,6,"#a0a8bd");
  rect(bx+4,by+1,16,10,"#22283d");rect(bx+2,by+4,20,8,"#414b6b");rect(bx+5,by+2,14,3,"#a7b4d0");rect(bx+4,by+5,3,5,"#7786a5");
  rect(bx+5,by+8,14,4,"#151a2b");rect(bx+7,by+8,10,2,"#0b101b");rect(bx+14,by+7,5,3,"#79e7ff");glow(bx+16,by+8,13,"#5ee7ff",.62);
  const slash=attackTimer>0?Math.sin(attackProgress*Math.PI):0;rect(bx+17,by+15-slash*2,5,9,"#293650");rect(bx+17,by+14-slash*2,7,5,"#7b8ca9");
  ctx.save();ctx.translate(bx+20,by+20);ctx.rotate(attackTimer>0?(-.95+attackProgress*1.95):-.45);
  glow(9,0,attackTimer>0?31:15,attackTimer>0?"#8be9ff":"#a7b8d5",attackTimer>0?.5:.13);
  rect(0,-2,25,4,"#cbd5e1");rect(4,-1,18,2,"#f8fafc");rect(21,-2,5,4,"#8be9ff");rect(-4,-4,4,8,"#d4a65b");rect(-8,-2,5,4,"#76513a");rect(-10,-3,3,6,"#d4a65b");ctx.restore();ctx.restore();
  if(invuln>0)ctx.globalAlpha=1;
  if(attackTimer>0){const sx=px+(face>0?22:-22),sy=py+13+bob;ctx.save();ctx.globalAlpha=.8;ctx.strokeStyle="#8be9ff";ctx.lineWidth=4;ctx.beginPath();ctx.arc(px+12,sy+3,27,face>0?-1.15+attackProgress*.45:.05+attackProgress*.3,face>0?.85+attackProgress*.45:2.1+attackProgress*.3);ctx.stroke();ctx.strokeStyle="#f0fdff";ctx.lineWidth=1.5;ctx.beginPath();ctx.arc(px+12,sy+3,30,face>0?-1.05+attackProgress*.45:.15+attackProgress*.3,face>0?.75+attackProgress*.45:2+attackProgress*.3);ctx.stroke();glow(sx+7,sy+3,31,"#8be9ff",.38);for(let i=0;i<5;i++){const a=attackProgress*5+i*1.1;rect(sx+Math.cos(a)*14,sy+Math.sin(a)*12,2,2,i%2?"#fff":"#8be9ff");}ctx.restore();}
  if(moving&&Math.floor(performance.now()/85)%3===0){const dx=px+(face<0?player.w+2:-3),dy=py+player.h-3;glow(dx,dy,9,"#a5b4fc",.16);rect(dx,dy,3,2,"#a5b4fc");}
// floating particles
 particles.forEach(p=>{glow(p.x-cam,p.y,12,p.color,.16);rect(p.x-cam,p.y,4,4,p.color);});
}
function draw(){
 const cam=Math.max(0,Math.min(world.length-W,player.x-W*.38));
 ctx.save();
 if(shake>0)ctx.translate((Math.random()-.5)*8,(Math.random()-.5)*6);
 drawBackground(cam);drawWorld(cam);
 // Foreground fog rolls across the ground in layered translucent ribbons.
 ctx.save();
 for(let i=0;i<7;i++){
  const fx=((i*190-performance.now()*.022*(i%2?1:-.65))%(W+300)+W+300)%(W+300)-150;
  const fy=world.ground-15+(i%3)*13;
  const fog=ctx.createRadialGradient(fx,fy,3,fx,fy,150);
  fog.addColorStop(0,"rgba(164,174,220,0.12)");
  fog.addColorStop(1,"rgba(100,110,170,0)");
  ctx.fillStyle=fog;ctx.fillRect(fx-150,fy-35,300,100);
 }
 // Dark vignette directs the eye toward the player and action.
 const vignette=ctx.createRadialGradient(W*.5,H*.45,110,W*.5,H*.48,590);
 vignette.addColorStop(0,"rgba(0,0,0,0)");
 vignette.addColorStop(.7,"rgba(2,3,10,0.12)");
 vignette.addColorStop(1,"rgba(1,2,7,0.68)");
 ctx.fillStyle=vignette;ctx.fillRect(0,0,W,H);
   // Sparse drifting ash particles add depth without external image assets.
  const ashTime=performance.now()*.018;for(let i=0;i<34;i++){const ax=(i*83+ashTime*(i%3+1))%(W-12)+6,ay=(i*47+Math.sin(ashTime*.04+i)*9)%(H-20)+8;ctx.globalAlpha=.08+(i%4)*.025;rect(ax,ay,i%7===0?2:1,i%7===0?2:1,i%3===0?"#d8c5ff":"#b7c1d9");}ctx.globalAlpha=1;
  // Subtle edge highlights make the scene feel framed like a dark-fantasy game.
 ctx.strokeStyle="rgba(204,176,125,0.24)";ctx.lineWidth=2;ctx.strokeRect(5,5,W-10,H-10);
 ctx.restore();
 ctx.restore();
 // overlay
 if(world.boss && boss && boss.alive){
  rect(W/2-158,14,316,23,"#080914");rect(W/2-154,18,308,15,"#34213e");rect(W/2-151,21,302*(boss.hp/boss.maxHp),9,"#e34b80");
  rect(W/2-151,21,302*(boss.hp/boss.maxHp),3,"#ffb2d1");text("✦ THE VOID KEEPER ✦",W/2,11,11,"#f7c8ff","center");
 }
 if(gameOver||victory){
  rect(0,0,W,H,"rgba(5,6,17,.82)");glow(W/2,H/2,210,victory?"#a855f7":"#e11d48",.22);
  rect(W/2-235,H/2-88,470,178,"#171428");rect(W/2-231,H/2-84,462,170,"#28203c");rect(W/2-225,H/2-78,450,158,"#100f20");
  rect(W/2-205,H/2-60,410,2,victory?"#d8b4fe":"#fb7185");
  text(victory?"✦ SHADOWS DEFEATED ✦":"☠ YOU HAVE FALLEN ☠",W/2,H/2-24,24,victory?"#e9d5ff":"#ff8ba5","center");
  text("Điểm: "+score+"     •     Xu: "+coins,W/2,H/2+14,17,"#f6eaff","center");
  text("NHẤN R ĐỂ CHƠI LẠI",W/2,H/2+52,13,"#b8c5e8","center");
 }
 document.getElementById("healthbar").style.width=(Math.max(0,player.hp)/player.maxHp*100)+"%";
 document.getElementById("hptext").textContent=Math.max(0,player.hp)+" / "+player.maxHp;
 document.getElementById("staminabar").style.width=(100-Math.min(100,Math.abs(player.vx)/220*18+(attackTimer>0?22:0)))+"%";
 document.getElementById("coins").textContent=(godMode?"◈ ∞":"◈ "+coins)+"  ·  "+score;
 document.getElementById("level").textContent=["I","II","III"][levelIndex]+" · "+world.name;

}
// Vòng lặp tối ưu: giới hạn khoảng 40 FPS để giảm tải khi vẽ nhiều hiệu ứng.
let lastFrameTime=0, lastBestSavedState="";
const FRAME_INTERVAL=1000/40;
function loop(t){
 if(document.hidden){
  lastTime=0;lastFrameTime=0;
  requestAnimationFrame(loop);
  return;
 }
 if(lastFrameTime && t-lastFrameTime<FRAME_INTERVAL){
  requestAnimationFrame(loop);
  return;
 }
 const dt=lastTime?(t-lastTime)/1000:0;
 lastTime=t;lastFrameTime=t;
 update(Math.min(dt,.033));
 draw();
 // Chỉ lưu kỷ lục một lần khi trạng thái thua/thắng thay đổi, không ghi bộ nhớ mỗi khung hình.
 if(gameOver||victory){
  const resultKey=(victory?"victory":"gameover")+":"+score;
  if(resultKey!==lastBestSavedState){
   saveBest();
   lastBestSavedState=resultKey;
  }
 }
 requestAnimationFrame(loop);
}
document.addEventListener("visibilitychange",()=>{lastTime=0;lastFrameTime=0;});
requestAnimationFrame(loop);
document.querySelectorAll(".diff-btn").forEach(btn=>btn.addEventListener("click",()=>{difficulty=btn.dataset.diff;document.querySelectorAll(".diff-btn").forEach(b=>b.classList.toggle("active",b===btn));document.getElementById("diffdesc").textContent=difficultySettings[difficulty].desc;makeWorld(levelIndex); }));
document.getElementById("startbtn").addEventListener("click",()=>{score=0;coins=0;levelIndex=0;shopUpgrades={hp:0,damage:0,speed:0};makeWorld(0);started=true;document.getElementById("mainmenu").style.display="none";canvas.focus();persistCheckpoint();beep(330,.08,"triangle",.025);});
document.getElementById("resumebtn").addEventListener("click",resumeCheckpoint);
document.querySelectorAll(".buy-btn").forEach(btn=>btn.addEventListener("click",()=>buyItem(btn.dataset.item)));
document.getElementById("continuebtn").addEventListener("click",()=>{
 shopOpen=false;document.getElementById("shopmenu").style.display="none";
 makeWorld(levelIndex);player.hp=player.maxHp;started=true;persistCheckpoint();canvas.focus();beep(420,.08,"triangle",.03);
});
canvas.addEventListener("pointerdown",()=>{canvas.focus();});
// Touch controls use pointer events so they work on phones, tablets, and desktop testing.
function releaseTouchButtons(){document.querySelectorAll("[data-touch]").forEach(btn=>{keys[btn.dataset.touch]=false;btn.classList.remove("pressed");});}
document.querySelectorAll("[data-touch]").forEach(btn=>{
 const key=btn.dataset.touch;
 const press=e=>{e.preventDefault();keys[key]=true;btn.classList.add("pressed");if(key==="j")attack();};
 const release=e=>{e.preventDefault();keys[key]=false;btn.classList.remove("pressed");};
 btn.addEventListener("pointerdown",press);btn.addEventListener("pointerup",release);btn.addEventListener("pointercancel",release);btn.addEventListener("lostpointercapture",release);
});
window.addEventListener("blur",releaseTouchButtons);
window.addEventListener("keydown",e=>{
 const k=e.key;
 // Bí mật: gõ lần lượt /67 để bật bất tử và vô hạn vàng.
 if(k.length===1){cheatBuffer=(cheatBuffer+k).slice(-3);}
 if(cheatBuffer.endsWith("/67")){
  godMode=!godMode;coins=godMode?INFINITE_COINS:Math.min(coins,INFINITE_COINS);
  if(player){player.hp=player.maxHp;invuln=0;}
  document.getElementById("save-message").textContent= (godMode?"✦ CHEAT ĐÃ BẬT: BẤT TỬ + VÔ HẠN VÀNG. Gõ /67 lần nữa để tắt.":"Cheat đã tắt. Máu có thể giảm trở lại.");
  if(shopOpen){shopMessage="Mật mã bí mật đã kích hoạt! Mua hàng miễn phí.";updateShopUI();}
  beep(980,.16,"triangle",.06);cheatBuffer="";
 }
 if(k==="Escape")cheatBuffer="";
 if(["ArrowLeft","ArrowRight","ArrowUp"," ","ArrowDown","/"].includes(k))e.preventDefault();
 keys[k]=true;
 if(k==="j"||k==="J")attack();
 if(k==="m"||k==="M"){audioOn=!audioOn;beep(500,.06);}
 if((k==="r"||k==="R")&&gameOver)retryFromCheckpoint();
 if((k==="r"||k==="R")&&victory)resetGame();
});
window.addEventListener("keyup",e=>{keys[e.key]=false;});
refreshSaveSlots();
canvas.focus();
})();
</script>
</body>
</html>
"""

components.html(game_html, height=820, scrolling=False)

st.markdown("---")
st.subheader("🕹️ Shadowbound — Bản nâng cấp đồ họa")
st.markdown(
    """
    - Vượt qua 3 khu vực: **Rừng Tàn**, **Hầm Ngục** và **Đấu Trường**. Có thêm **Cung Thủ Bóng Tối** bắn tên và **Tanker Thiết Giáp** nhảy lên bệ cao, lao tới húc đẩy người chơi.
    - Thu thập xu, tránh hố, gai, **đá lăn** và **bẫy phun lửa**; mỗi bẫy gây sát thương khác nhau.
    - Đánh bại boss ở màn cuối để chiến thắng.
    - Hiệu ứng nâng cấp: cực quang, tia trăng, sương mù chuyển động, tro bay, linh hồn bay, rễ cây tiền cảnh, nấm phát sáng, cổ tự trên nền đá và viền điện ảnh. Nhân vật có hoạt ảnh chạy/nhảy, áo choàng động, kiếm luôn hiển thị, đường chém phát sáng, bụi chân và hiệu ứng tiếp đất.
    - Có checkpoint tự lưu và nút tiếp tục từ checkpoint; nhấn R sau khi thất bại để hồi sinh tại điểm gần nhất.
    - Boss có đạn linh hồn, tăng tốc độ tấn công khi còn dưới nửa máu.
    - Có nút cảm ứng cho điện thoại/tablet; giữ nguyên điều khiển bàn phím trên máy tính.
    - Có 3 ô lưu thủ công riêng cho từng màn; dữ liệu lưu trong trình duyệt trên thiết bị hiện tại, chưa đồng bộ giữa nhiều máy.
    - Đồ họa pixel, bẫy, hiệu ứng và âm thanh được tạo bằng Canvas/Web Audio nên không cần tải asset ngoài.
    """
)
