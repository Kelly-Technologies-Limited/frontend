# Kelly Technologies — Official Website

Static one-pager for **Kelly Technologies Limited** (kellytec.io).

**Design language (Brandmark palette).** Near-white canvas (`#FCFCFC`)
over a deep cool charcoal ink (`#373545`), with a three-step muted
lavender-gray accent ladder — **Accent 1** `#7F7B9A`, **Accent 2**
`#67647E`, **Accent 3** `#4F4C61`. Display type is Fraunces (serif),
body is Inter, monospace eyebrows use JetBrains Mono.

A live palette study lives at `palettes.html` if we ever want to retheme.

## Stack

- Pure HTML / CSS / JS — no build step, no framework
- Google Fonts: Fraunces (display serif), Inter (sans), JetBrains Mono
- Hosted on GitHub Pages at `kellytec.io` (via `CNAME`)

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Project structure

```
├── index.html          # single-page site
├── palettes.html       # palette study / retheming playground
├── assets/
│   ├── styles.css      # design tokens + components
│   ├── script.js       # header scroll state + reveal animations
│   ├── logo.svg        # wordmark + icon (dark on light)
│   ├── logo-light.svg  # light variant for dark backgrounds
│   └── hero-bg.jpg     # hero background image
├── CNAME               # custom domain → kellytec.io
└── .nojekyll           # disable Jekyll on Pages (we ship raw files)
```

## Editing content

All copy lives in `index.html` in semantic sections:

| Section ID    | Purpose                              |
| ------------- | ------------------------------------ |
| `hero`        | Firm intro (no id)                   |
| `#strategies` | One-line strategy statement          |
| `#team`       | Founder cards (TS / XX / PX)         |
| `#contact`    | Office address + email               |

Design tokens (colors, fonts, spacing) are defined as CSS variables
at the top of `assets/styles.css` under `:root` — change them in one
place to retheme the whole site.
