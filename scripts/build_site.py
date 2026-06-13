"""Build the static Kelly Technologies frontend from source fragments."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

CHROME = SRC / "chrome"
HOME = SRC / "pages" / "home"
CARDS = HOME / "cards"
TABS = HOME / "tabs"

CSS_SOURCES = (
    SRC / "styles" / "tokens.css",
    SRC / "styles" / "base.css",
    SRC / "styles" / "chrome.css",
    SRC / "styles" / "tabs" / "tab_hero.css",
    SRC / "styles" / "tabs" / "tab_strategies.css",
    SRC / "styles" / "tabs" / "tab_team.css",
    SRC / "styles" / "tabs" / "tab_contact.css",
    SRC / "styles" / "effects.css",
)

CARD_FILES = {
    "hero_title": "card_hero_title.html",
    "strategy_statement": "card_strategy_statement.html",
    "volatility_surface": "card_volatility_surface.html",
    "team_heading": "card_team_heading.html",
    "team_member_tianxin_song": "card_team_member_tianxin_song.html",
    "team_member_xinhai_xiong": "card_team_member_xinhai_xiong.html",
    "team_member_peiyu_xiong": "card_team_member_peiyu_xiong.html",
    "office_contact": "card_office_contact.html",
}

TAB_FILES = {
    "hero": "tab_hero.html",
    "strategies": "tab_strategies.html",
    "team": "tab_team.html",
    "contact": "tab_contact.html",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")


def replace_all(text: str, values: dict[str, str]) -> str:
    result = text
    for key, value in values.items():
        result = result.replace("{{" + key + "}}", value.rstrip())
    leftovers = sorted({part.split("}}", 1)[0] for part in result.split("{{")[1:] if "}}" in part})
    if leftovers:
        raise ValueError("Unresolved include(s): " + ", ".join(leftovers))
    return result


def render_home_page() -> str:
    cards = {
        f"card.{name}": read(CARDS / filename)
        for name, filename in CARD_FILES.items()
    }
    tabs = {
        f"tab.{name}": replace_all(read(TABS / filename), cards)
        for name, filename in TAB_FILES.items()
    }
    page_values = {
        "chrome.document_head": read(CHROME / "document_head.html"),
        "chrome.header": read(CHROME / "header.html"),
        "chrome.footer": read(CHROME / "footer.html"),
        **tabs,
    }
    return replace_all(read(HOME / "page.html"), page_values).rstrip() + "\n"


def build_css() -> str:
    return "\n\n".join(read(path).rstrip() for path in CSS_SOURCES).rstrip() + "\n"


def main() -> None:
    (ROOT / "index.html").write_text(render_home_page(), encoding="utf-8")
    (ROOT / "assets" / "styles.css").write_text(build_css(), encoding="utf-8")


if __name__ == "__main__":
    main()
