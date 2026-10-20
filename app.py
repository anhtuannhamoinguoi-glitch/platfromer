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
    **Điều khiển** — A/D hoặc ←/→: di chuyển · Space/W/↑: nhảy · J: tấn công · M: âm thanh · R: chơi lại sau khi thất bại. Bấm BẮT ĐẦU trong màn hình game để vào cuộc hành trình.
    """
)

game_html = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
*{box-sizing:border-box}
html,body{margin:0;background:#080a0b;color:#d8d2c3;font-family:Georgia,'Courier New',monospace}
.wrap{width:100%;max-width:1000px;margin:auto;padding:9px;background:linear-gradient(145deg,#171923,#080a10 45%,#15101d);border:1px solid #756044;border-radius:7px;box-shadow:0 0 0 1px #030404,0 0 26px #9b5de522,inset 0 0 28px #c2a56a12}
.hud{display:grid;grid-template-columns:minmax(210px,1.5fr) minmax(100px,.7fr) minmax(120px,.8fr);gap:8px;align-items:center;padding:8px 4px 10px;color:#d8d2c3;font-size:12px;letter-spacing:.5px}
.status{display:flex;flex-direction:column;gap:5px;min-width:0}.label{font-size:10px;letter-spacing:2px;color:#999487;text-transform:uppercase}.bar{height:12px;background:#211b19;border:1px solid #5b493a;padding:2px;box-shadow:inset 0 1px 3px #000}.bar-fill{height:100%;width:100%;background:linear-gradient(90deg,#6d171b,#a42b2b 65%,#d14b3d);transition:width .12s linear}.subbar{height:5px;background:#171d21;border:1px solid #3b4649;padding:1px}.subfill{height:100%;width:100%;background:#657f91;transition:width .12s linear}.stat{border-left:1px solid #4a4438;padding:4px 10px;min-height:34px}.stat b{display:block;color:#e2d9c4;font-size:15px;font-weight:normal;letter-spacing:1px}.stat small{display:block;color:#8e8a7e;font-size:9px;letter-spacing:1.5px;margin-bottom:3px}.right-stats{display:flex;justify-content:flex-end;gap:12px}.stat em{font-style:normal;color:#c7a96b}
.stage{position:relative;border:1px solid #817052;background:#050708;line-height:0;overflow:hidden;box-shadow:inset 0 0 34px #000,0 0 24px #7c3aed18}canvas{display:block;width:100%;height:auto;background:#101319;image-rendering:pixelated;outline:none;filter:saturate(1.12) contrast(1.04);}
.hint{font-size:10px;line-height:1.7;color:#8d8a80;padding:9px 4px 2px;text-align:center;letter-spacing:.4px;border-top:1px solid #292821;margin-top:5px}
.menu{position:absolute;inset:0;z-index:3;display:flex;align-items:center;justify-content:center;background:linear-gradient(90deg,rgba(4,6,7,.92),rgba(5,7,8,.56) 58%,rgba(4,6,7,.2));line-height:1.4}.menu-card{width:54%;padding:22px 24px;border-left:2px solid #a58a55;background:linear-gradient(90deg,rgba(9,11,12,.92),rgba(9,11,12,.45));text-shadow:0 2px #000}.eyebrow{font-size:9px;letter-spacing:4px;color:#b59a65;margin-bottom:10px}.menu-title{font:700 clamp(22px,4vw,42px) Georgia,serif;letter-spacing:3px;color:#e4ddca;text-shadow:0 3px #342b20,0 0 18px #c3a26733}.menu-sub{font-size:10px;letter-spacing:2px;color:#9a978b;margin:8px 0 20px}.rule{height:1px;background:linear-gradient(90deg,#a58a55,transparent);margin:15px 0}.start-btn{display:block;width:100%;padding:12px 15px;background:#8e2527;border:1px solid #d0a66b;color:#f4e8cd;font:700 12px Georgia,serif;letter-spacing:3px;cursor:pointer;box-shadow:0 3px 0 #351516;transition:background .15s,transform .15s}.start-btn:hover{background:#aa3031;transform:translateY(-1px)}.difficulty{display:flex;gap:6px;margin:14px 0 4px}.diff-btn{flex:1;padding:9px 4px;background:#17191b;border:1px solid #514838;color:#bdb8aa;font:600 10px Georgia,serif;letter-spacing:1px;cursor:pointer}.diff-btn.active{background:#3a2823;border-color:#c7a96b;color:#f4e8cd;box-shadow:inset 0 -2px #a33b36}.diff-desc{font-size:9px;color:#999487;min-height:14px;margin-top:6px}.menu-note{font-size:10px;color:#a09a8b;margin-top:13px;letter-spacing:.5px}.corner{position:absolute;right:14px;bottom:12px;color:#b8a779;font-size:9px;letter-spacing:2px;opacity:.85}
@media(max-width:600px){.hud{grid-template-columns:1fr 1fr}.right-stats{justify-content:flex-start}.menu-card{width:76%;padding:12px}.menu-sub{margin-bottom:10px}.menu-note{display:none}}
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
    <div class="menu" id="mainmenu"><div class="menu-card"><div class="eyebrow">THE LAST LIGHT IS FADING</div><div class="menu-title">SHADOWBOUND</div><div class="menu-sub">A SOULSLIKE PIXEL ADVENTURE</div><div class="rule"></div><div class="eyebrow">CHỌN ĐỘ KHÓ</div><div class="difficulty"><button class="diff-btn" data-diff="easy">DỄ</button><button class="diff-btn active" data-diff="normal">TRUNG BÌNH</button><button class="diff-btn" data-diff="hard">KHÓ</button></div><div class="diff-desc" id="diffdesc">Thử thách cân bằng, phù hợp để làm quen.</div><button class="start-btn" id="startbtn">BẮT ĐẦU HÀNH TRÌNH</button><div class="menu-note">Ba vùng đất. Một lời nguyền. Không có đường quay lại.</div></div><div class="corner">WASD / ARROWS · SPACE · J</div></div>
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
let best = 0;
try { best = Number(localStorage.getItem("shadowbound_best") || 0); } catch(e) {}
const bestEl = document.getElementById("best");
bestEl.textContent = "Kỷ lục: " + best;

const levels = [
 {name:"Rừng Tàn", length:2300, start:70, goal:2180, ground:430,
  platforms:[[250,360,120],[470,310,120],[710,370,140],[960,320,120],[1210,360,140],[1490,300,130],[1770,350,130]],
  pits:[[390,455],[630,690],[880,930],[1110,1160],[1390,1440],[1660,1710],[1950,2010]],
  coinSpots:[[180,380],[290,315],[520,265],[760,325],[1010,275],[1260,315],[1540,255],[1810,305],[2050,385]],
  enemies:[330,780,1040,1570,1870],
  traps:[{type:"boulder",x:500,start:470,end:820,damage:1.2,size:104,speed:245,pause:4.8,rollTime:2.8},{type:"fire",x:1015,damage:0.65,period:3.2,active:1.15},{type:"fire",x:1760,damage:0.65,period:2.8,active:1.0},
   {type:"laser",x:760,y:245,damage:0.8,period:3.8,active:1.15,points:[[760,245],[900,245],[900,345],[1035,345],[1035,265]]}], boss:false},
 {name:"Hầm Ngục", length:2600, start:70, goal:2470, ground:430,
  platforms:[[210,350,120],[430,300,130],[680,350,120],[900,285,130],[1160,340,140],[1430,290,130],[1680,350,130],[1940,280,130],[2190,340,120]],
  pits:[[360,410],[620,670],[850,890],[1100,1150],[1390,1420],[1640,1670],[1900,1930],[2150,2180]],
  coinSpots:[[150,380],[250,305],[470,255],[720,305],[950,240],[1200,295],[1480,245],[1730,305],[1990,235],[2250,295]],
  enemies:[300,740,1020,1510,1810,2250],
  traps:[{type:"boulder",x:690,start:650,end:1010,damage:1.3,size:112,speed:260,pause:5.2,rollTime:3.0},{type:"fire",x:1210,damage:0.7,period:2.7,active:1.15},{type:"boulder",x:1690,start:1650,end:2010,damage:1.3,size:112,speed:260,pause:5.2,rollTime:3.0},
   {type:"laser",x:1240,y:225,damage:0.85,period:3.3,active:1.35,points:[[1240,225],[1380,225],[1380,330],[1530,330],[1530,245]]}], boss:false},
 {name:"Đấu Trường", length:1800, start:70, goal:1680, ground:430,
  platforms:[[280,350,130],[540,300,130],[800,350,140],[1080,300,130],[1350,350,130]],
  pits:[[430,480],[700,750],[970,1020],[1240,1290]],
  coinSpots:[[180,380],[330,305],[590,255],[850,305],[1130,255],[1400,305],[1580,385]],
  enemies:[350,880],
  traps:[{type:"fire",x:620,damage:0.75,period:2.5,active:1.1},{type:"boulder",x:990,start:950,end:1290,damage:1.35,size:120,speed:275,pause:5.5,rollTime:3.2},
   {type:"laser",x:600,y:235,damage:0.95,period:2.8,active:1.55,points:[[600,235],[745,235],[745,335],[885,335],[885,245]]}], boss:true}
];
let world, player, enemies, coinsList, particles, boss, traps;

function makeWorld(index) {
 const d = levels[index];
 world = d;
 player = {x:d.start,y:350,w:24,h:34,vx:0,vy:0,grounded:false,face:1,hp:difficultySettings[difficulty].hp,maxHp:difficultySettings[difficulty].hp,anim:0};
 enemies = d.enemies.map((x,i)=>({x,y:390,w:26,h:30,vx:(i%2?1:-1)*55*difficultySettings[difficulty].enemy,alive:true,home:x,range:75,hp:1}));
 coinsList = d.coinSpots.map(([x,y])=>({x,y,r:8,taken:false}));
 particles = [];
 traps = (d.traps || []).map((t,i)=>({...t,damage:t.damage*(difficulty==="easy"?0.78:difficulty==="hard"?1.2:1),period:t.period? t.period/difficultySettings[difficulty].trap:t.period,active:t.active,dropSpeed:(t.dropSpeed||620)*difficultySettings[difficulty].trap,baseX:t.x,dir:i%2===0?1:-1,phase:Math.random()*(t.period||2),rolling:false,state:"rest",y:-(t.size||108)-10,flameHeight:t.type==="fire"?(difficulty==="hard"?[48,72,98,126][Math.floor(Math.random()*4)]:difficulty==="easy"?58:78):78,pauseTimer:(t.type==="boulder"?(t.pause||6)*difficultySettings[difficulty].pause*(0.8+Math.random()*0.35):0),rollTimer:0,hitCooldown:0,impactTimer:0,laserPhase:Math.random()*(t.period||2),laserOn:false}));
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
 if(invuln>0 || gameOver || victory) return;
 player.hp=Math.max(0,player.hp-amount); invuln=1.25; shake=.25; noiseHit(); addParticles(player.x+12,player.y+15,"#ff657a",12);
 if(player.hp<=0){gameOver=true; beep(90,.5,"sawtooth",.06);}
}
function attack(){
 if(!started || attackTimer>0 || gameOver || victory) return;
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
 if(!started || gameOver || victory) return;
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
   // Laser pulses on/off; its route has at most three reflections at solid mirror objects.
   const period=t.period/(difficulty==="hard"?1.2:difficulty==="easy"?0.88:1);
   const active=t.active*(difficulty==="hard"?1.18:difficulty==="easy"?0.78:1);
   t.laserPhase=(t.laserPhase+dt)%period;
   t.laserOn=t.laserPhase<active;
   if(t.laserOn && t.hitCooldown<=0){
    const pts=t.points||[]; let hitBeam=false;
    for(let i=0;i<pts.length-1;i++){
     const a=pts[i],b=pts[i+1],px=player.x+player.w/2,py=player.y+player.h/2;
     const dx=b[0]-a[0],dy=b[1]-a[1],len2=dx*dx+dy*dy;
     const u=Math.max(0,Math.min(1,((px-a[0])*dx+(py-a[1])*dy)/(len2||1)));
     const qx=a[0]+u*dx,qy=a[1]+u*dy;
     if(Math.hypot(px-qx,py-qy)<13){hitBeam=true;break;}
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
function drawBackground(cam){
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
   rect(x-cam,world.ground,80,H-world.ground,"#1d2c31");
   rect(x-cam,world.ground,80,6,"#6a9a70");rect(x-cam,world.ground+6,80,3,"#354f4a");
   for(let k=0;k<9;k++){const xx=x-cam+(k*19)%76,yy=world.ground+16+(k*23)%88;rect(xx,yy,4+(k%3),3,k%2?"#2b4140":"#142329");}
   // little grass blades along the edge
   for(let k=0;k<5;k++){let gx=x-cam+k*17+5;rect(gx,world.ground-3,2,5,k%2?"#9bc58a":"#507f69");}
  }else{
   rect(x-cam,world.ground+5,80,H-world.ground,"#05060c");glow(x-cam+40,world.ground+65,48,"#8f244f",.15);
   rect(x-cam,world.ground+5,80,3,"#6c3455");
  }
 }
 // platforms with stone edges and pixel cracks
 platforms().forEach((p,i)=>{
  rect(p.x-cam,p.y,p.w,p.h,"#33364d");rect(p.x-cam,p.y,p.w,4,"#9d8bb7");rect(p.x-cam,p.y+4,p.w,3,"#625675");
  for(let x=9;x<p.w;x+=25){rect(p.x-cam+x,p.y+8,11,3,"#25293d");rect(p.x-cam+x+5,p.y+11,4,2,"#4b465e");}
  for(let x=12;x<p.w;x+=47)rect(p.x-cam+x,p.y-3,3,3,"#b5a6cb");
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
 });
 // exit portal
 const gx=world.goal-cam, gy=world.ground-69, pulse=.7+.3*Math.sin(performance.now()/190);
 glow(gx+16,gy+38,65,"#a855f7",pulse);rect(gx-5,gy-4,42,73,"#4b2d70");rect(gx,gy,32,65,"#9b5de5");rect(gx+5,gy+5,22,55,"#201532");
 ctx.strokeStyle="#e9c8ff";ctx.lineWidth=3;ctx.strokeRect(gx+4,gy+3,24,59);rect(gx+10,gy+13,4,4,"#f3d7ff");rect(gx+20,gy+30,4,4,"#f3d7ff");
 // coins: glowing gold pixel coins
 coinsList.forEach(c=>{if(c.taken)return;let wob=Math.sin(performance.now()/180+c.x)*3,x=c.x-cam,y=c.y+wob;glow(x,y,23,"#fbbf24",.3);rect(x-6,y-8,12,16,"#e9a52e");rect(x-4,y-10,8,2,"#ffe8a1");rect(x-4,y-6,8,12,"#ffdc69");rect(x-1,y-5,3,10,"#fff4bc");rect(x-6,y+7,12,2,"#b87920");});
 // enemies with glowing eyes and little shadows
 enemies.forEach(e=>{if(!e.alive)return;const x=e.x-cam,y=e.y;glow(x+13,y+15,28,"#fb456c",.16);ctx.globalAlpha=.35;rect(x+1,world.ground-3,25,4,"#000");ctx.globalAlpha=1;
  rect(x+4,y+5,18,20,"#687c91");rect(x+1,y+12,24,14,"#35495f");rect(x+5,y+9,16,8,"#91a2b9");rect(x+5,y+12,5,4,"#ff5578");rect(x+16,y+12,5,4,"#ff5578");rect(x+4,y+26,7,5,"#222c40");rect(x+16,y+26,7,5,"#222c40");rect(x+8,y+7,3,2,"#dbeafe");
 });
 // boss silhouette with crown spikes, armor plates and health glow
 if(boss&&boss.alive){const x=boss.x-cam,y=boss.y;glow(x+31,y+35,85,"#d946ef",.2);rect(x+8,y+12,46,56,boss.flash?"#ffd2e1":"#492650");rect(x,y+28,62,36,boss.flash?"#ffd2e1":"#281b3d");rect(x+10,y+4,42,22,boss.flash?"#ffd2e1":"#70366f");
  for(let i=0;i<5;i++){ctx.fillStyle="#b45a9f";ctx.beginPath();ctx.moveTo(x+9+i*10,y+7);ctx.lineTo(x+14+i*10,y-8-(i%2)*5);ctx.lineTo(x+19+i*10,y+7);ctx.fill();}
  rect(x+14,y+15,10,7,"#ff426f");rect(x+38,y+15,10,7,"#ff426f");glow(x+19,y+18,15,"#fb376b",.65);glow(x+43,y+18,15,"#fb376b",.65);rect(x+6,y+65,14,11,"#191627");rect(x+42,y+65,14,11,"#191627");rect(x+10,y+36,9,13,"#8c4b91");rect(x+43,y+36,9,13,"#8c4b91");
 }
 // player shadow, aura and detailed pixel knight
 const px=player.x-cam, py=player.y;const run=player.grounded&&Math.abs(player.vx)>20;const step=run?Math.sin(player.anim)*3:0;
 ctx.globalAlpha=.35;rect(px-3,world.ground-4,30,4,"#000");ctx.globalAlpha=1;
 glow(px+12,py+19,38,"#6d75ff",.13);
 // Pulsing soul-light around the knight, stronger while moving or attacking.
 const aura=.08+(Math.abs(player.vx)/220)*.07+(attackTimer>0?.18:0);
 glow(px+12,py+18,run?48:38,attackTimer>0?"#8be9ff":"#6d75ff",aura);
 if(run && Math.floor(performance.now()/95)%2===0){
  rect(px+(player.face>0?-5:25),py+23,3,3,"#a5b4fc");
  rect(px+(player.face>0?-10:29),py+29,2,2,"#818cf8");
 }

 if(invuln>0 && Math.floor(performance.now()/80)%2===0)ctx.globalAlpha=.42;
 // flowing scarf / cape
 rect(px+(player.face>0?-2:16),py+9,9,19,"#5c2879");rect(px+(player.face>0?-5:18),py+14,6,12,"#9b3f9b");rect(px+(player.face>0?-8:20),py+20,5,8,"#4b286c");
 // helmet and face slit
 rect(px+4,py+1,16,10,"#22283d");rect(px+2,py+4,20,8,"#414b6b");rect(px+5,py+2,14,3,"#7884a5");rect(px+5,py+8,14,4,"#151a2b");
 rect(px+(player.face>0?14:5),py+7,5,3,"#79e7ff");glow(px+(player.face>0?16:7),py+8,12,"#5ee7ff",.5);
 // torso armor and belt
 rect(px+4,py+13,16,14,"#313c59");rect(px+2,py+16,5,10,"#202940");rect(px+17,py+16,5,10,"#202940");rect(px+7,py+15,10,8,"#526482");rect(px+8,py+19,8,2,"#a4b6d1");rect(px+5,py+25,14,3,"#d4a65b");rect(px+10,py+25,4,3,"#fff0ad");
 // legs animate when running
 rect(px+5,py+27,6,7+step,"#667895");rect(px+14,py+27,6,7-step,"#667895");rect(px+3,py+31+step,8,3,"#20273d");rect(px+14,py+31-step,8,3,"#20273d");
 // sword and slash arc
 if(attackTimer>0){const sx=px+(player.face>0?21:-22),sy=py+12;glow(sx+10,sy+3,34,"#8be9ff",.4);rect(sx,sy,24,4,"#8be9ff");rect(sx+(player.face>0?15:2),sy-5,4,14,"#e4fbff");rect(sx+(player.face>0?7:10),sy-8,3,4,"#ffffff");ctx.strokeStyle="#b9f4ff";ctx.lineWidth=3;ctx.beginPath();ctx.arc(px+12,py+17,25,player.face>0?-1.15:.05,player.face>0?.9:2.1);ctx.stroke();}
 if(invuln>0)ctx.globalAlpha=1;
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
 document.getElementById("coins").textContent="◈ "+coins+"  ·  "+score;
 document.getElementById("level").textContent=["I","II","III"][levelIndex]+" · "+world.name;
 if(gameOver||victory)saveBest();
}
function loop(t){const dt=(t-lastTime)/1000||0;lastTime=t;update(dt);draw();requestAnimationFrame(loop);}
requestAnimationFrame(loop);
document.querySelectorAll(".diff-btn").forEach(btn=>btn.addEventListener("click",()=>{difficulty=btn.dataset.diff;document.querySelectorAll(".diff-btn").forEach(b=>b.classList.toggle("active",b===btn));document.getElementById("diffdesc").textContent=difficultySettings[difficulty].desc;makeWorld(levelIndex); }));
document.getElementById("startbtn").addEventListener("click",()=>{makeWorld(0);started=true;document.getElementById("mainmenu").style.display="none";canvas.focus();beep(330,.08,"triangle",.025);});
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
st.subheader("🕹️ Shadowbound — Bản nâng cấp đồ họa")
st.markdown(
    """
    - Vượt qua 3 khu vực: **Rừng Tàn**, **Hầm Ngục** và **Đấu Trường**.
    - Thu thập xu, tránh hố, gai, **đá lăn** và **bẫy phun lửa**; mỗi bẫy gây sát thương khác nhau.
    - Đánh bại boss ở màn cuối để chiến thắng.
    - Hiệu ứng nâng cấp: cực quang, tia trăng, sương mù chuyển động, linh hồn bay, rễ cây tiền cảnh, nấm phát sáng, cổ tự trên nền đá, viền điện ảnh và hào quang nhân vật.
    - Điểm cao nhất được lưu trên trình duyệt của bạn. Đây là lưu cục bộ trên thiết bị hiện tại, chưa phải tài khoản đồng bộ giữa nhiều máy.
    """
)
