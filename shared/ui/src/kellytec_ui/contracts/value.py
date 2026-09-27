"""Typed descriptors for every user-visible monitor value."""

from __future__ import annotations

from typing import Literal, NotRequired, TypedDict


DisplayKind = Literal[
    "text", "integer", "decimal", "quantity", "price", "money",
    "percent_ratio", "percent_points", "bytes", "gigabytes", "duration_ms",
    "trading_date", "datetime_et", "time_et", "minute_et", "status",
]
DISPLAY_KINDS = frozenset(DisplayKind.__args__)
STATUS_VALUES = frozenset({"healthy", "warning", "critical", "unknown", "inactive"})


class DisplayValue(TypedDict):
    kind: DisplayKind
    value: object
    currency: NotRequired[str]
    label: NotRequired[str]
    show_plus: NotRequired[bool]
    compact: NotRequired[Literal["millions"]]


def display_value(
    kind: DisplayKind,
    value: object,
    *,
    currency: str | None = None,
    label: str | None = None,
    show_plus: bool = False,
    compact: Literal["millions"] | None = None,
) -> DisplayValue:
    """Build a strict semantic value without guessing business meaning."""

    if kind not in DISPLAY_KINDS:
        raise ValueError(f"unsupported display kind: {kind}")
    if kind == "money" and (not isinstance(currency, str) or not currency.strip()):
        raise ValueError("money display values require currency")
    if kind != "money" and currency is not None:
        raise ValueError("currency is only valid for money display values")
    if kind == "status" and value not in STATUS_VALUES:
        raise ValueError("status display values require a canonical status")
    if kind != "status" and label is not None:
        raise ValueError("label is only valid for status display values")
    if kind != "quantity" and show_plus:
        raise ValueError("show_plus is only valid for quantity display values")
    if kind != "money" and compact is not None:
        raise ValueError("compact is only valid for money display values")

    result: DisplayValue = {"kind": kind, "value": value}
    if currency is not None:
        result["currency"] = currency.strip().upper()
    if label is not None:
        result["label"] = label
    if show_plus:
        result["show_plus"] = True
    if compact is not None:
        result["compact"] = compact
    return result


__all__ = ["DISPLAY_KINDS", "DisplayKind", "DisplayValue", "display_value"]
