/* Shared prototype behaviour — Atterer redesign */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* Header: shadow after scroll, hide on scroll down */
  const header = $('[data-header]');
  if (header) {
    let last = scrollY;
    const onScroll = () => {
      const y = scrollY;
      header.classList.toggle('is-scrolled', y > 8);
      if (!document.body.classList.contains('menu-open')) {
        header.classList.toggle('is-hidden', y > 400 && y > last + 4);
        if (y < last - 4) header.classList.remove('is-hidden');
      }
      last = y;
    };
    addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* Mobile menu */
  const burger = $('[data-burger]');
  const panel = $('[data-mobile-nav]');
  if (burger && panel) {
    document.body.appendChild(panel); /* fullscreen: escape header's containing block */
    const set = (open) => {
      if (open && header) { header.classList.remove('is-hidden'); panel.style.setProperty('--mtop', (Math.max(0, header.getBoundingClientRect().top) + header.offsetHeight) + 'px'); }
      document.body.classList.toggle('menu-open', open);
      burger.setAttribute('aria-expanded', open);
      panel.toggleAttribute('inert', !open);
    };
    panel.setAttribute('inert', '');
    burger.addEventListener('click', () => set(!document.body.classList.contains('menu-open')));
    addEventListener('keydown', (e) => e.key === 'Escape' && set(false));
    $$('[data-acc]', panel).forEach((btn) => {
      btn.addEventListener('click', () => {
        const open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', !open);
        btn.nextElementSibling.style.height = open ? '0px' : btn.nextElementSibling.scrollHeight + 'px';
      });
    });
  }

  /* Desktop dropdowns: keyboard support (hover handled in CSS) */
  $$('[data-dd]').forEach((li) => {
    const btn = $('button', li);
    if (!btn) return;
    btn.addEventListener('click', () => {
      const open = li.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open);
    });
    li.addEventListener('focusout', (e) => {
      if (!li.contains(e.relatedTarget)) { li.classList.remove('is-open'); btn.setAttribute('aria-expanded', false); }
    });
  });

  /* Reveal (used sparingly, only where marked) */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -12% 0px' });
  $$('[data-reveal]').forEach((el) => (reduce ? el.classList.add('in') : io.observe(el)));

  /* Count-up numbers */
  const fmt = (n) => n.toLocaleString('de-DE');
  const cio = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      const el = en.target; cio.unobserve(el);
      const target = parseInt(el.dataset.count.replace(/\./g, ''), 10);
      if (reduce || target < 100 || el.dataset.count.length === 4 && !el.dataset.count.includes('.')) { el.textContent = el.dataset.count; return; }
      const t0 = performance.now(), dur = 1400;
      const tick = (t) => {
        const p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
        el.textContent = fmt(Math.round(target * e));
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  }, { threshold: 0.6 });
  $$('[data-count]').forEach((el) => cio.observe(el));

  /* Filters (job list) */
  $$('[data-filter-group]').forEach((group) => {
    const target = $(group.dataset.filterGroup);
    $$('button', group).forEach((b) => b.addEventListener('click', () => {
      $$('button', group).forEach((x) => x.setAttribute('aria-pressed', x === b));
      const f = b.dataset.filter;
      $$('[data-kind]', target).forEach((item) => {
        const show = f === 'all' || item.dataset.kind === f;
        item.classList.toggle('is-filtered', !show);
      });
      const count = $$('[data-kind]:not(.is-filtered)', target).length;
      const out = $('[data-filter-count]'); if (out) out.textContent = count;
    }));
  });

  /* Lightbox */
  const imgs = $$('[data-lightbox]');
  if (imgs.length) {
    const box = document.createElement('div');
    box.className = 'plb'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-modal', 'true'); box.hidden = true;
    box.innerHTML = '<button class="plb-x" aria-label="Schließen">×</button><button class="plb-p" aria-label="Vorheriges Bild">‹</button><img alt=""><button class="plb-n" aria-label="Nächstes Bild">›</button><span class="plb-c"></span>';
    document.body.append(box);
    let i = 0;
    const show = (n) => { i = (n + imgs.length) % imgs.length; $('img', box).src = imgs[i].dataset.lightbox || imgs[i].src; $('.plb-c', box).textContent = (i + 1) + ' / ' + imgs.length; };
    const close = () => { box.classList.remove('on'); setTimeout(() => (box.hidden = true), 250); };
    imgs.forEach((im, n) => { im.style.cursor = 'zoom-in'; im.addEventListener('click', () => { box.hidden = false; show(n); requestAnimationFrame(() => box.classList.add('on')); $('.plb-x', box).focus(); }); });
    $('.plb-x', box).onclick = close; $('.plb-p', box).onclick = () => show(i - 1); $('.plb-n', box).onclick = () => show(i + 1);
    box.addEventListener('click', (e) => e.target === box && close());
    addEventListener('keydown', (e) => { if (box.hidden) return; if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(i - 1); if (e.key === 'ArrowRight') show(i + 1); });
  }

  /* Rails: arrow buttons only */
  $$('[data-rail]').forEach((rail) => {
    let box = rail.parentElement, nav = null;
    while (box && box !== document.body && !(nav = box.querySelector('[data-rail-nav]'))) box = box.parentElement;
    if (!nav) return;
    const prev = $('[data-prev]', nav), next = $('[data-next]', nav);
    const step = () => Math.max(rail.clientWidth * 0.7, 260);
    prev.addEventListener('click', () => rail.scrollBy({ left: -step(), behavior: reduce ? 'auto' : 'smooth' }));
    next.addEventListener('click', () => rail.scrollBy({ left: step(), behavior: reduce ? 'auto' : 'smooth' }));
    const sync = () => {
      const max = rail.scrollWidth - rail.clientWidth - 2;
      prev.disabled = rail.scrollLeft <= 2; next.disabled = rail.scrollLeft >= max;
    };
    rail.addEventListener('scroll', sync, { passive: true }); addEventListener('resize', sync); sync();
  });

  /* Table of contents: highlight the section in view */
  const tocLinks = $$('.toc a[href^="#"]').filter((a) => a.getAttribute('href').length > 1);
  if (tocLinks.length) {
    const pairs = tocLinks.map((a) => [a, document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)))]).filter((p) => p[1]);
    let ticking = false;
    const spy = () => {
      ticking = false;
      const line = Math.min(innerHeight * 0.35, 220);
      let cur = pairs[0];
      for (const p of pairs) if (p[1].getBoundingClientRect().top <= line) cur = p;
      if (innerHeight + scrollY >= document.documentElement.scrollHeight - 4) cur = pairs[pairs.length - 1];
      pairs.forEach((p) => { const on = p === cur; p[0].classList.toggle('is-active', on); on ? p[0].setAttribute('aria-current', 'location') : p[0].removeAttribute('aria-current'); });
    };
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(spy); } }, { passive: true });
    addEventListener('resize', spy); spy();
  }

  /* Contact form (prototype: no sending) */
  $$('form[data-proto]').forEach((f) => f.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!f.checkValidity()) { f.reportValidity(); return; }
    f.classList.add('is-sent');
    const ok = $('[data-sent]', f); if (ok) { ok.hidden = false; ok.focus(); }
  }));

  /* Pages that are not part of this preview stage */
  const built = (document.body.dataset.built || '').split(',').filter(Boolean);
  let toastEl;
  const toast = (msg) => {
    if (!toastEl) { toastEl = document.createElement('div'); toastEl.className = 'toast'; toastEl.setAttribute('role', 'status'); document.body.append(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add('on'); clearTimeout(toastEl._t); toastEl._t = setTimeout(() => toastEl.classList.remove('on'), 2600);
  };
  if (built.length) {
    $$('a[href]').forEach((a) => {
      const h = a.getAttribute('href');
      if (/^(https?:|mailto:|tel:|#)/.test(h)) return;
      const page = h.split('#')[0];
      if (page && !built.includes(page)) a.addEventListener('click', (e) => { e.preventDefault(); toast('Diese Seite entsteht nach der Wahl der Richtung.'); });
    });
  }

  /* Scroll-linked parallax for marked images */
  if (!reduce) {
    const par = $$('[data-parallax]');
    if (par.length) {
      const run = () => { par.forEach((el) => { const r = el.parentElement.getBoundingClientRect(); const p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight; el.style.transform = `translate3d(0, ${p * -6}%, 0) scale(1.12)`; }); };
      addEventListener('scroll', () => requestAnimationFrame(run), { passive: true }); run();
    }
  }
})();
/* Two-click map: load Google Maps only after consent */
document.querySelectorAll('[data-map-load]').forEach((btn) => btn.addEventListener('click', () => {
  const box = btn.closest('[data-map]');
  const f = document.createElement('iframe');
  f.src = btn.dataset.mapLoad; f.title = 'Google Maps – Atterer Stahlcenter'; f.loading = 'lazy'; f.allowFullscreen = true;
  f.referrerPolicy = 'no-referrer-when-downgrade';
  box.innerHTML = ''; box.append(f); box.classList.add('is-loaded');
}));
/* Smooth <details> */
document.querySelectorAll('details[data-acc-d]').forEach((d) => {
  const s = d.querySelector('summary'), body = d.querySelector('.acc-b');
  s.addEventListener('click', (e) => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    e.preventDefault();
    if (d.open) { body.style.height = body.scrollHeight + 'px'; requestAnimationFrame(() => { body.style.height = '0px'; }); setTimeout(() => { d.open = false; body.style.height = ''; }, 300); }
    else { d.open = true; const h = body.scrollHeight; body.style.height = '0px'; requestAnimationFrame(() => { body.style.height = h + 'px'; }); setTimeout(() => { body.style.height = ''; }, 320); }
  });
});
