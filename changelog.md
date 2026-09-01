# Changelog

## 2026-09-02

- Replaced both GP card Unicode arrow characters with deterministic inline SVG
  paths so mobile platforms cannot substitute emoji glyphs. Centered the
  security-note mark on the first mobile text line; the 430px Chrome regression
  measures a 0.04px center delta with zero horizontal overflow.
- Reframed both GP system cards as two-line product hierarchies: English uses
  `ALGO3 Monitor / Operations` and `ALGO3 Monitor / Data Availability`, while
  Chinese uses `ALGO3 监控台 / 运营` and `ALGO3 监控台 / 数据可用性`.

## 2026-09-01

- Standardized the GP landing browser-tab title in English regardless of the
  selected page language.
- Aligned both monitor-card titles with the GP Login serif weight and tracking.
- Corrected the public access navigation so the language switch renders
  `GP / LP` in English and `管理人 / 投资人` in Chinese.
- Compacted the GP landing page to fit standard desktop viewports without
  vertical scrolling while retaining responsive narrow-screen behavior.
- Moved the legacy GP redirect source under `src/redirects/`; root `gp/`
  remains generated output required by branch-based GitHub Pages.
- Replaced the public Monitor header action with the bilingual GP access link.
- Added a bilingual `/gp/` launchpad for the protected ALGO3 Operations and
  Data Availability monitors.
- Preserved `/gp/monitor/` as a redirect to the new launchpad and marked the
  launchpad `noindex, nofollow`.
- Extended the static build around the existing page → tab → card → cell
  presentation model so both public pages share the same chrome and assets.
