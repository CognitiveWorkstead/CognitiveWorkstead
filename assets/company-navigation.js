(() => {
  'use strict';
  const header = document.querySelector('[data-cw-navigation]');
  if (!header) return;
  const button = header.querySelector('.cw-menu-toggle');
  const nav = header.querySelector('.cw-primary-nav');
  if (!button || !nav) return;
  const close = (restoreFocus = false) => {
    button.setAttribute('aria-expanded', 'false');
    if (restoreFocus) button.focus();
  };
  header.classList.add('cw-nav-ready');
  button.addEventListener('click', () => {
    button.setAttribute('aria-expanded', String(button.getAttribute('aria-expanded') !== 'true'));
  });
  nav.addEventListener('click', event => { if (event.target.closest('a')) close(); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && button.getAttribute('aria-expanded') === 'true') close(true);
  });
  document.addEventListener('click', event => { if (!header.contains(event.target)) close(); });
  window.matchMedia('(min-width:1180px)').addEventListener('change', () => close());
})();
