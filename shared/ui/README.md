# Shared UI

`kellytec-ui==0.1.0` owns the Monitor presentation used by both Monitor apps
and Kelly Technologies Research Platform. Runtime Python dependencies are standard library only.
The package contains the original Page → Tab → Card → Cell contracts,
renderers, CSS tokens, JavaScript, templates, generated brand and fonts.
There is no application authentication, fetch loop or compute logic here.

Build from the frontend repository:

```sh
python scripts/sync_frontend_chrome.py
python -m build --wheel shared/ui
python -m pip install --no-deps shared/ui/dist/kellytec_ui-0.1.0-py3-none-any.whl
python -m pytest -q shared/ui/tests tests
```

Publish the reviewed, immutable wheel through the existing approved Python
package repository before releasing Monitor. Monitor's two pinned requirements
files feed its existing dependency download, vendor and offline Docker install
steps. Research Platform bundles the same wheel. Consumers never read a sibling checkout.
Do not reuse a version for changed release bytes.

Use `kellytec_ui.assets.ROOT` for installed favicon/static resources, and
`design_system_css()` / `shared_ui_script()` for the canonical bundles.
Use `data-ui="button"` for application actions outside the toolbar; it selects
the same base and hover styles as Monitor toolbar buttons, with the shared
native disabled and keyboard-focus behavior.
`MonitorPage.toolbar_actions_html=None` retains Monitor's existing status and
Refresh controls; a trusted application HTML string replaces only those actions.
`updated_initial` is escaped and can contain the current account/project text.
`toolbar_aria_label` supplies its accessible label.

`render_login` keeps the password form by default. Optional `instruction`,
`form_html`, `scripts_html`, and `brand_logo=True` allow browser authorization
without putting provider behavior inside shared UI. Apps must escape user values
in trusted HTML slots; labels passed as plain text are escaped by the renderer.

Fonts are downloaded production resources, not extracted from a test HAR.
Their original URLs, SHA-256 values and OFL licenses are in `static/fonts`.
IBM Plex Sans 400/500/600/700, Mono 400/500/600, and Playfair Display 400–700
are bundled; Noto Serif SC includes the existing Chinese copyright glyphs.
The logo is an SVG outline. English tool interfaces require no external fonts.
`font_stylesheet()` embeds these resources so applications need no font route
and can run offline. Other CJK text would require an explicit font subset update.

Canonical logos and imagery live in `shared/assets/`. Brand generation reads
that directory and the website's `src/chrome/` and `src/styles/` directly;
it does not require generated website output. Generated package resources
remain bundled in the wheel, so consumers need no sibling asset directory.

Website output is built independently by `scripts/build_site.py` into `dist/site/`.
The allowlist excludes Python, tests, wheel and build tooling. The GitHub Actions
workflow builds and tests both artifacts, then deploys only the public website on
pushes to `main`. Pull requests never deploy. Pages uses GitHub Actions publishing,
not the branch root. The separate wheel artifact still needs publication through
the approved Python package repository before a consumer release; a website
deployment does not update Monitor or Research Platform.
