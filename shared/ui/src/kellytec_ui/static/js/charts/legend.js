/* Stable caller-selected series roles; CSS owns every color value. */
(function (UI) {
  UI.chartSeriesColor = function (role) {
    const colors = {
      pnl: 'var(--monitor-chart-pnl)',
      'categorical-1': 'var(--monitor-chart-categorical-1)',
      'categorical-2': 'var(--monitor-chart-categorical-2)',
      'categorical-3': 'var(--monitor-chart-categorical-3)',
      'categorical-4': 'var(--monitor-chart-categorical-4)'
    };
    return colors[role] || colors.pnl;
  };
  UI.chartLegendItem = function (config) {
    return '<span class="monitor-chart-legend ' + UI.esc(config.className || '') + '" data-ui-type="chart-legend"><i style="background:' + UI.chartSeriesColor(config.role) + '"></i><b>' + UI.esc(config.label) + '</b><em>' + UI.esc(config.value) + '</em></span>';
  };
})(window.MonitorUI);
