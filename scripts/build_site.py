"""Build the static Kelly Technologies frontend from source fragments."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

CHROME = SRC / "chrome"
HOME = SRC / "pages" / "home"
CARDS = HOME / "cards"
TABS = HOME / "tabs"
GP = SRC / "pages" / "gp"
GP_CARDS = GP / "cards"
GP_TABS = GP / "tabs"

CSS_SOURCES = (
    SRC / "styles" / "tokens.css",
    SRC / "styles" / "base.css",
    SRC / "styles" / "chrome.css",
    SRC / "styles" / "tabs" / "tab_hero.css",
    SRC / "styles" / "tabs" / "tab_strategies.css",
    SRC / "styles" / "tabs" / "tab_team.css",
    SRC / "styles" / "tabs" / "tab_contact.css",
    SRC / "styles" / "pages" / "page_gp.css",
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

GP_CARD_FILES = {
    "intro": "card_intro.html",
    "operations": "card_operations.html",
    "data_availability": "card_data_availability.html",
    "security_note": "card_security_note.html",
}

GP_TAB_FILES = {
    "access": "tab_access.html",
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


def render_document_head(
    *, title: str, description: str, asset_prefix: str, noindex: bool, preload: str = ""
) -> str:
    return replace_all(
        read(CHROME / "document_head.html"),
        {
            "document.title": title,
            "document.description": description,
            "document.robots": (
                '<meta name="robots" content="noindex, nofollow" />' if noindex else ""
            ),
            "document.preload": preload,
            "asset.prefix": asset_prefix,
        },
    )


def render_header(*, asset_prefix: str, home_href: str, gp_current: bool) -> str:
    return replace_all(
        read(CHROME / "header.html"),
        {
            "asset.prefix": asset_prefix,
            "navigation.home": home_href,
            "navigation.gp_current": " is-current" if gp_current else "",
        },
    )


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
        "chrome.document_head": render_document_head(
            title="Kelly Technologies",
            description="Kelly Technologies — an investment and technology firm.",
            asset_prefix="",
            noindex=False,
            preload='<link rel="preload" as="image" href="assets/hero-bg.jpg" fetchpriority="high" />',
        ),
        "chrome.header": render_header(
            asset_prefix="", home_href="#top", gp_current=False
        ),
        "chrome.footer": read(CHROME / "footer.html"),
        **tabs,
    }
    return replace_all(read(HOME / "page.html"), page_values).rstrip() + "\n"


def render_gp_page() -> str:
    cards = {
        f"card.{name}": read(GP_CARDS / filename)
        for name, filename in GP_CARD_FILES.items()
    }
    tabs = {
        f"tab.{name}": replace_all(read(GP_TABS / filename), cards)
        for name, filename in GP_TAB_FILES.items()
    }
    page_values = {
        "chrome.document_head": render_document_head(
            title="GP Login | Kelly Technologies",
            description="Authorized access to Kelly Technologies monitoring systems.",
            asset_prefix="../",
            noindex=True,
        ),
        "chrome.header": render_header(
            asset_prefix="../", home_href="/", gp_current=True
        ),
        "chrome.footer": read(CHROME / "footer.html"),
        **tabs,
    }
    return replace_all(read(GP / "page.html"), page_values).rstrip() + "\n"


def build_css() -> str:
    return "\n\n".join(read(path).rstrip() for path in CSS_SOURCES).rstrip() + "\n"


def main() -> None:
    (ROOT / "index.html").write_text(render_home_page(), encoding="utf-8")
    (ROOT / "gp").mkdir(exist_ok=True)
    (ROOT / "gp" / "index.html").write_text(render_gp_page(), encoding="utf-8")
    (ROOT / "assets" / "styles.css").write_text(build_css(), encoding="utf-8")


if __name__ == "__main__":
    main()
