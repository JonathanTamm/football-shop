document.addEventListener('DOMContentLoaded', function () {
  const root = document.getElementById('toast-component');
  if (!root) return;
  const inner = document.getElementById('toast-inner');
  const icon = document.getElementById('toast-icon');
  const titleEl = document.getElementById('toast-title');
  const msgEl = document.getElementById('toast-message');
  const closeBtn = document.getElementById('toast-close');
  let hideTimer = null;

  function resetVariant() {
    inner.classList.remove(
      'bg-green-600', 'border-green-700',
      'bg-red-600', 'border-red-700',
      'bg-yellow-500', 'border-yellow-600',
      'bg-blue-600', 'border-blue-700',
      'bg-gray-800', 'border-gray-700'
    );
    inner.classList.add('bg-gray-800', 'border-gray-700');
    icon.textContent = '';
  }

  function applyVariant(type) {
    resetVariant();
    if (type === 'success') {
      inner.classList.add('bg-green-600', 'border-green-700');
      icon.textContent = '✔';
    } else if (type === 'error') {
      inner.classList.add('bg-red-600', 'border-red-700');
      icon.textContent = '✖';
    } else if (type === 'warn' || type === 'warning') {
      inner.classList.add('bg-yellow-500', 'border-yellow-600');
      icon.textContent = '⚠';
    } else if (type === 'info') {
      inner.classList.add('bg-blue-600', 'border-blue-700');
      icon.textContent = 'ℹ';
    }
  }

  function show(title = '', message = '', type = 'normal', duration = 3000) {
    if (hideTimer) {
      clearTimeout(hideTimer);
      hideTimer = null;
    }
    titleEl.textContent = title || '';
    msgEl.textContent = message || '';
    applyVariant(type);

    // show
    root.classList.remove('opacity-0', 'translate-y-8', 'pointer-events-none');
    root.classList.add('opacity-100', 'translate-y-0');

    hideTimer = setTimeout(hide, duration);
  }

  function hide() {
    root.classList.remove('opacity-100', 'translate-y-0');
    root.classList.add('opacity-0', 'translate-y-8', 'pointer-events-none');
    if (hideTimer) {
      clearTimeout(hideTimer);
      hideTimer = null;
    }
  }

  if (closeBtn) closeBtn.addEventListener('click', hide);
  root.addEventListener('click', (e) => {
    if (e.target === root) hide();
  });

  // Backward-compatible API:
  // showToast(title, message, type, duration)
  // or showToast({ title, message, type, duration })
  window.showToast = function (a, b, c, d) {
    if (typeof a === 'object' && a !== null) {
      const { title = '', message = '', type = 'normal', duration = 3000 } = a;
      show(title, message, type, duration);
    } else {
      show(a || '', b || '', c || 'normal', d || 3000);
    }
  };
});