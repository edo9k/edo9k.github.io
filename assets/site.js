/* Eduardo França — CV
   Language toggle. The visual swap is done in CSS via html[lang]; this script
   only flips the attribute, remembers the choice and keeps aria in sync. */

(function () {
  'use strict';

  var STORAGE_KEY = 'cv-lang';
  var SUPPORTED = ['en', 'pt'];
  var root = document.documentElement;
  var switches = document.querySelectorAll('.langswitch__btn');

  function normalize(value) {
    if (SUPPORTED.indexOf(value) !== -1) return value;
    var lang = String(value || '').toLowerCase();
    if (lang.indexOf('pt') === 0) return 'pt';
    if (lang.indexOf('en') === 0) return 'en';
    return null;
  }

  function readStored() {
    try {
      return normalize(localStorage.getItem(STORAGE_KEY));
    } catch (e) {
      return null;
    }
  }

  function store(lang) {
    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch (e) {
      /* private mode / storage disabled — the toggle still works for this page */
    }
  }

  function preferred() {
    /* Portuguese is the primary language; only an explicit past choice overrides it. */
    return readStored() || 'pt';
  }

  function apply(lang, persist) {
    root.lang = lang;

    for (var i = 0; i < switches.length; i++) {
      switches[i].setAttribute('aria-pressed', switches[i].dataset.setLang === lang ? 'true' : 'false');
    }

    if (persist) store(lang);
  }

  for (var i = 0; i < switches.length; i++) {
    (function (btn) {
      btn.addEventListener('click', function () {
        apply(btn.dataset.setLang, true);
      });
    })(switches[i]);
  }

  apply(preferred(), false);

  /* Keep the choice when the visitor follows a link to another page. */
  window.addEventListener('pageshow', function (e) {
    if (e.persisted) apply(preferred(), false);
  });

  /* Print button */
  var printBtn = document.getElementById('print-btn');
  if (printBtn) {
    printBtn.addEventListener('click', function () {
      window.print();
    });
  }

  /* Highlight the nav link for the section currently in view. */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.topnav a[href^="#"]'));
  var sections = navLinks
    .map(function (link) {
      return document.querySelector(link.getAttribute('href'));
    })
    .filter(Boolean);

  if ('IntersectionObserver' in window && sections.length) {
    var visible = new Map();

    var observer = new IntersectionObserver(
      function (records) {
        records.forEach(function (record) {
          visible.set(record.target.id, record.isIntersecting ? record.intersectionRatio : 0);
        });

        var best = null;
        var bestRatio = 0;
        visible.forEach(function (ratio, id) {
          if (ratio > bestRatio) {
            bestRatio = ratio;
            best = id;
          }
        });

        navLinks.forEach(function (link) {
          link.classList.toggle('is-active', best !== null && link.getAttribute('href') === '#' + best);
        });
      },
      { rootMargin: '-20% 0px -55% 0px', threshold: [0, 0.15, 0.4, 0.75, 1] }
    );

    sections.forEach(function (section) {
      observer.observe(section);
    });
  }
})();