
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SHADOWBOUND",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

GAME_HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { box-sizing:border-box; }
body {
    margin:0; background:#080910; color:#eee;
    font-family:Arial,sans-serif; overflow:hidden;
}
#wrap { width:100%; max-width:1100px; margin:auto; padding:8px; }
h1 {
    margin:4px 0 8px; text-align:center; letter-spacing:5px;
    color:#d9b2ff; text-shadow:0 0 18px #813dca;
}
#hud {
    display:flex; justify-content:space-between; gap:8px;
    flex-wrap:wrap; padding:10px; margin-bottom:8px;
    background:#171523; border:1px solid #42344f; border-radius:8px;
}
.huditem { font-size:14px; }
#healthOuter { width:150px; height:12px; background:#3b202b;
    border-radius:8px; overflow:hidden; display:inline-block; }
#health { height:100%; width:100%; background:#e74462; }
canvas {
    width:100%; display:block; background:#10101c;
    border:1px solid #59416e; border-radius:8px;
    touch-action:none;
}
#help { color:#bdb8cc; font-size:13px; line-height:1.7; padding:8px 2px; }
#controls {
    display:flex; justify-content:center; flex-wrap:wrap;
    gap:8px; margin-top:8px;
}
button {
    background:#282238; color:#fff; border:1px solid #76599a;
    border-radius:8px; padding:11px 15px; cursor:pointer;
    font-size:14px; font-weight:bold;
}
button:active { background:#604080; }
#message {
    text-align:center; color:#f3d8ff; font-weight:bold;
    min-height:24px; padding:5px;
}
</style>
</head>
<body>
<div id="wrap">
<h1>SHADOWBOUND</h1>
<div id="hud">
  <div class="huditem">❤️ Máu: <span id="hpText">100 / 100</span>
    <div id="healthOuter"><div id="health"></div></div>
  </div>
  <div class="huditem">🧪 Bình máu: <b id="potionText">2</b></div>
  <div class="huditem">🪙 Vàng: <b id="coinsText">0</b></div>
  <div class="huditem">🏰 Màn: <b id="levelText">1 / 3</b></div>
</div>
<canvas id="game" width="960" height="480"></canvas>
<div id="message">Tiêu diệt quái vật và tìm cổng sang màn tiếp theo!</div>
<div id="controls">
  <button id="left">◀ Trái</button>
  <button id="right">Phải ▶</button>
  <button id="jump">⬆ Nhảy</button>
  <button id="attack">⚔️ Tấn công</button>
  <button id="potion">🧪 Uống máu (H)</button>
  <button id="restart">↻ Chơi lại</button>
</div>
<div id="help">
  Máy tính: A/D hoặc phím mũi tên để di chuyển, W/Space để nhảy,
  J để tấn công, H để uống bình máu. Mỗi bình hồi 50% máu tối đa.
  Bạn có 2 bình máu mỗi lượt. Đánh bại quái vật rồi đi đến cổng tím.
</div>
</div>
<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const W = canvas.width, H = canvas.height;
const $ = id => document.getElementById(id);

let keys = {};
let player, enemies, coins, level, score, gameOver, victory;
let attackTime = 0, invincible = 0, frame = 0;
let platforms = [], laser = null;

function makeLevel(n) {
    level = n;
    platforms = [
        {x:0,y:430,w:960,h:50},
        {x:150,y:350,w:140,h:18},
        {x:370,y:295,w:145,h:18},
        {x:610,y:350,w:150,h:18}
    ];
    player = {
        x:45,y:380,w:26,h:42,vx:0,vy:0,
        hp:100,maxHp:100,potions:2,face:1,ground:false
    };
    enemies = [];
    const count = 2 + n;
    for(let i=0;i<count;i++) {
        enemies.push({
            x:250+i*150,y:390,w:28,h:40,
            hp:n===3?3:2, maxHp:n===3?3:2,
            vx:0.7+0.2*n, alive:true,
            type:(i%2===0?"walker":"archer"),
            cooldown:100+i*25
        });
    }
    coins = [];
    for(let i=0;i<5;i++) coins.push({x:150+i*140,y:250+(i%2)*35,taken:false});
    laser = n===3 ? {x:480,y:220,r:17,vx:3,vy:2} : null;
    gameOver = false;
    victory = false;
    attackTime = 0;
    invincible = 0;
    $("message").textContent = "Màn "+(n+1)+": Hãy sống sót!";
    updateHUD();
}

function resetGame() {
    score=0; level=0;
    makeLevel(0);
}

function usePotion() {
    if(gameOver || victory || player.potions<=0 || player.hp>=player.maxHp) return;
    player.hp=Math.min(player.maxHp,player.hp+player.maxHp*0.5);
    player.potions--;
    $("message").textContent="Đã hồi máu! Còn "+player.potions+" bình.";
    updateHUD();
}

function hurt(amount) {
    if(invincible>0 || gameOver || victory) return;
    player.hp=Math.max(0,player.hp-amount);
    invincible=55;
    if(player.hp<=0) {
        gameOver=true;
        $("message").textContent="Bạn đã gục ngã! Nhấn Chơi lại để thử lần nữa.";
    }
    updateHUD();
}

function attack() {
    if(gameOver || victory) return;
    attackTime=12;
    for(const e of enemies) {
        if(!e.alive) continue;
        const dx=e.x-player.x;
        if(Math.abs(dx)<65 && Math.abs(e.y-player.y)<65 && Math.sign(dx)===player.face) {
            e.hp--;
            if(e.hp<=0) {
                e.alive=false; score+=10;
                coins.push({x:e.x,y:e.y,taken:false,drop:true});
            }
        }
    }
}

function updateHUD() {
    $("hpText").textContent=Math.ceil(player.hp)+" / "+player.maxHp;
    $("health").style.width=(player.hp/player.maxHp*100)+"%";
    $("potionText").textContent=player.potions;
    $("coinsText").textContent=score;
    $("levelText").textContent=(level+1)+" / 3";
}

function movePlayer() {
    if(keys["ArrowLeft"]||keys["a"]||keys["A"]) {
        player.vx=-4; player.face=-1;
    } else if(keys["ArrowRight"]||keys["d"]||keys["D"]) {
        player.vx=4; player.face=1;
    } else player.vx*=0.72;

    if((keys[" "]||keys["ArrowUp"]||keys["w"]||keys["W"])&&player.ground) {
        player.vy=-11; player.ground=false;
    }

    player.vy+=0.48;
    player.x+=player.vx;
    player.y+=player.vy;
    player.ground=false;

    if(player.x<0) player.x=0;
    if(player.x+player.w>W) player.x=W-player.w;

    for(const p of platforms) {
        if(player.x+player.w>p.x && player.x<p.x+p.w &&
           player.y+player.h>=p.y && player.y+player.h<=p.y+18 &&
           player.vy>=0) {
            player.y=p.y-player.h;
            player.vy=0; player.ground=true;
        }
    }
    if(player.y>H) hurt(100);
}

function updateEnemies() {
    for(const e of enemies) {
        if(!e.alive) continue;
        e.cooldown--;
        if(e.type==="walker") {
            if(Math.abs(player.x-e.x)<260) {
                e.vx=player.x<e.x?-1.0:1.0;
            }
            e.x+=e.vx;
            if(e.x<0||e.x+e.w>W) e.vx*=-1;
        } else if(e.cooldown<=0) {
            e.cooldown=145;
            if(Math.abs(player.x-e.x)<390) {
                // Mũi tên được biểu diễn bằng viên đạn nhỏ
                projectiles.push({x:e.x,y:e.y+15,vx:player.x<e.x?-4:4,life:100});
            }
        }
        if(player.x<e.x+e.w && player.x+player.w>e.x &&
           player.y<e.y+e.h && player.y+player.h>e.y) hurt(12);
    }
}

let projectiles=[];
function updateProjectiles() {
    for(const b of projectiles) {
        b.x+=b.vx; b.life--;
        if(b.life>0 && player.x<b.x+8 && player.x+player.w>b.x &&
           player.y<b.y+8 && player.y+player.h>b.y) {
            hurt(10); b.life=0;
        }
    }
    projectiles=projectiles.filter(b=>b.life>0&&b.x>-10&&b.x<W+10);
}

function updateLaser() {
    if(!laser) return;
    laser.x+=laser.vx; laser.y+=laser.vy;
    if(laser.x<100||laser.x>860) laser.vx*=-1;
    if(laser.y<90||laser.y>390) laser.vy*=-1;
    const dx=player.x+player.w/2-laser.x;
    const dy=player.y+player.h/2-laser.y;
    if(Math.hypot(dx,dy)<laser.r+20) hurt(15);
}

function updateCoins() {
    for(const c of coins) {
        if(c.taken) continue;
        if(player.x<c.x+15&&player.x+player.w>c.x-15&&
           player.y<c.y+15&&player.y+player.h>c.y-15) {
            c.taken=true; score+=c.drop?5:1;
        }
    }
}

function drawBackground() {
    const g=ctx.createLinearGradient(0,0,0,H);
    g.addColorStop(0,"#111126"); g.addColorStop(1,"#30182f");
    ctx.fillStyle=g; ctx.fillRect(0,0,W,H);
    for(let i=0;i<65;i++) {
        let x=(i*137)%W, y=(i*71)%350;
        ctx.fillStyle=i%3===0?"#a68ad9":"#6a6591";
        ctx.globalAlpha=0.35; ctx.fillRect(x,y,2,2);
    }
    ctx.globalAlpha=1;
    // Mặt trăng
    ctx.fillStyle="#d9c9f0"; ctx.globalAlpha=0.75;
    ctx.beginPath(); ctx.arc(800,85,33,0,Math.PI*2); ctx.fill();
    ctx.globalAlpha=1;
}

function draw() {
    drawBackground();
    for(const p of platforms) {
        ctx.fillStyle="#39304b"; ctx.fillRect(p.x,p.y,p.w,p.h);
        ctx.fillStyle="#79608e"; ctx.fillRect(p.x,p.y,p.w,4);
    }

    // Cổng sang màn kế tiếp
    ctx.fillStyle="#a65bff"; ctx.fillRect(900,350,28,80);
    ctx.fillStyle="#e4caff"; ctx.fillRect(907,360,14,65);

    for(const c of coins) {
        if(c.taken) continue;
        ctx.fillStyle=c.drop?"#ffd66b":"#e9c74d";
        ctx.beginPath(); ctx.arc(c.x,c.y,7,0,Math.PI*2); ctx.fill();
    }

    for(const e of enemies) {
        if(!e.alive) continue;
        ctx.fillStyle=e.type==="archer"?"#b4a2c8":"#b83b58";
        ctx.fillRect(e.x,e.y,e.w,e.h);
        ctx.fillStyle="#241622"; ctx.fillRect(e.x+5,e.y+8,5,5);
        ctx.fillRect(e.x+18,e.y+8,5,5);
        ctx.fillStyle="#251c2c"; ctx.fillRect(e.x,e.y-9,e.w,4);
        ctx.fillStyle="#e84660"; ctx.fillRect(e.x,e.y-9,e.w*e.hp/e.maxHp,4);
        if(e.type==="archer") {
            ctx.strokeStyle="#e2c9a5"; ctx.lineWidth=2;
            ctx.beginPath(); ctx.moveTo(e.x+e.w/2,e.y+18);
            ctx.lineTo(e.x+e.w/2+(player.x<e.x?-13:13),e.y+18); ctx.stroke();
        }
    }

    for(const b of projectiles) {
        ctx.fillStyle="#ffb67a"; ctx.fillRect(b.x,b.y,10,4);
    }

    if(laser) {
        ctx.save();
        ctx.strokeStyle="#ff315d"; ctx.lineWidth=4;
        ctx.shadowBlur=18; ctx.shadowColor="#ff164a";
        ctx.beginPath(); ctx.moveTo(70,laser.y); ctx.lineTo(890,laser.y); ctx.stroke();
        ctx.fillStyle="#ff315d"; ctx.beginPath();
        ctx.arc(laser.x,laser.y,laser.r,0,Math.PI*2); ctx.fill();
        ctx.restore();
    }

    // Người chơi
    if(invincible<=0||Math.floor(frame/5)%2===0) {
        ctx.fillStyle="#d9c5ff";
        ctx.fillRect(player.x+4,player.y,18,15);
        ctx.fillStyle="#7856a4";
        ctx.fillRect(player.x,player.y+15,player.w,27);
        ctx.fillStyle="#f6e9ff";
        ctx.fillRect(player.x+(player.face===1?17:5),player.y+5,4,4);
    }

    if(attackTime>0) {
        ctx.strokeStyle="#f4e0ff"; ctx.lineWidth=5;
        ctx.beginPath();
        const ax=player.x+player.w/2+player.face*35;
        ctx.arc(ax,player.y+20,19,-1.1,1.1); ctx.stroke();
    }

    if(gameOver||victory) {
        ctx.fillStyle="rgba(0,0,0,0.72)"; ctx.fillRect(0,0,W,H);
        ctx.textAlign="center";
        ctx.fillStyle=victory?"#e7c8ff":"#ff758d";
        ctx.font="bold 42px Arial";
        ctx.fillText(victory?"CHIẾN THẮNG!":"GAME OVER",W/2,H/2);
        ctx.font="20px Arial"; ctx.fillStyle="#fff";
        ctx.fillText("Nhấn Chơi lại để bắt đầu",W/2,H/2+42);
    }
}

function tick() {
    frame++;
    if(!gameOver&&!victory) {
        movePlayer();
        updateEnemies();
        updateProjectiles();
        updateLaser();
        updateCoins();

        if(player.x+player.w>895 && player.y+player.h>345) {
            if(level<2) {
                makeLevel(level+1);
                projectiles=[];
            } else {
                victory=true;
                $("message").textContent="Bạn đã chinh phục cả 3 màn!";
            }
        }
        if(attackTime>0) attackTime--;
        if(invincible>0) invincible--;
        updateHUD();
    }
    draw();
    requestAnimationFrame(tick);
}

function bindHold(id,key) {
    const el=$(id);
    el.addEventListener("pointerdown",e=>{e.preventDefault();keys[key]=true;});
    for(const ev of ["pointerup","pointercancel","pointerleave"])
        el.addEventListener(ev,()=>keys[key]=false);
}
bindHold("left","ArrowLeft");
bindHold("right","ArrowRight");
bindHold("jump"," ");
$("attack").addEventListener("click",attack);
$("potion").addEventListener("click",usePotion);
$("restart").addEventListener("click",()=>{projectiles=[];resetGame();});

window.addEventListener("keydown",e=>{
    keys[e.key]=true;
    if(["ArrowLeft","ArrowRight","ArrowUp"," "].includes(e.key)) e.preventDefault();
    if(e.repeat) return;
    if(e.key==="j"||e.key==="J") attack();
    if(e.key==="h"||e.key==="H") usePotion();
    if(e.key==="r"||e.key==="R") {projectiles=[];resetGame();}
});
window.addEventListener("keyup",e=>keys[e.key]=false);
window.addEventListener("blur",()=>keys={});

resetGame();
tick();
</script>
</body>
</html>
"""

components.html(GAME_HTML, height=750, scrolling=False)
