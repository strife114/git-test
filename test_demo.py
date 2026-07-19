"""A quick demo module — nothing fancy, just a warm handshake."""

from datetime import datetime, timezone


def greet(name: str = "world") -> str:
    """Return a friendly greeting with a UTC timestamp."""
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return f"Hello, {name}! It's {now} UTC."


if __name__ == "__main__":
    print(greet())
