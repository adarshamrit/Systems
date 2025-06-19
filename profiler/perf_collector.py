import subprocess
import os
from typing import List

class PerfCollector:
    """Collects performance data using Linux 'perf'."""
    def __init__(self, binary_path: str, perf_data_path: str = "perf.data"):
        self.binary_path = binary_path
        self.perf_data_path = perf_data_path

    def record(self, args: List[str] = None, events: str = "cycles,instructions"):
        args = args or []
        cmd = [
            "perf", "record", f"-e", events, "-o", self.perf_data_path, "--", self.binary_path
        ] + args
        subprocess.run(cmd, check=True)

    def report(self) -> str:
        cmd = ["perf", "report", "-i", self.perf_data_path, "--stdio"]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return result.stdout
