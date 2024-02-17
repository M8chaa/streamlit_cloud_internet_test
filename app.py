import platform
import psutil
import streamlit as st
def get_cpu_info():
    info = {
        "Processor": platform.processor(),
        "Physical cores": psutil.cpu_count(logical=False),
        "Total cores": psutil.cpu_count(logical=True),
        "Max Frequency": f"{psutil.cpu_freq().max:.2f} MHz",
        "Min Frequency": f"{psutil.cpu_freq().min:.2f} MHz",
        "Current Frequency": f"{psutil.cpu_freq().current:.2f} MHz",
    }
    return info

if __name__ == "__main__":
    st.write(get_cpu_info())
