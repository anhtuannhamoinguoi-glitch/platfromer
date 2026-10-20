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
    .stApp { background: #0b1018; color: #e8edf5; }
    h1, h2, h3 { color: #e8edf5 !important; }
    [data-testid="stMarkdownContainer"] p { color: #c4cedb; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🌑 SHADOWBOUND")
st.caption("Platformer 2D Pixel Art • Sinh tồn trong bóng tối")
st.markdown(
    """
    **Cách chơi:** bấm vào khung game để điều khiển bằng bàn phím.
    **A/D** hoặc **←/→**: chạy · **W**, **↑** hoặc **Space**: nhảy ·
    **J**: tấn công · **M**: bật/tắt âm thanh · **R**: chơi lại khi thua.
    """
)

game_html = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
*{box-sizing:border-box}
html,body{margin:0;background:#080d14;color:#e9eef7;font-family:monospace}
.wrap{width:100%;max-width:1000px;margin:auto}
canvas{display:block;width:100%;height:auto;background:#101927;border:2px solid #354258;image-rendering:pixelated;outline:none}
.hud{display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:space-between;padding:8px 2px;color:#dbe5f4;font-size:13px}
.pill{background:#182334;border:1px solid #354258;border-radius:5px;padding:6px 9px}
.hint{font-size:12px;color:#94a5bd;padding:2px 0 8px}
</style>
</head>
<body>
<div class="wrap">
  <div class="hud">
    <span class="pill" id="health">♥ ♥ ♥</span>
    <span class="pill" id="coins">Xu: 0</span>
    <span class="pill" id="level">Màn: 1 / 3</span>
    <span class="pill" id="best">Kỷ lục: 0</span>
    <span class="pill" id="sound">Âm thanh: bật (M)</span>
  </div>
  <canvas id="game" width="960" height="540" tabindex="0" aria-label="Game Shadowbound"></canvas>
  <div class="hint">Mẹo: đứng trên đầu quái vật để hạ nó hoặc nhấn J để tấn công gần. Tìm cổng phát sáng để sang màn tiếp theo.</div>
</div>
<script>
(() => {
"use strict";
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
ctx.imageSmoothingEnabled = false;
const W = canvas.width, H = canvas.height;
const keys = {};
let audioOn = true, audioCtx = null, lastTime = 0, gameOver = false, victory = false;
let score = 0, coins = 0, levelIndex = 0, attackTimer = 0, invuln = 0, shake = 0;
let best = 0;
try { best = Number(localStorage.getItem("shadowbound_best") || 0); } catch(e) {}
const bestEl = document.getElementById("best");
bestEl.textContent = "Kỷ lục: " + best;

const levels = [
 {name:"Rừng Tàn", length:2300, start:70, goal:2180, ground:430,
  platforms:[[250,360,120],[470,310,120],[710,370,140],[960,320,120],[1210,360,140],[1490,300,130],[1770,350,130]],
  pits:[[390,455],[630,690],[880,930],[1110,1160],[1390,1440],[1660,1710],[1950,2010]],
  coinSpots:[[180,380],[290,315],[520,265],[760,325],[1010,275],[1260,315],[1540,255],[1810,305],[2050,385]],
  enemies:[330,780,1040,1570,1870], boss:false},
 {name:"Hầm Ngục", length:2600, start:70, goal:2470, ground:430,
  platforms:[[210,350,120],[430,300,130],[680,350,120],[900,285,130],[1160,340,140],[1430,290,130],[1680,350,130],[1940,280,130],[2190,340,120]],
  pits:[[360,410],[620,670],[850,890],[1100,1150],[1390,1420],[1640,1670],[1900,1930],[2150,2180]],
  coinSpots:[[150,380],[250,305],[470,255],[720,305],[950,240],[1200,295],[1480,245],[1730,305],[1990,235],[2250,295]],
  enemies:[300,740,1020,1510,1810,2250], boss:false},
 {name:"Đấu Trường", length:1800, start:70, goal:1680, ground:430,
  platforms:[[280,350,130],[540,300,130],[800,350,140],[1080,300,130],[1350,350,130]],
  pits:[[430,480],[700,750],[970,1020],[1240,1290]],
  coinSpots:[[180,380],[330,305],[590,255],[850,305],[1130,255],[1400,305],[1580,385]],
  enemies:[350,880], boss:true}
];
let world, player, enemies, coinsList, particles, boss;

function makeWorld(index) {
 const d = levels[index];
 world = d;
 player = {x:d.start,y:350,w:24,h:34,vx:0,vy:0,grounded:false,face:1,hp:3,anim:0};
 enemies = d.enemies.map((x,i)=>({x,y:390,w:26,h:30,vx:(i%2?1:-1)*55,alive:true,home:x,range:75,hp:1}));
 coinsList = d.coinSpots.map(([x,y])=>({x,y,r:8,taken:false}));
 particles = [];
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
function damage(){
 if(invuln>0 || gameOver || victory) return;
 player.hp--; invuln=1.25; shake=.25; noiseHit(); addParticles(player.x+12,player.y+15,"#ff657a",12);
 if(player.hp<=0){gameOver=true; beep(90,.5,"sawtooth",.06);}
}
function attack(){
 if(attackTimer>0 || gameOver || victory) return;
 attackTimer=.22; beep(240,.07,"square",.04);
 const range={x:player.face>0?player.x+player.w:player.x-28,y:player.y+5,w:30,h:25};
 enemies.forEach(e=>{if(e.alive && hit(range,e)){e.alive=false;score+=100;addParticles(e.x+13,e.y+12,"#a9c6d9",12);beep(620,.09);}});
 if(boss && boss.alive && hit(range,boss)){boss.hp--;boss.flash=.18;score+=25;addParticles(boss.x+boss.w/2,boss.y+25,"#fca5a5",8);beep(170,.08,"sawtooth",.05);if(boss.hp<=0){boss.alive=false;score+=1000;addParticles(boss.x+30,boss.y+30,"#e879f9",30);}}
}
function resetGame(){score=0;coins=0;levelIndex=0;makeWorld(0);beep(500,.08);}
function nextLevel(){
 if(levelIndex<levels.length-1){levelIndex++;makeWorld(levelIndex);beep(700,.1);setTimeout(()=>beep(900,.1),110);}
 else {victory=true;score+=500;saveBest();}
}
function saveBest(){
 best=Math.max(best,score);
 try{localStorage.setItem("shadowbound_best",String(best));}catch(e){}
 bestEl.textContent="Kỷ lục: "+best;
}
function update(dt){
 if(gameOver||victory) return;
 dt=Math.min(dt,.033);
 player.anim+=dt*10; attackTimer=Math.max(0,attackTimer-dt); invuln=Math.max(0,invuln-dt); shake=Math.max(0,shake-dt);
 const left=keys["ArrowLeft"]||keys["a"]||keys["A"], right=keys["ArrowRight"]||keys["d"]||keys["D"];
 const jump=keys[" "]||keys["ArrowUp"]||keys["w"]||keys["W"];
 const speed=220, accel=1500;
 if(left){player.vx-=accel*dt;player.face=-1;} if(right){player.vx+=accel*dt;player.face=1;}
 if(!left&&!right) player.vx*=Math.pow(.0008,dt);
 player.vx=Math.max(-speed,Math.min(speed,player.vx));
 if(jump && player.grounded){player.vy=-470;player.grounded=false;beep(360,.07,"square",.025);}
 player.vy+=1150*dt; player.vy=Math.min(player.vy,700);
 // horizontal movement and world boundaries
 player.x+=player.vx*dt; player.x=Math.max(0,Math.min(world.length-player.w,player.x));
 // collide with platforms while falling
 const oldY=player.y; player.y+=player.vy*dt; player.grounded=false;
 const floor=floorAt(player.x+player.w/2);
 if(player.y+player.h>=floor && oldY+player.h<=floor+14 && floor<H+50){player.y=floor-player.h;player.vy=0;player.grounded=true;}
 for(const p of platforms()){
  if(player.vy>=0 && oldY+player.h<=p.y+5 && player.y+player.h>=p.y && player.x+player.w>p.x && player.x<p.x+p.w){
   player.y=p.y-player.h;player.vy=0;player.grounded=true;
  }
 }
 if(player.y>H+80){damage();if(player.hp>0){player.x=Math.max(40,player.x-120);player.y=250;player.vy=0;}}
 // collect coins
 coinsList.forEach(c=>{if(!c.taken && Math.abs((player.x+player.w/2)-c.x)<22 && Math.abs((player.y+player.h/2)-c.y)<25){c.taken=true;coins++;score+=10;beep(800,.06,"sine",.035);addParticles(c.x,c.y,"#ffd166",7);}});
 // enemies
 enemies.forEach(e=>{
  if(!e.alive)return;
  e.x+=e.vx*dt;
  if(Math.abs(e.x-e.home)>e.range)e.vx*=-1;
  const eb={x:e.x,y:e.y,w:e.w,h:e.h};
  if(hit(player,eb)){
   if(player.vy>80 && oldY+player.h<e.y+12){e.alive=false;player.vy=-300;score+=100;addParticles(e.x,e.y,"#a9c6d9",10);beep(500,.07);}
   else damage();
  }
 });
 if(boss && boss.alive){
  boss.x+=boss.vx*dt;
  if(boss.x<1150||boss.x>1550)boss.vx*=-1;
  boss.flash=Math.max(0,boss.flash-dt);
  boss.attack+=dt;
  if(hit(player,boss)){if(player.vy>90 && oldY+player.h<boss.y+18){boss.hp--;player.vy=-330;boss.flash=.2;score+=25;beep(190,.08,"sawtooth");if(boss.hp<=0){boss.alive=false;score+=1000;}}else damage();}
 }
 // exit
 if(player.x+player.w>world.goal && (!world.boss || !boss.alive)) nextLevel();
 particles=particles.filter(p=>p.life>0);
 particles.forEach(p=>{p.x+=p.vx*dt;p.y+=p.vy*dt;p.vy+=350*dt;p.life-=dt;});
}

function drawBackground(cam){
 rect(0,0,W,H,"#101927");
 // moon
 ctx.fillStyle="#c5d0db";ctx.beginPath();ctx.arc(790-cam*.08,92,34,0,Math.PI*2);ctx.fill();
 ctx.fillStyle="#101927";ctx.beginPath();ctx.arc(804-cam*.08,80,31,0,Math.PI*2);ctx.fill();
 // stars
 for(let i=0;i<55;i++){let x=((i*173)%W-cam*.12+W)%W,y=(i*71)%220;rect(x,y,2,2,"#8999b5");}
 // far mountains
 for(let i=0;i<10;i++){let x=i*150-(cam*.22%150);ctx.fillStyle=i%2?"#1b2939":"#182436";ctx.beginPath();ctx.moveTo(x,420);ctx.lineTo(x+75,220+(i%3)*25);ctx.lineTo(x+170,420);ctx.fill();}
}
function drawWorld(cam){
 // ground sections, leaving pits
 let start=Math.floor(cam/80)*80;
 for(let x=start;x<cam+W+80;x+=80){
  const center=x+40;
  if(!world.pits.some(p=>center>p[0]&&center<p[1])){
   rect(x-cam,world.ground,80,H-world.ground,"#263a36");
   rect(x-cam,world.ground,80,7,"#62845a");
   for(let k=0;k<5;k++)rect(x-cam+(k*17)%75,world.ground+18+(k*13)%70,5,4,k%2?"#344d43":"#1d302d");
  }else{
   rect(x-cam,world.ground+8,80,H-world.ground,"#080b12");
   rect(x-cam,world.ground+8,80,4,"#452c43");
  }
 }
 platforms().forEach(p=>{rect(p.x-cam,p.y,p.w,p.h,"#46505f");rect(p.x-cam,p.y,p.w,4,"#87919e");for(let x=8;x<p.w;x+=24)rect(p.x-cam+x,p.y+7,10,3,"#303a49");});
 // spikes near pit edges
 world.pits.forEach(p=>{for(let x=p[0]+4;x<p[1]-8;x+=16){ctx.fillStyle="#b84b62";ctx.beginPath();ctx.moveTo(x-cam,world.ground+8);ctx.lineTo(x+8-cam,world.ground-10);ctx.lineTo(x+16-cam,world.ground+8);ctx.fill();}});
 // exit gate
 rect(world.goal-cam,world.ground-64,32,64,"#7c3aed");rect(world.goal-cam+6,world.ground-56,20,56,"#c084fc");
 rect(world.goal-cam+11,world.ground-45,10,38,"#f5d0fe");
 coinsList.forEach(c=>{if(c.taken)return;let wob=Math.sin(performance.now()/180+c.x)*2;rect(c.x-cam-5,c.y-7+wob,10,14,"#f6bd45");rect(c.x-cam-2,c.y-5+wob,4,10,"#fff0a6");});
 enemies.forEach(e=>{if(!e.alive)return;const x=e.x-cam;rect(x+4,e.y+7,18,20,"#8195a8");rect(x,e.y+13,26,14,"#526779");rect(x+5,e.y+11,5,5,"#ff657a");rect(x+16,e.y+11,5,5,"#ff657a");rect(x+3,e.y+27,7,5,"#303b4a");rect(x+17,e.y+27,7,5,"#303b4a");});
 if(boss&&boss.alive){const x=boss.x-cam;rect(x+8,boss.y+12,46,56,boss.flash?"#fca5a5":"#5d2b63");rect(x,boss.y+28,62,36,boss.flash?"#fca5a5":"#3e234e");rect(x+10,boss.y+4,42,22,"#7e3d7b");rect(x+15,boss.y+15,9,7,"#ff5964");rect(x+39,boss.y+15,9,7,"#ff5964");rect(x+6,boss.y+65,14,11,"#29253b");rect(x+42,boss.y+65,14,11,"#29253b");}
 // player shadow and pixel character
 const px=player.x-cam, py=player.y;
 ctx.globalAlpha=.25;rect(px-2,world.ground-4,28,4,"#000000");ctx.globalAlpha=1;
 if(invuln>0 && Math.floor(performance.now()/80)%2===0)ctx.globalAlpha=.4;
 rect(px+5,py+2,14,10,"#e0b98a");rect(px+3,py+1,18,6,"#1b1724");rect(px+2,py+8,20,5,"#3d536f");
 rect(px+3,py+14,18,13,"#34465f");rect(px+1,py+17,5,10,"#1b2638");rect(px+18,py+17,5,10,"#1b2638");
 let step=player.grounded&&Math.abs(player.vx)>20?Math.sin(player.anim)*3:0;
 rect(px+4,py+26,7,7+step,"#9aa8b9");rect(px+14,py+26,7,7-step,"#9aa8b9");
 rect(px+(player.face>0?15:5),py+5,4,3,"#f8d477");
 if(attackTimer>0){rect(px+(player.face>0?22:-22),py+9,24,4,"#b7e4ff");rect(px+(player.face>0?37:-28),py+5,5,12,"#e8f7ff");}
 if(invuln>0)ctx.globalAlpha=1;
 particles.forEach(p=>{rect(p.x-cam,p.y,4,4,p.color);});
}
function draw(){
 const cam=Math.max(0,Math.min(world.length-W,player.x-W*.38));
 ctx.save();
 if(shake>0)ctx.translate((Math.random()-.5)*8,(Math.random()-.5)*6);
 drawBackground(cam);drawWorld(cam);
 ctx.restore();
 // overlay
 if(world.boss && boss && boss.alive){
  rect(W/2-150,18,300,14,"#291c2d");rect(W/2-147,21,294*(boss.hp/boss.maxHp),8,"#e45b75");
  text("BOSS",W/2,14,12,"#f5c8d4","center");
 }
 if(gameOver||victory){
  rect(0,0,W,H,"rgba(5,8,15,.78)");
  text(victory?"ĐÃ THOÁT KHỎI BÓNG TỐI":"BẠN ĐÃ GỤC NGÃ",W/2,H/2-30,28,victory?"#f6d365":"#ff7185","center");
  text("Điểm: "+score+"   •   Xu: "+coins,W/2,H/2+8,18,"#e8edf5","center");
  text("Nhấn R để chơi lại",W/2,H/2+48,16,"#b9c6d8","center");
 }
 document.getElementById("health").textContent="♥ ".repeat(Math.max(0,player.hp))+"♡ ".repeat(3-Math.max(0,player.hp));
 document.getElementById("coins").textContent="Xu: "+coins+" • Điểm: "+score;
 document.getElementById("level").textContent="Màn: "+(levelIndex+1)+" / "+levels.length+" — "+world.name;
 document.getElementById("sound").textContent="Âm thanh: "+(audioOn?"bật":"tắt")+" (M)";
 if(gameOver||victory)saveBest();
}
function loop(t){const dt=(t-lastTime)/1000||0;lastTime=t;update(dt);draw();requestAnimationFrame(loop);}
requestAnimationFrame(loop);
canvas.addEventListener("pointerdown",()=>{canvas.focus();});
window.addEventListener("keydown",e=>{
 const k=e.key;
 if(["ArrowLeft","ArrowRight","ArrowUp"," ","ArrowDown"].includes(k))e.preventDefault();
 keys[k]=true;
 if(k==="j"||k==="J")attack();
 if(k==="m"||k==="M"){audioOn=!audioOn;beep(500,.06);}
 if((k==="r"||k==="R")&&(gameOver||victory))resetGame();
});
window.addEventListener("keyup",e=>{keys[e.key]=false;});
canvas.focus();
})();
</script>
</body>
</html>
"""

components.html(game_html, height=650, scrolling=False)

st.markdown("---")
st.subheader("🕹️ Mục tiêu bản đầu")
st.markdown(
    """
    - Vượt qua 3 khu vực: **Rừng Tàn**, **Hầm Ngục** và **Đấu Trường**.
    - Thu thập xu, tránh hố và gai, tiêu diệt quái vật.
    - Đánh bại boss ở màn cuối để chiến thắng.
    - Điểm cao nhất được lưu trên trình duyệt của bạn. Đây là lưu cục bộ trên thiết bị hiện tại, chưa phải tài khoản đồng bộ giữa nhiều máy.
    """
)
