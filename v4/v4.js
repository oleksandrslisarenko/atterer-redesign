/* V4 behaviours: header hide/show strip, catalogue tabs + auto rotation, photo pair, document tabs */
(() => {
  const root = document.querySelector('.at-root'); if (!root) return;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let last = scrollY, tick = false;
  addEventListener('scroll', () => { if (tick) return; tick = true; requestAnimationFrame(() => {
    tick = false; const y = scrollY, on = y > 140;
    root.classList.toggle('hs-on', on);
    if (!on) root.classList.remove('hs-up'); else if (y < last - 2) root.classList.add('hs-up'); else if (y > last + 2) root.classList.remove('hs-up');
    last = y; }); }, { passive: true });

  /* catalogue */
  const cat = document.querySelector('[data-cat]');
  if (cat) {
    const tabs = [...cat.querySelectorAll('.ctab')], lists = [...cat.querySelectorAll('.cat-list')];
    const imgs = [...cat.querySelectorAll('.frame img')], cap = cat.querySelector('[data-cap]'), capLink = cat.querySelector('[data-cap-link]'), flink = cat.querySelector('.flink');
    let tab = 0, idx = 0, hover = false;
    const items = () => [...lists[tab].querySelectorAll('.it')];
    const show = (i) => {
      const its = items(); idx = (i + its.length) % its.length; const it = its[idx];
      cat.querySelectorAll('.it').forEach((x) => x.classList.toggle('on', x === it));
      imgs.forEach((im) => im.classList.toggle('on', im.dataset.key === it.dataset.key));
      cap.textContent = it.dataset.cap; capLink.href = flink.href = it.getAttribute('href');
    };
    tabs.forEach((t, i) => t.addEventListener('click', () => {
      tab = i; tabs.forEach((x, j) => x.setAttribute('aria-selected', j === i)); lists.forEach((l, j) => (l.hidden = j !== i)); show(0);
    }));
    cat.querySelectorAll('.it').forEach((it) => { it.addEventListener('mouseenter', () => show(items().indexOf(it))); it.addEventListener('focus', () => show(items().indexOf(it))); });
    cat.addEventListener('mouseenter', () => (hover = true)); cat.addEventListener('mouseleave', () => (hover = false));
    show(0);
    if (!reduce) setInterval(() => { if (!hover) show(idx + 1); }, 3000);
  }

  /* photo pair */
  const pair = document.querySelector('[data-pair]');
  if (pair) {
    let p = 0, hover = false; const n = 3;
    const set = (i) => { p = (i + n) % n; pair.querySelectorAll('[data-p]').forEach((el) => el.classList.toggle('on', +el.dataset.p === p)); };
    pair.querySelector('[data-prev]').onclick = () => set(p - 1);
    pair.querySelector('[data-next]').onclick = () => set(p + 1);
    pair.addEventListener('mouseenter', () => (hover = true)); pair.addEventListener('mouseleave', () => (hover = false));
    if (!reduce) setInterval(() => { if (!hover) set(p + 1); }, 2600);
  }

  /* document tabs */
  document.querySelectorAll('[data-doctabs]').forEach((wrap) => {
    const tabs = [...wrap.querySelectorAll('.ctab')], bodies = [...wrap.querySelectorAll('tbody')];
    tabs.forEach((t, i) => t.addEventListener('click', () => { tabs.forEach((x, j) => x.setAttribute('aria-selected', j === i)); bodies.forEach((b, j) => (b.hidden = j !== i)); }));
  });
})();
