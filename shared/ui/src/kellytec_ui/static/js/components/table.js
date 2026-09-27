/* Canonical semantic table shell. */
(function (UI) {
  UI.table = function (headers, rows, emptyText) {
    if (!rows.length) return '<div class="empty">' + UI.esc(emptyText || "No data") + "</div>";
    return '<div class="scroll"><table data-ui="table"><thead><tr>' +
      headers.map(function (heading) { return '<th data-ui-type="table-header">' + UI.esc(heading) + "</th>"; }).join("") +
      "</tr></thead><tbody>" + rows.map(function (row) {
        return "<tr>" + row.map(function (value) {
          return '<td data-ui-type="table-cell">' + value + "</td>";
        }).join("") + "</tr>";
      }).join("") + "</tbody></table></div>";
  };
})(window.MonitorUI);
