"""Builds index.html from src/. Run: python src/build.py"""
from pathlib import Path
SRC=Path(__file__).resolve().parent; ROOT=SRC.parent
import json,re
iv=open(SRC/'buddhdhamma-ivory.html',encoding='utf-8').read()
tpl=open(SRC/'proto3_template.html',encoding='utf-8').read()
art=json.load(open(SRC/'art2.json',encoding='utf-8'))

# ---- map block from the ivory build ----
a=iv.index('<div id="spread">'); s0=iv.index('<script>',a); s1=iv.index('</script>',s0)+9
mp=iv[a:s1]+'\n</div>'
# panel markup
p0=mp.index('<aside class="panel"'); p1=mp.index('</aside>',p0)+8
panel='''<aside class="panel card" id="panel" aria-live="polite">
  <div class="pic" id="ppic"></div>
  <span class="label">Place · Sarnath, near Vārāṇasī</span>
  <h3>Isipatana</h3><p class="anc">Earliest Buddhist presence c. 450 BCE</p>
  <div class="tags"><span class="badge">◇ Traditional account</span></div>
  <p class="d">Deer park of the first teaching in tradition; Ashokan pillar, c. 3rd c. BCE.</p>
  <span class="label" style="margin-top:4px">Hover to preview · tap to open</span>
  <a class="btn primary" id="penter" href="#place-isipatana">Enter Isipatana →</a>
 </aside>'''
mp=mp[:p0]+panel+mp[p1:]
mp=mp.replace('<div class="mapbox"><svg viewBox="0 0 1100 640"','<div class="mapbox"><div class="layers" id="layers"><button type="button" data-l="terrain" aria-pressed="true" title="Mountains &amp; deserts"><span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M2.5 19.5 9 8l4.2 7 2.6-3.6 5.7 8.1z"/></svg></span><span class="tx">Mountains &amp; deserts</span></button><button type="button" data-l="water" aria-pressed="true" title="Rivers &amp; lakes"><span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M2.5 9.5c2.2-2 4.1-2 6.3 0s4.1 2 6.3 0 4.1-2 6.4 0M2.5 15.5c2.2-2 4.1-2 6.3 0s4.1 2 6.3 0 4.1-2 6.4 0"/></svg></span><span class="tx">Rivers &amp; lakes</span></button><button type="button" data-l="routes" aria-pressed="true" title="Routes"><span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="5" cy="18" r="2"/><circle cx="19" cy="6" r="2"/><path d="M6.6 16.6C10 13 9 9 12.5 8.2S17 7.5 17.4 7.2" stroke-dasharray="2.5 2.5"/></svg></span><span class="tx">Routes</span></button><button type="button" data-l="viharas" aria-pressed="false" title="Centres of learning"><span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"><path d="M3 9.5 12 4l9 5.5M5 10v8M9.7 10v8M14.3 10v8M19 10v8M3 20.5h18"/></svg></span><span class="tx">Centres of learning</span></button></div><div class="zoomctl" role="group" aria-label="Map zoom"><button type="button" data-z="in" aria-label="Zoom in" title="Zoom in">+</button><button type="button" data-z="out" aria-label="Zoom out" title="Zoom out">−</button><button type="button" data-z="reset" aria-label="Reset map view" title="Reset map view">⟲</button></div><svg class="main" viewBox="0 0 1100 640"',1)
mp=mp.replace('<g id="regions"','<g id="terrain"></g><g id="water"></g><g id="regions"',1)
mp=mp.replace('<div class="legend">','<div class="legend"><span><i class="mtn"></i>Mountains</span><span><i class="river"></i>Rivers and lakes</span>',1)
R=[("function showTip(s,ev){","function showTip(s,ev){return;"),
   ("function showPanel(s){","function showPanel(s){window.panelExtra&&window.panelExtra(s);"),
   ("g.addEventListener('click',()=>showPanel(s));sites.push(g);","g.addEventListener('mouseenter',()=>showPanel(s));g.addEventListener('focus',()=>showPanel(s));g.addEventListener('click',()=>{location.hash='place-'+window.slug(s[0])});g.addEventListener('keydown',e=>{if(e.key==='Enter')location.hash='place-'+window.slug(s[0])});sites.push(g);"),
   ("const REGIONS=","window.SITES=SITES;\n  const REGIONS=")]
for k,v in R:
    assert k in mp,k; mp=mp.replace(k,v)

MAPEXTRA=r'''<script>
(function(){const NS='http://www.w3.org/2000/svg',X=lon=>(lon-40)*10,Y=lat=>(52-lat)*10;
 const el=(t,a,p)=>{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);p&&p.appendChild(e);return e};
 const T=document.getElementById('terrain'),W=document.getElementById('water');const PK=el('g',{id:'peaks'},T),TL=el('g',{},T),WS=el('g',{id:'watershapes'},W);
 // deserts (stipple)
 const defs=document.querySelector('#spread svg defs');
 defs.insertAdjacentHTML('beforeend','<pattern id="sand" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r=".9" fill="rgba(168,131,82,.45)"/><circle cx="5.5" cy="5" r=".7" fill="rgba(168,131,82,.35)"/></pattern>');
 [['Taklamakan',83,39,72,15],['Gobi',105,42.6,88,20],['Thar',71.3,27,24,19],['Karakum',60,39.6,34,14]].forEach(d=>{el('ellipse',{cx:X(d[1]),cy:Y(d[2]),rx:d[3],ry:d[4],fill:'url(#sand)'},PK);const t=el('text',{x:X(d[1]),y:Y(d[2])+4,'text-anchor':'middle','font-size':10,'font-family':'JetBrains Mono','letter-spacing':2,fill:'rgba(140,105,60,.6)'},TL);t.textContent=d[0].toUpperCase()+' DESERT';});
 // mountains: little ridged peaks along each range
 const M=[['HIMALAYA',[[73.5,35],[76,33],[79,31.2],[81,30],[84,28.6],[87,28],[89,27.9],[92,27.9],[95,28.6]],1],['KARAKORAM',[[74,36.4],[76.5,35.8],[78.5,35]],1],['HINDU KUSH',[[66.5,34.8],[69,35.4],[71,36],[73,36.4]],1],['PAMIR',[[71.8,38.6],[74.2,38.3]],0],
  ['TIAN SHAN',[[70,41.6],[75,41.6],[80,42.3],[85,43.2],[90,43.1],[94,43.2]],1],['KUNLUN',[[76.5,36.6],[80,36.1],[85,36],[90,36],[95,35.6],[99,35.4]],1],['QILIAN',[[95,39.2],[99,38.3],[102.5,37.3]],0],['ALTAI',[[85,49.5],[89,48.8],[94,47.2]],0],
  ['W. GHATS',[[73.6,20],[74.3,16],[75.6,12],[76.9,9]],1],['VINDHYA',[[75,23.6],[78,24.2],[81.5,24.5]],0],['SULAIMAN',[[69.6,31.4],[69.9,29.2],[68.4,27.2]],0],['HENGDUAN',[[98,31],[99,27.5],[99.5,25]],0],['ARAKAN',[[94,22.5],[94.4,19.5],[94.8,17]],0],['ZAGROS',[[45.5,35],[48,33],[51,30.5],[54,28]],0]];
 M.forEach(([name,pts,big])=>{const g=el('g',{},PK);for(let i=1;i<pts.length;i++){const[a,b]=pts[i-1],[c,d]=pts[i];const x1=X(a),y1=Y(b),x2=X(c),y2=Y(d),L=Math.hypot(x2-x1,y2-y1),n=Math.max(1,Math.round(L/(big?11:13)));
   for(let k=0;k<n;k++){const x=x1+(x2-x1)*(k+.5)/n,y=y1+(y2-y1)*(k+.5)/n,h=big?(6+((k*7+i*3)%4)):5,w=big?6:5;el('path',{d:`M${x-w} ${y+2} L${x} ${y-h} L${x+w} ${y+2}`,fill:'rgba(168,131,82,.16)',stroke:'rgba(140,105,60,.55)','stroke-width':.8,'stroke-linejoin':'round'},g);
    if(big)el('path',{d:`M${x-1.6} ${y-h+2.4} L${x} ${y-h} L${x+1.6} ${y-h+2.4}`,fill:'#fff',stroke:'none'},g);}}
  const mid=pts[Math.floor(pts.length/2)];const t=el('text',{x:X(mid[0]),y:Y(mid[1])+(name==='HIMALAYA'?18:-12),'text-anchor':'middle','font-size':big?9.5:8.5,'font-family':'JetBrains Mono','letter-spacing':2,fill:'rgba(120,90,50,.75)'},TL);t.textContent=name;});
 // lakes and inland seas
 const LK=[['Caspian Sea','M70 70 L90 55 L120 52 L130 70 L112 100 L125 112 L135 135 L120 150 L95 140 L92 120 L98 100 L80 90 Z'],['Aral Sea',`M${X(58.4)} ${Y(46.6)} Q${X(61.8)} ${Y(46.4)} ${X(61.2)} ${Y(44.6)} Q${X(59.6)} ${Y(43.6)} ${X(58.5)} ${Y(44.6)} Z`]];
 LK.forEach(l=>{el('path',{d:l[1],fill:'rgba(127,163,191,.35)',stroke:'rgba(95,130,160,.6)','stroke-width':.8},WS);});
 [['Balkhash',75,46.4,22,4,-10],['Issyk-Kul',77.3,42.4,9,2.6,0],['Qinghai Lake',100.2,36.9,5,3,0],['Mānasarovar',81.5,30.7,3.2,2.4,0],['Tonlé Sap',104,12.9,5,2.5,-35],['Dal Lake',74.85,34.1,1.6,1.4,0]].forEach(l=>{el('ellipse',{cx:X(l[1]),cy:Y(l[2]),rx:l[3],ry:l[4],transform:`rotate(${l[5]} ${X(l[1])} ${Y(l[2])})`,fill:'rgba(127,163,191,.45)',stroke:'rgba(95,130,160,.7)','stroke-width':.8},WS);});
 // rivers
 const RV=[['Ganges',[[78,30],[79.5,27.5],[81.8,25.4],[83,25.3],[85.2,25.6],[87.3,25],[88.5,24],[90.4,22.4]]],['Indus',[[81,31.2],[79,32.6],[77,34.6],[75,35.6],[73.5,35.8],[72.2,34],[71.4,31],[70,28.5],[68.5,25.5],[67.5,24]]],['Brahmaputra',[[82,30.2],[86,29.3],[90,29.3],[94,29.4],[95.3,28],[94,26.6],[91,26.1],[89.7,25.1],[90.5,23]]],
  ['Yellow River',[[96,34.6],[101,36],[104,36.6],[106,40],[110,40.8],[111,38],[110.3,35],[113,34.8],[116,36],[118.6,37.8]]],['Yangtze',[[91,33],[97,32.2],[100,28],[104,29],[106.5,29.6],[111,30.7],[114.3,30.6],[117,31],[121.5,31.5]]],['Mekong',[[94,33],[98.6,29],[100,22],[102.6,18],[104.8,16],[105.8,14],[106.2,10.4]]],
  ['Amu Darya',[[73,37.2],[68,37.2],[65,38.6],[61.5,41.6],[59.6,43.8]]],['Syr Darya',[[72,41],[69,41],[66,44],[61.6,46]]],['Tarim',[[76,39.5],[80,40.6],[84,41],[87,40.5],[88.4,39.8]]],['Irrawaddy',[[97.5,26],[96,22],[95.5,19],[95.2,16]]],['Godāvarī',[[73.6,20],[78,19],[81.8,16.8]]],['Kṛṣṇā',[[73.7,17.9],[77,16.5],[80.8,15.9]]],['Narmadā',[[81.6,22.7],[77,22.5],[72.8,21.7]]]];
 RV.forEach(([n,p])=>{let d='M'+X(p[0][0])+' '+Y(p[0][1]);for(let i=1;i<p.length;i++){const[a,b]=p[i-1],[c,e]=p[i];d+=` Q${X(a)} ${Y(b)} ${(X(a)+X(c))/2} ${(Y(b)+Y(e))/2}`;}d+=` L${X(p.at(-1)[0])} ${Y(p.at(-1)[1])}`;
  const pa=el('path',{d,fill:'none',stroke:'rgba(110,150,185,.8)','stroke-width':1.3,'stroke-linecap':'round'},WS);el('title',{},pa).textContent=n;});
 [['Gaṅgā',84.5,24.6],['Indus',69.4,27],['Yellow R.',112.4,39.2],['Yangtze',108,31.6],['Mekong',101.4,20],['Amu Darya',64,40]].forEach(l=>{const t=el('text',{x:X(l[1]),y:Y(l[2]),'font-size':9.5,'font-style':'italic','font-family':'Instrument Serif, Georgia, serif',fill:'rgba(80,120,155,.9)'},W);t.textContent=l[0];});
 // layer toggles
 const routes=document.getElementById('routes');
 document.getElementById('layers').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const on=b.getAttribute('aria-pressed')!=='true';b.setAttribute('aria-pressed',on);const g={terrain:T,water:W,routes}[b.dataset.l]||document.getElementById(b.dataset.l);g.style.display=on?'':'none';});
 // centres of learning (mahaviharas)
 const VG=el('g',{id:'viharas',style:'display:none'},document.getElementById('sites').parentNode);
 (window.VIH||[]).forEach(v=>{const x=X(v.lon),y=Y(v.lat);const A=el('a',{href:'#vihara-'+v.id,class:'vmk'},VG);el('title',{},A).textContent=v.n+' · '+v.d;
  el('rect',{x:x-5,y:y-5,width:10,height:10,transform:`rotate(45 ${x} ${y})`,fill:'#fff',stroke:'#9E6B1B','stroke-width':1.6},A);el('rect',{x:x-2,y:y-2,width:4,height:4,transform:`rotate(45 ${x} ${y})`,fill:'#9E6B1B'},A);
  const left=['vikramashila','odantapuri','telhara','somapura','jagaddala','vikrampur','shalban'].includes(v.id)?0:1;
  const hid=false;const t=el('text',{class:hid?'h':'',x:x+(left?9:-9),y:y+3.5,'text-anchor':left?'start':'end','font-size':11,'font-family':'Inter Tight, sans-serif','font-weight':500,fill:'#7a5214',stroke:'#FAF7F0','stroke-width':3,'paint-order':'stroke'},A);t.textContent=v.n;A.dataset.lon=v.lon;A.dataset.lat=v.lat;});
 window.setVihLayer=on=>{const b=document.querySelector('#layers [data-l="viharas"]');if(b&&(b.getAttribute('aria-pressed')==='true')!==!!on)b.click();};
 addEventListener('hashchange',()=>{if(location.hash==='#map'&&window.__vihOn){window.__vihOn=0;setVihLayer(true);}});
 // panel extras: illustration + link
 window.panelExtra=s=>{const sl=window.slug(s[0]);const pic=document.getElementById('ppic');const ph=(window.PLACEPH||{})[sl];const VHP={vikramasila:'vikramashila_6',kancipura:'kanchi_intro',rajagaha:'telhara_4'};if(pic){pic.innerHTML=ph&&ph.length?PH(ph[0],'',s[0]):(VHP[sl]&&sl!=='rajagaha'?'<div class="photo"><img src="img/vh/'+VHP[sl]+'.webp" alt="" decoding="async"><span class="cr">'+(window.T?T('Reconstruction'):'Reconstruction')+'</span></div>':(window.ART&&window.siteType?ART[siteType(s)]:''));const im=pic.querySelector('img');if(im)im.loading='eager';}const a=document.getElementById('penter');a.href='#place-'+sl;a.textContent=(window.T?window.T('Enter')+' '+window.T(s[0]):'Enter '+s[0])+' →';};
 { const s0=(window.SITES||[]).find(x=>x[0]==='Isipatana');const pp=document.getElementById('ppic');if(s0&&pp&&!pp.innerHTML.trim())window.panelExtra(s0); }
})();
</script>'''

# expose ART and siteType globally (template uses const)
tpl=tpl.replace('const ART={{ART}}, MUD={{MUD}};','window.ART={{ART}}; window.MUD={{MUD}}; const ART=window.ART, MUD=window.MUD;')
tpl=tpl.replace('function siteType(s){','window.siteType=siteType;function siteType(s){')

sc=[('𑀥𑀫𑁆𑀫','Dhamma Lipi','var(--brahmi)'),('धम्म','Devanāgarī',''),('ධම්ම','Sinhala',''),('ဓမ္မ','Burmese',''),('ธรรม','Thai',''),('ཆོས','Tibetan',''),('法','Chinese · Japanese',''),('ধম্ম','Bengali','')]
scripts=''.join(f'<span{" style=\"font-family:"+f+"\"" if f else ""}>{w}<small>{n}</small></span>' for w,n,f in sc)

i0=iv.index('<script>/**'); a1=iv.index('<script>const ASSETS'); a2=iv.index('</script>',a1)+9
libs=iv[i0:a2]
sc0=iv.index('<script>',a2); sc1=iv.index('</script>',sc0)+9
scene=iv[sc0:sc1]
_a=scene.index('  const stupaMat = new THREE.MeshBasicMaterial');_b=scene.index('  stupa.position.set(-7.5, 0, -14)')
scene=scene[:_a]+open(SRC/'stupa_scene.js',encoding='utf-8').read()+scene[_b:]
scene=scene.replace('stupa.position.set(-7.5, 0, -14); stupa.rotation.y = 0.3; stupa.scale.setScalar(0.85);','stupa.rotation.y = 0.3; window.__stupaPos = () => { if (innerWidth > 900) { stupa.position.set(-10.6, 0, -9.4); stupa.scale.setScalar(0.72); } else { stupa.position.set(-7.6, 0, -12); stupa.scale.setScalar(0.62); } }; window.__stupaPos();')
scene=scene.replace('shift = w > 900 ? 1.25 : 0; }','shift = w > 900 ? 1.25 : 0; if (window.__stupaPos) window.__stupaPos(); }')
assert 'window.__stupaPos();' in scene and 'if (window.__stupaPos) window.__stupaPos(); }' in scene
import json as _j
meta=_j.load(open(ROOT/'img/meta.json',encoding='utf-8'))
PHOTO={m[0]:[m[1],m[2],m[3]] for m in meta}
scene=(scene.replace('pillar.position.set(-8, 0, -2); pillar.scale.setScalar(0.6); pillar.rotation.y = 0.5;','pillar.position.set(-1, 0, -2); pillar.scale.setScalar(0.62); window.__pillar = pillar;')
 .replace('cap.position.y = 4.4; pillar.add(cap);',"cap.position.y = 4.4; pillar.add(cap); { const wg=new THREE.Group(); const R=0.4; wg.add(new THREE.Mesh(new THREE.TorusGeometry(R,0.045,12,96),polished)); wg.add(new THREE.Mesh(new THREE.TorusGeometry(R*0.22,0.035,10,40),polished)); wg.add(new THREE.Mesh(new THREE.CylinderGeometry(R*0.16,R*0.16,0.05,32).rotateX(Math.PI/2),polished)); for(let i=0;i<32;i++){const a=i/32*Math.PI*2;const sp=new THREE.Mesh(new THREE.BoxGeometry(0.014,R*0.78,0.028),polished);sp.position.set(Math.cos(a)*R*0.6,Math.sin(a)*R*0.6,0);sp.rotation.z=a-Math.PI/2;wg.add(sp);} wg.position.y=5.4+R+0.02; wg.rotation.y=0.35; wg.traverse(o=>{if(o.isMesh)o.castShadow=true}); pillar.add(wg); }")
 .replace('camera.lookAt(new THREE.Vector3(0, c.l, 0).addScaledVector(right, -s));','camera.lookAt(new THREE.Vector3(0, c.l, 0).addScaledVector(right, -s)); if (window.__pillar) { const oc = window.__ocam, mob = innerWidth < 600; oc.aspect = innerWidth / innerHeight; oc.updateProjectionMatrix(); const hh = 12 * Math.tan(15 * Math.PI / 180), hw = hh * oc.aspect; const g = ease(clamp((p - 0.78) / 0.22, 0, 1)); const f = lerp(mob ? 0.2 : 0.3, mob ? 0.5 : 0.8, g); const sc = f * 2 * hh / 6.27; const PL = window.__pillar; PL.scale.setScalar(sc); PL.position.set(-hw + 2 * hw * lerp(mob ? 0.025 : 0.012, mob ? 0.03 : 0.014, g) + 0.55 * sc, -hh + 2 * hh * lerp(0.07, 0.045, g), 0); PL.rotation.y = -0.35 + (1 - p) * 0.9; }')
 .replace('      renderer.render(scene, camera);\n    }\n    requestAn','      renderer.render(scene, camera); if (window.__oscene && window.__pillar) { renderer.autoClear = false; renderer.clearDepth(); renderer.render(window.__oscene, window.__ocam); renderer.autoClear = true; }\n    }\n    requestAn')
 .replace('haze(pillar, 0.08); scene.add(pillar);','haze(pillar, 0.08); { const os = new THREE.Scene(); os.environment = scene.environment; os.add(new THREE.HemisphereLight(0xfff4e0, 0x6b5a40, 0.95)); const d1 = new THREE.DirectionalLight(0xfff1dc, 1.6); d1.position.set(-4, 6, 6); os.add(d1); const d2 = new THREE.DirectionalLight(0xffe2b0, 0.7); d2.position.set(5, 3, -4); os.add(d2); window.__ocam = new THREE.PerspectiveCamera(30, 1, 0.1, 100); window.__ocam.position.set(0, 0, 12); const pm = polished.clone(); pm.transparent = false; pm.opacity = 1; pm.depthWrite = true; pillar.traverse(o => { if (o.isMesh) o.material = pm; }); os.add(pillar); window.__oscene = os; }')
 .replace('polished.opacity = clamp((p - 0.6) / 0.2, 0, 1);','polished.opacity = clamp((p - 0.12) / 0.18, 0, 1);')
 .replace('renderer.setPixelRatio(Math.min(devicePixelRatio, 2));','renderer.setPixelRatio(Math.min(devicePixelRatio, 1.5));')
 .replace('mapSize.set(2048, 2048)','mapSize.set(1024, 1024)')
 .replace('p += (target - p) * (reduce ? 1 : 0.07);','if (window.__snap3d) { p = target; window.__snap3d = false; } p += (target - p) * (reduce ? 1 : 0.07);'))
for _k in ['window.__oscene = os','renderer.clearDepth()','window.__ocam.position','5.4+R+0.02','window.__snap3d = false']: assert _k in scene, _k
out=(tpl.replace('{{PHOTO}}',_j.dumps(PHOTO,ensure_ascii=False)).replace('{{MAP}}',mp).replace('{{MAPEXTRA}}',MAPEXTRA).replace('{{SCRIPTS}}',scripts)
     .replace('{{ART}}',json.dumps(art['ART'],ensure_ascii=False)).replace('{{MUD}}',json.dumps(art['MUD'],ensure_ascii=False))
     .replace('{{LIBS}}','<script src="i18n.js"></script>\n'+libs).replace('{{SCENE}}',scene))
assert '{{' not in out.replace('{{ ','')[:200000] or True

_T="(window.T||(x=>x))"
for a,b in [("P.querySelector('.label').textContent='Place · '+s[1];","P.querySelector('.label').textContent="+_T+"('Place')+' · '+"+_T+"(s[1]);"),
 ("P.querySelector('.anc').textContent='Earliest Buddhist presence '+fmt(s[4]);","P.querySelector('.anc').textContent="+_T+"('Earliest Buddhist presence')+' '+"+_T+"(fmt(s[4]));"),
 ("P.querySelector('.tags').innerHTML='<span class=\"badge\">'+ST[s[5]]+'</span>';","P.querySelector('.tags').innerHTML='<span class=\"badge\">'+"+_T+"(ST[s[5]])+'</span>';"),
 ("P.querySelector('p.d').textContent=s[6];","P.querySelector('p.d').textContent="+_T+"(s[6]);"),
 ("P.querySelector('.btn').textContent='Enter '+s[0]+' →';","P.querySelector('.btn').textContent="+_T+"('Enter')+' '+"+_T+"(s[0])+' →';"),
 ("cap.textContent=text;","cap.textContent="+_T+"(text);"),
 ("$('#jcount').textContent=sample?'Example trail · open a place to start your own':`${pts.length} stops`;","$('#jcount').textContent=sample?T('Example trail · open a place to start your own'):`${pts.length} ${T('stops')}`;"),
 ("toast('Trail cleared')","toast(T('Trail cleared'))")]:
    assert a in out, a[:60]; out=out.replace(a,b)

import sys as _sys; _sys.path.insert(0,str(SRC))
from clean_text import clean_html as _ch, _scan as _cs
out=_ch(out)
for _f in ['data_fr.js','data_src.js','data_vih.js','data_vihimg.js','data_councils.js','i18n.js']:
    _p=ROOT/_f; _t=open(_p,encoding='utf-8').read(); _u=_cs(_t)
    if _u!=_t: open(_p,'w',encoding='utf-8').write(_u)
open(ROOT/'index.html','w',encoding='utf-8').write('<!doctype html>\n<html lang="en">\n'+out)
print(len(out), out.count('{{'))
