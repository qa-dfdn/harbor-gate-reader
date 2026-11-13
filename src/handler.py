"""Request handler for harbor-gate-reader."""

def handle(event: dict) -> dict:
    kind = event.get("kind", "scan")
    return {"ok": True, "kind": kind, "service": "harbor-gate-reader"}
