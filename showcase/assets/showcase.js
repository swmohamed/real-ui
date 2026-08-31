(() => {
  document.querySelectorAll('[data-toggle]').forEach((control) => {
    control.addEventListener('click', () => {
      const pressed = control.getAttribute('aria-pressed') === 'true';
      control.setAttribute('aria-pressed', String(!pressed));
    });
  });
  document.querySelectorAll('form[data-demo-form]').forEach((form) => {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const status = form.querySelector('[role="status"]');
      if (status) status.textContent = status.dataset.message || 'Selection saved for this demo.';
    });
  });
})();
