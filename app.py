import psutil
import streamlit as st
import cpuinfo  # Import the cpuinfo library

def get_cpu_info():
    info = cpuinfo.get_cpu_info()  # Use cpuinfo to get detailed CPU information
    cpu_details = {
        "Processor": info.get('brand_raw', ''),  # Get the CPU brand
        "Physical cores": psutil.cpu_count(logical=False),
        "Total cores": psutil.cpu_count(logical=True),
        "Max Frequency": f"{psutil.cpu_freq().max:.2f} MHz",
        "Min Frequency": f"{psutil.cpu_freq().min:.2f} MHz",
        "Current Frequency": f"{psutil.cpu_freq().current:.2f} MHz",
    }
    return cpu_details

if __name__ == "__main__":
    st.write(get_cpu_info())
