// Footer year
document.getElementById('year').textContent = new Date().getFullYear();

// Sticky header shadow on scroll
const header = document.querySelector('.site-header');
const onScroll = () => {
  if (window.scrollY > 8) header.classList.add('scrolled');
  else header.classList.remove('scrolled');
};
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Reveal-on-scroll
const revealTargets = document.querySelectorAll(
  '.hero-title, .hero-sub, .hero-actions, .hero-meta, .section-header, .col-label, .col-body, .card, .team-card, .pipeline > li, .exec-card, .strat-card, .contact-card'
);
revealTargets.forEach(el => el.classList.add('reveal'));

const io = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in');
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

revealTargets.forEach(el => io.observe(el));
