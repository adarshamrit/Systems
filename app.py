import streamlit as st
import pandas as pd
from profiler.perf_collector import PerfCollector
from profiler.ir_mapper import IRMapper

st.title("Performance Profiler & Visualizer")

binary_path = st.text_input("Path to binary for profiling:")

if binary_path:
    perf = PerfCollector(binary_path)
    if st.button("Collect perf data"):
        with st.spinner("Collecting perf data..."):
            try:
                perf.record()
                st.success("Perf data collected.")
            except Exception as e:
                st.error(f"Error: {e}")
    if st.button("Show perf report"):
        with st.spinner("Generating report..."):
            try:
                report = perf.report()
                st.text_area("Perf Report", report, height=300)
            except Exception as e:
                st.error(f"Error: {e}")
    addr = st.text_input("Address to map (e.g., 0x400123):")
    if addr:
        ir_mapper = IRMapper(binary_path)
        src = ir_mapper.addr_to_source(addr)
        ir = ir_mapper.addr_to_ir(addr)
        st.write(f"Source: {src['source']}")
        st.write(f"LLVM IR: {ir}")
