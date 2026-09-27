/* One semantic value contract for dates, numbers, money, quantities and status. */
(function (UI) {
  const EMPTY = UI.EMPTY || "—";
  const STATUS_LABELS = {
    healthy: "Healthy",
    warning: "Warning",
    critical: "Critical",
    unknown: "Unknown",
    inactive: "Inactive"
  };

  function missing(value) {
    return value === null || value === undefined || value === "";
  }

  function number(value) {
    if (missing(value)) return null;
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : null;
  }

  function grouped(value, minimum, maximum) {
    const parsed = number(value);
    if (parsed === null) return EMPTY;
    return parsed.toLocaleString("en-US", {
      minimumFractionDigits: minimum,
      maximumFractionDigits: maximum
    });
  }

  function etParts(value) {
    if (missing(value)) return null;
    const raw = String(value).trim();
    if (!/(?:z|[+-]\d{2}:?\d{2})$/i.test(raw)) {
      const match = raw.replace(/\s*ET$/i, "").replace("T", " ")
        .match(/^(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})(?::(\d{2}))?/);
      return match ? {
        year: match[1], month: match[2], day: match[3],
        hour: match[4], minute: match[5], second: match[6] || "00"
      } : null;
    }
    const instant = new Date(raw);
    if (Number.isNaN(instant.getTime())) return null;
    return new Intl.DateTimeFormat("en-US", {
      timeZone: "America/New_York",
      hour12: false,
      hourCycle: "h23",
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit"
    }).formatToParts(instant).reduce(function (result, part) {
      result[part.type] = part.value;
      return result;
    }, {});
  }

  function date(parts) {
    return parts.year + "-" + parts.month + "-" + parts.day;
  }

  function clock(parts, seconds) {
    return parts.hour + ":" + parts.minute + (seconds ? ":" + parts.second : "");
  }

  const formatters = {
    text: function (spec) {
      return missing(spec.value) ? EMPTY : String(spec.value);
    },
    integer: function (spec) {
      return grouped(spec.value, 0, 0);
    },
    decimal: function (spec) {
      return grouped(spec.value, 0, 2);
    },
    quantity: function (spec) {
      const parsed = number(spec.value);
      if (parsed === null) return EMPTY;
      return (parsed > 0 && spec.show_plus ? "+" : "") + grouped(parsed, 0, 4);
    },
    price: function (spec) {
      return grouped(spec.value, 2, 2);
    },
    money: function (spec) {
      const parsed = number(spec.value);
      if (parsed === null || !spec.currency) return EMPTY;
      const scaled = spec.compact === "millions" ? Math.abs(parsed) / 1000000 : Math.abs(parsed);
      const abs = scaled.toLocaleString("en-US", spec.compact === "millions" ? {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      } : { maximumFractionDigits: 0 });
      const symbol = spec.currency === "USD" ? "$" : spec.currency + " ";
      return (parsed < 0 ? "-" : "") + symbol + abs + (spec.compact === "millions" ? "M" : "");
    },
    percent_ratio: function (spec) {
      const parsed = number(spec.value);
      return parsed === null ? EMPTY : grouped(parsed * 100, 0, 1) + "%";
    },
    percent_points: function (spec) {
      const parsed = number(spec.value);
      return parsed === null ? EMPTY : grouped(parsed, 0, 1) + "%";
    },
    bytes: function (spec) {
      let parsed = number(spec.value);
      if (parsed === null || parsed < 0) return EMPTY;
      const units = ["B", "KB", "MB", "GB", "TB"];
      let index = 0;
      while (parsed >= 1024 && index < units.length - 1) {
        parsed /= 1024;
        index += 1;
      }
      const formatted = index === 0 ? grouped(parsed, 0, 0) : grouped(parsed, parsed >= 10 ? 1 : 2, parsed >= 10 ? 1 : 2);
      return formatted + " " + units[index];
    },
    gigabytes: function (spec) {
      const parsed = number(spec.value);
      return parsed === null || parsed < 0
        ? EMPTY
        : grouped(parsed / 1000000000, 2, 2) + " GB";
    },
    duration_ms: function (spec) {
      const parsed = number(spec.value);
      if (parsed === null || parsed < 0) return EMPTY;
      if (parsed < 1000) return grouped(parsed, 0, 0) + " ms";
      if (parsed < 60000) return grouped(parsed / 1000, 0, 1) + " s";
      return grouped(parsed / 60000, 0, 1) + " min";
    },
    trading_date: function (spec) {
      if (missing(spec.value)) return EMPTY;
      const match = String(spec.value).match(/^(\d{4}-\d{2}-\d{2})/);
      return match ? match[1] : EMPTY;
    },
    datetime_et: function (spec) {
      const parts = etParts(spec.value);
      return parts ? date(parts) + " " + clock(parts, true) + " ET" : EMPTY;
    },
    time_et: function (spec) {
      const parts = etParts(spec.value);
      return parts ? clock(parts, true) + " ET" : EMPTY;
    },
    minute_et: function (spec) {
      const parts = etParts(spec.value);
      return parts ? clock(parts, false) + " ET" : EMPTY;
    },
    status: function (spec) {
      const state = String(spec.value || "unknown").toLowerCase();
      return spec.label || STATUS_LABELS[state] || STATUS_LABELS.unknown;
    }
  };

  UI.value = function (spec) {
    if (!spec || typeof spec !== "object" || !formatters[spec.kind]) return EMPTY;
    return formatters[spec.kind](spec);
  };

  UI.statusText = function (value) {
    return UI.value({ kind: "status", value: value });
  };

})(window.MonitorUI);
