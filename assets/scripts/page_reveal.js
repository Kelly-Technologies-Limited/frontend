// Reveal page only after fonts + hero background are ready.
// Falls back to a 2.5s timeout so a stalled asset never traps the page.
(function gateReveal() {
  const reveal = () => document.body.classList.add('loaded');
  const ready = [];
  if (document.fonts && document.fonts.ready) ready.push(document.fonts.ready);
  ready.push(new Promise(resolve => {
    const img = new Image();
    img.onload = img.onerror = () => resolve();
    img.src = 'assets/hero-bg.jpg';
  }));
  Promise.all(ready).then(reveal);
  setTimeout(reveal, 2500);
})();
