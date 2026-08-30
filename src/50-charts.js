<script>
(function () {
  if (typeof echarts === "undefined") return;

  function isDark() {
    var t = document.documentElement.getAttribute("data-theme");
    if (t === "dark") return true;
    if (t === "light") return false;
    try { return window.matchMedia("(prefers-color-scheme: dark)").matches; } catch (e) { return false; }
  }

  var charts = [];
  function mk(id, opt) {
    var el = document.getElementById(id);
    if (!el) return;
    try {
      var c = echarts.init(el, null, { renderer: "canvas" });
      c.setOption(opt);
      charts.push(c);
    } catch (e) {}
  }

  function render() {
    charts.forEach(function (c) { try { c.dispose(); } catch (e) {} });
    charts = [];
    var d = isDark();
    var ink  = d ? "#E4EDEC" : "#182A2C";
    var mut  = d ? "#8FA3A4" : "#5C6F72";
    var grid = d ? "#243A3D" : "#DFE8E6";
    var P    = d ? "#4FC0C8" : "#0E7C86";
    var pal  = d ? ["#4FC0C8", "#8ED0D5", "#D9A441", "#5CBA7D", "#9AA7E0"]
                 : ["#0E7C86", "#57A7AE", "#B07C10", "#2E7D46", "#5B6BB5"];
    var axis = {
      axisLine: { lineStyle: { color: grid } },
      axisLabel: { color: mut, fontSize: 11 },
      splitLine: { lineStyle: { color: grid } }
    };

    mk("chartCost", {
      color: pal,
      textStyle: { color: ink },
      tooltip: { trigger: "item", formatter: "{b}: {c}M $ ({d}%)" },
      series: [{
        type: "pie", radius: ["44%", "70%"], center: ["50%", "46%"],
        itemStyle: { borderRadius: 6, borderColor: d ? "#131C1E" : "#F7FAF9", borderWidth: 2 },
        label: { color: ink, fontSize: 12, formatter: "{b}\n{c}M $" },
        labelLine: { lineStyle: { color: mut } },
        data: [
          { value: 1.6, name: "Miras (2 çocuk)" },
          { value: 1.1, name: "Kendi yaşamın" },
          { value: 2.2, name: "Gelir portföyü" }
        ]
      }]
    });

    mk("chartBridge", {
      color: pal,
      textStyle: { color: ink },
      tooltip: { trigger: "axis", axisPointer: { type: "shadow" }, valueFormatter: function (v) { return v ? v.toLocaleString("tr-TR") + " $" : "—"; } },
      legend: { top: 0, textStyle: { color: mut, fontSize: 11 }, itemWidth: 12, itemHeight: 8, type: "scroll" },
      grid: { left: 8, right: 14, top: 34, bottom: 6, containLabel: true },
      xAxis: Object.assign({}, axis, { type: "category", data: ["Bugün", "Ara 26", "Haz 27", "Ara 27", "2028"] }),
      yAxis: Object.assign({}, axis, { type: "value", axisLabel: { color: mut, fontSize: 11, formatter: function (v) { return (v / 1000) + "K"; } } }),
      series: [
        { name: "Maaş (türksab)", type: "bar", stack: "g", data: [2000, 2000, 2000, 2000, 2000] },
        { name: "titanlar", type: "bar", stack: "g", data: [0, 2800, 3000, 2500, 2000] },
        { name: "Proje işleri", type: "bar", stack: "g", data: [0, 200, 500, 300, 0] },
        { name: "arsam araçları", type: "bar", stack: "g", data: [0, 0, 300, 700, 1500] },
        { name: "DestekTeşvik", type: "bar", stack: "g", data: [0, 0, 0, 800, 3800],
          markLine: { symbol: "none", label: { formatter: "5.000 $ taban", color: ink, fontSize: 11, position: "insideStartTop" },
            lineStyle: { color: P, type: "dashed", width: 1.5 }, data: [{ yAxis: 5000 }] } }
      ]
    });

    mk("chartPath", {
      textStyle: { color: ink },
      tooltip: { trigger: "axis", valueFormatter: function (v) { return v == null ? "—" : v.toLocaleString("tr-TR") + " bin $"; } },
      legend: { top: 0, textStyle: { color: mut, fontSize: 11 }, itemWidth: 14, itemHeight: 8 },
      grid: { left: 8, right: 20, top: 34, bottom: 6, containLabel: true },
      xAxis: Object.assign({}, axis, { type: "category", boundaryGap: false, data: ["2026", "2027", "2028", "2029", "2030", "2031"] }),
      yAxis: Object.assign({}, axis, { type: "value", axisLabel: { color: mut, fontSize: 11, formatter: function (v) { return v >= 1000 ? (v / 1000) + "M" : v; } } }),
      series: [
        {
          name: "5 yıl kuralı (hasat şart)", type: "line", smooth: true, symbol: "circle", symbolSize: 6,
          lineStyle: { color: P, width: 2.5, type: "dashed" },
          itemStyle: { color: P },
          data: [0, 60, 220, 500, 1500, 5000],
          markPoint: {
            symbolSize: 1, label: { color: ink, fontSize: 11 },
            data: [
              { coord: ["2028", 220], value: "Ev olayı", label: { offset: [0, -14] } },
              { coord: ["2031", 5000], value: "≈5M $ (hasatla)", label: { offset: [-30, -14] } }
            ]
          }
        },
        {
          name: "Hasatsız taban", type: "line", smooth: true, symbol: "circle", symbolSize: 5,
          lineStyle: { color: mut, width: 2 },
          itemStyle: { color: mut },
          areaStyle: { opacity: 0.08, color: mut },
          data: [0, 40, 180, 280, 400, 520]
        }
      ]
    });

    mk("chartWeek", {
      textStyle: { color: ink },
      tooltip: { trigger: "axis", axisPointer: { type: "shadow" }, valueFormatter: function (v) { return v + " saat/hafta"; } },
      grid: { left: 8, right: 30, top: 8, bottom: 6, containLabel: true },
      xAxis: Object.assign({}, axis, { type: "value", max: 34 }),
      yAxis: Object.assign({}, axis, { type: "category", data: ["Sağlık", "MetaFramer (kutu)", "DT hazırlık", "arsam kutusu", "titanlar", "Maaş işi (türksab)"], splitLine: { show: false } }),
      series: [{
        type: "bar", barWidth: 15,
        itemStyle: { borderRadius: [0, 5, 5, 0] },
        label: { show: true, position: "right", color: mut, fontSize: 11, formatter: "{c} sa" },
        data: [
          { value: 4,  itemStyle: { color: pal[3] } },
          { value: 2,  itemStyle: { color: pal[1] } },
          { value: 4,  itemStyle: { color: pal[4] } },
          { value: 8,  itemStyle: { color: P } },
          { value: 8,  itemStyle: { color: pal[2] } },
          { value: 30, itemStyle: { color: d ? "#3A5054" : "#9FB4B2" } }
        ]
      }]
    });
  }

  render();
  window.addEventListener("resize", function () {
    charts.forEach(function (c) { try { c.resize(); } catch (e) {} });
  });
  // Kapsayici genisligi degisince de yeniden olcekle (yon degistirme, panel acilma vb.)
  try {
    var ro = new ResizeObserver(function () {
      charts.forEach(function (c) { try { c.resize(); } catch (e) {} });
    });
    document.querySelectorAll(".chart").forEach(function (el) { ro.observe(el); });
  } catch (e) {}
  try {
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", render);
  } catch (e) {}
  try {
    new MutationObserver(render).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
  } catch (e) {}
})();
</script>
