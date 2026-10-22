
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
 if(gameOver||victory)saveBest();
}
function loop(t){const dt=(t-lastTime)/1000||0;lastTime=t;update(dt);draw();requestAnimationFrame(loop);}
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

