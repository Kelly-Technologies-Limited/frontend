# Kelly Technologies - Official Website

Static website for **Kelly Technologies Limited** (`kellytec.io`).

The served site is still plain HTML/CSS/JS on GitHub Pages. The editable
source now lives under `src/` and is built into root-level `index.html` plus
`assets/styles.css`.

## Mental model

The frontend follows the same presentation model as Monitor:

```text
page -> tab -> card -> cell
```

- **page**: one complete page. Current page: `home`.
- **tab**: one top-level area inside a page. On this public site a tab is a
  page section, not necessarily a visible tab control.
- **card**: one content or visual block inside a tab.
- **cell**: the smallest displayed value inside a card.

Current source mapping:

```text
home page
  hero tab
    hero_title card
      headline cell

  strategies tab
    strategy_statement card
      eyebrow cell
      title cell
    volatility_surface card
      surface cell

  team tab
    team_heading card
      eyebrow cell
    team_member_tianxin_song card
      initials, name, role, bio cells
    team_member_xinhai_xiong card
      initials, name, role, bio cells
    team_member_peiyu_xiong card
      initials, name, role, bio cells

  contact tab
    office_contact card
      eyebrow, address, email cells
```

Cells stay inside card files until a cell type earns its own deeper Module.
Do not add placeholder pages, tabs, cards, or cells for content that does not
exist yet.

## Stack

- Pure HTML / CSS / JS
- No framework and no browser-side fragment loading
- A tiny standard-library Python build script
- Google Fonts: Playfair Display and Noto Serif SC
- Hosted on GitHub Pages at `kellytec.io` via `CNAME`

## Build

Edit source files under `src/`, then rebuild the served files:

```bash
cd frontend
python scripts/build_site.py
```

The build writes:

- `index.html`
- `assets/styles.css`

The old monolithic `assets/script.js` entrypoint is intentionally gone. Runtime
behavior is split under `assets/scripts/`.

## Project structure

```text
index.html                  # generated served home page
palettes.html               # palette study / retheming playground
scripts/build_site.py       # renders source fragments into served files
src/chrome/                 # document head, header, footer
src/pages/home/page.html    # home page shell and tab order
src/pages/home/tabs/        # current tab_*.html sections
src/pages/home/cards/       # current card_*.html files with data-cell annotations
src/styles/                 # split CSS source
assets/styles.css           # generated stylesheet, Monitor chrome source
assets/scripts/             # split runtime behavior Modules
assets/logo.svg             # wordmark + icon
assets/logo-light.svg       # light logo variant
assets/favicon.svg
assets/hero-bg.jpg
gp/monitor/index.html       # static redirect to Monitor
CNAME
.nojekyll
```

## Editing rules

- Edit source fragments, not generated `index.html` or `assets/styles.css`.
- Keep `site-header` and `site-footer` shapes stable unless you also check
  Monitor chrome extraction.
- Preserve the existing CSS classes and ids when refactoring. The `data-page`,
  `data-tab`, `data-card`, and `data-cell` attributes are the semantic editing
  Interface.
- Keep public behavior static-first. Do not add a framework or runtime HTML
  loader unless the site grows enough to justify a new architecture decision.

## Brand notes

The current brand palette is near-white canvas (`#FCFCFC`) over deep cool
charcoal ink (`#373545`), with muted lavender-gray accents:

- Accent 1: `#7F7B9A`
- Accent 2: `#67647E`
- Accent 3: `#4F4C61`

`palettes.html` remains the live palette study for future retheming.
