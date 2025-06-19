# Performance Profiler/Visualizer

This tool collects performance counters using Linux 'perf', maps them to LLVM IR and source code, and visualizes bottlenecks. It is inspired by AMD uProf but focused on correlating perf data with LLVM IR and source lines.

## Features
- Collects performance data using 'perf'.
- Parses and maps performance data to LLVM IR and source code using DWARF debug info.
- Visualizes bottlenecks interactively via a modern web UI (Streamlit).

## Getting Started
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the profiler UI:
   ```sh
   streamlit run app.py
   ```

## Requirements
- Python 3.8+
- Linux with 'perf' installed
- LLVM tools (llvm-objdump, llvm-dwarfdump)

## Usage
- Compile your program with debug info (`-g`) and LLVM IR output.
- Use this tool to collect and visualize performance data.

## License
MIT
