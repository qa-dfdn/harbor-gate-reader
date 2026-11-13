"""RFID gate readers for Northwind Harbor Logistics"""

class HarborGateReader:
    """Internal service for harbor-gate-reader."""

    def status(self) -> str:
        return "ok"


if __name__ == "__main__":
    print(HarborGateReader().status())
