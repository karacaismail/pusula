
<noscript><style>.rule-pop-body[hidden]{display:block!important}.rule-btns{display:none}</style></noscript>
<script>
/* Kural balonlari: iki icon-only buton, ayni anda tek balon acik, Esc kapatir.
   JS yoksa <noscript> stili balonlari acik gosterir (icerik erisilebilir kalir). */
(function () {
  var btns = Array.prototype.slice.call(document.querySelectorAll(".rule-btn"));
  if (!btns.length) return;

  function panelOf(btn) {
    return document.getElementById(btn.getAttribute("aria-controls"));
  }

  function close(btn) {
    var p = panelOf(btn);
    if (p) p.hidden = true;
    btn.setAttribute("aria-expanded", "false");
  }

  function closeAll(except) {
    btns.forEach(function (b) { if (b !== except) close(b); });
  }

  btns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") === "true";
      closeAll(btn);
      if (open) { close(btn); return; }
      var p = panelOf(btn);
      if (p) p.hidden = false;
      btn.setAttribute("aria-expanded", "true");
    });
  });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var open = btns.filter(function (b) { return b.getAttribute("aria-expanded") === "true"; });
    if (!open.length) return;
    closeAll();
    open[0].focus();
  });
})();
</script>
