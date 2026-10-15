(() => {
  const toggle = document.querySelector('.menu-button');
  const nav = document.querySelector('#rig-nav');
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
  });
  nav.addEventListener('click', event => {
    if (event.target.closest('a')) {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('open')) {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.focus();
    }
  });
  document.querySelector('.copy-email').addEventListener('click', async () => {
    const result = document.querySelector('.copy-result');
    try {
      await navigator.clipboard.writeText('greg.cothran@cognitiveworkstead.com');
      result.textContent = 'Email address copied.';
    } catch {
      result.textContent = 'Select and copy the email address shown above.';
    }
  });
})();
