// Sidebar toggle, client-side search, active-heading tracking. No dependencies.
(function () {
  'use strict';

  var toggle = document.getElementById('navtoggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', function (e) {
      if (!document.body.classList.contains('nav-open')) return;
      var sb = document.getElementById('sidebar');
      if (sb && !sb.contains(e.target) && e.target !== toggle) {
        document.body.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // ---- search
  var q = document.getElementById('q');
  var results = document.getElementById('results');
  if (q && results) {
    var base = /\/p\//.test(location.pathname) ? '../' : '';
    var data = null, loading = false;

    function load() {
      if (data || loading) return;
      loading = true;
      fetch(base + 'search-index.json')
        .then(function (r) { return r.json(); })
        .then(function (j) { data = j; loading = false; run(); })
        .catch(function () { loading = false; });
    }

    function run() {
      var term = q.value.trim().toLowerCase();
      if (!term) { results.hidden = true; results.innerHTML = ''; return; }
      if (!data) { load(); return; }

      var hits = [];
      data.forEach(function (d) {
        var score = 0, where = '';
        if (d.t.toLowerCase().indexOf(term) > -1) { score += 10; }
        if (d.d.toLowerCase().indexOf(term) > -1) { score += 8; }
        for (var i = 0; i < d.h.length; i++) {
          if (d.h[i].toLowerCase().indexOf(term) > -1) {
            score += 4; if (!where) where = d.h[i];
          }
        }
        if (score) hits.push({ d: d, score: score, where: where });
      });
      hits.sort(function (a, b) { return b.score - a.score; });

      if (!hits.length) {
        results.innerHTML = '<div class="empty">No match.</div>';
        results.hidden = false; return;
      }
      results.innerHTML = hits.slice(0, 12).map(function (h) {
        var sub = h.where ? '<span class="rsub">' + esc(h.where) + '</span>' : '';
        return '<a href="' + base + 'p/' + h.d.s + '.html">' +
          '<span class="rnum">' + h.d.n + '</span>' + esc(h.d.d || h.d.t) + sub + '</a>';
      }).join('');
      results.hidden = false;
    }

    function esc(s) {
      return s.replace(/[&<>"]/g, function (c) {
        return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c];
      });
    }

    q.addEventListener('focus', load);
    q.addEventListener('input', run);
    q.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { q.value = ''; results.hidden = true; q.blur(); }
      if (e.key === 'ArrowDown') {
        var first = results.querySelector('a');
        if (first) { e.preventDefault(); first.focus(); }
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && document.activeElement !== q &&
          !/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)) {
        e.preventDefault(); q.focus();
      }
    });
    document.addEventListener('click', function (e) {
      if (!results.contains(e.target) && e.target !== q) results.hidden = true;
    });
  }

  // ---- active heading in the table of contents
  var links = [].slice.call(document.querySelectorAll('.toc a'));
  if (links.length && 'IntersectionObserver' in window) {
    var map = {};
    links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var seen = [];
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var id = en.target.id;
        var i = seen.indexOf(id);
        if (en.isIntersecting) { if (i < 0) seen.push(id); }
        else if (i > -1) { seen.splice(i, 1); }
      });
      links.forEach(function (a) { a.classList.remove('active'); });
      if (seen.length) {
        var order = links.map(function (a) { return a.getAttribute('href').slice(1); });
        seen.sort(function (a, b) { return order.indexOf(a) - order.indexOf(b); });
        if (map[seen[0]]) map[seen[0]].classList.add('active');
      }
    }, { rootMargin: '-60px 0px -75% 0px' });
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) io.observe(el);
    });
  }
})();
