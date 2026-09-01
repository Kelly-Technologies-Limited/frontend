# Changelog

## 2026-09-01

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
