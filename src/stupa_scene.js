  /* Sāñcī Great Stupa (Stupa 1), proportions from the monument: dome c. 36.6 m across,
     ground railing c. 43.6 m across, gateways c. 10.4 m high. 1 unit = c. 4.8 m. */
  const stupaMat = new THREE.MeshStandardMaterial({ color: 0xCBB592, roughness: 0.92, metalness: 0, transparent: true, opacity: 0, emissive: 0x2a1d0c, emissiveIntensity: 0.18 }); stupaMat.color.convertSRGBToLinear();
  const stupa = new THREE.Group();
  const add = (g, x, y, z, ry) => { const m = new THREE.Mesh(g, stupaMat); m.position.set(x, y, z); if (ry) m.rotation.y = ry; stupa.add(m); return m; };
  const DOME = 3.8, RAIL = 4.55, MEDHI = 0.9;
  // paved terrace
  add(new THREE.CylinderGeometry(RAIL + 0.9, RAIL + 1.0, 0.08, 96), 0, 0.04, 0);
  // medhi: raised drum with its own railing (the upper walkway)
  add(new THREE.CylinderGeometry(DOME + 0.55, DOME + 0.62, MEDHI, 96), 0, MEDHI / 2, 0);
  add(new THREE.TorusGeometry(DOME + 0.5, 0.035, 6, 160), 0, MEDHI + 0.22, 0).rotation.x = Math.PI / 2;
  for (let i = 0; i < 90; i++) { const a = i / 90 * Math.PI * 2; add(new THREE.BoxGeometry(0.05, 0.24, 0.05), Math.cos(a) * (DOME + 0.5), MEDHI + 0.11, Math.sin(a) * (DOME + 0.5)); }
  // double staircase on the south side, rising to the walkway
  [-1, 1].forEach(s => { for (let k = 0; k < 6; k++) { add(new THREE.BoxGeometry(0.13, 0.15 * (k + 1), 0.22), s * (0.25 + k * 0.13), 0.075 * (k + 1), DOME + 0.68); } });
  // anda: a slightly flattened hemisphere
  const dome = add(new THREE.SphereGeometry(DOME, 96, 48, 0, Math.PI * 2, 0, Math.PI / 2), 0, MEDHI, 0); dome.scale.y = 0.74;
  const sTop = MEDHI + DOME * 0.74;
  // harmika: square railing on the summit, then the triple umbrella (chhatra)
  add(new THREE.BoxGeometry(1.15, 0.08, 1.15), 0, sTop + 0.02, 0);
  for (let i = 0; i < 4; i++) { const a = i * Math.PI / 2; const r = add(new THREE.BoxGeometry(1.1, 0.34, 0.07), Math.cos(a) * 0.53, sTop + 0.22, Math.sin(a) * 0.53); r.rotation.y = -a + Math.PI / 2; }
  add(new THREE.BoxGeometry(1.2, 0.06, 1.2), 0, sTop + 0.42, 0);
  add(new THREE.CylinderGeometry(0.06, 0.07, 1.3, 12), 0, sTop + 0.95, 0);
  [[0.62, 0.62], [0.5, 0.98], [0.38, 1.3]].forEach(([r, y]) => { add(new THREE.CylinderGeometry(r * 0.92, r, 0.07, 48), 0, sTop + y, 0); });
  // ground railing (vedikā): posts, three lens-shaped crossbars, coping; open at the four gates
  const gap = 0.16;
  for (let i = 0; i < 132; i++) {
    const a = i / 132 * Math.PI * 2; const d = Math.min(...[0, 1, 2, 3, 4].map(q => Math.abs(a - q * Math.PI / 2)));
    if (d < gap) continue;
    add(new THREE.BoxGeometry(0.1, 0.62, 0.1), Math.cos(a) * RAIL, 0.31, Math.sin(a) * RAIL);
  }
  for (let q = 0; q < 4; q++) {
    const a0 = q * Math.PI / 2 + gap, len = Math.PI / 2 - 2 * gap;
    [0.17, 0.32, 0.47].forEach(y => { const b = add(new THREE.TorusGeometry(RAIL, 0.03, 4, 60, len), 0, y, 0); b.rotation.x = Math.PI / 2; b.rotation.z = a0; });
    const cop = add(new THREE.TorusGeometry(RAIL, 0.065, 8, 60, len), 0, 0.65, 0); cop.rotation.x = Math.PI / 2; cop.rotation.z = a0;
  }
  // toraṇas at the four cardinal points, standing just outside the railing openings
  function torana(a) {
    const g = new THREE.Group(); const m = (geo, x, y, z) => { const o = new THREE.Mesh(geo, stupaMat); o.position.set(x, y, z); g.add(o); return o; };
    const W = 0.36, H = 2.16; // half the clear width, total height
    // two square pillars, rising unbroken from the ground through all three architraves
    [-W, W].forEach(x => {
      m(new THREE.BoxGeometry(0.15, 1.5, 0.15), x, 0.75, 0);
      m(new THREE.BoxGeometry(0.24, 0.22, 0.22), x, 1.56, 0);            // capital (elephants / lions / dwarfs)
      m(new THREE.BoxGeometry(0.13, 0.62, 0.13), x, 1.98, 0);            // die blocks between the architraves
    });
    // three architraves, gently curved, ends rolled into spirals beyond the pillars
    [1.72, 2.02, 2.32].forEach((y, i) => {
      const span = 0.72 + 0.04 * i;
      const arc = new THREE.Mesh(new THREE.TorusGeometry(4.2, 0.065, 6, 40, (2 * span) / 4.2), stupaMat);
      arc.position.set(0, y - 4.2 + 0.03, 0); arc.rotation.z = Math.PI / 2 - span / 4.2; arc.scale.z = 1.4; g.add(arc);
      [-1, 1].forEach(s => { const v = m(new THREE.TorusGeometry(0.07, 0.03, 6, 20), s * (span + 0.03), y - 0.035, 0); v.rotation.y = 0; });
      if (i < 2) for (let k = -2; k <= 2; k++) m(new THREE.BoxGeometry(0.035, 0.18, 0.06), k * 0.13, y + 0.15, 0); // small balusters
    });
    // finials: Dharma wheel at the centre, triratna on the pillars
    const wh = m(new THREE.TorusGeometry(0.13, 0.025, 6, 32), 0, 2.56, 0);
    m(new THREE.BoxGeometry(0.03, 0.22, 0.03), 0, 2.56, 0); m(new THREE.BoxGeometry(0.22, 0.03, 0.03), 0, 2.56, 0);
    m(new THREE.BoxGeometry(0.06, 0.12, 0.06), 0, 2.4, 0);
    [-W, W].forEach(x => { m(new THREE.CylinderGeometry(0.05, 0.07, 0.14, 12), x, 2.46, 0); m(new THREE.TorusGeometry(0.05, 0.018, 6, 16, Math.PI), x, 2.55, 0); });
    const r = RAIL + 0.42; g.position.set(Math.cos(a) * r, 0, Math.sin(a) * r); g.rotation.y = -a + Math.PI / 2; stupa.add(g);
  }
  [0, 1, 2, 3].forEach(q => torana(q * Math.PI / 2));
