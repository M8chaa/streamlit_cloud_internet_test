import streamlit as st
import speedtest

def test_internet_speed():
    s = speedtest.Speedtest()
    s.get_best_server()
    download_speed = s.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = s.upload() / 1024 / 1024  # Convert to Mbps
    return download_speed, upload_speed

def main():
    st.title('Internet Speed Test')

    if st.button('Test Internet Speed'):
        with st.spinner('Testing...'):
            download_speed, upload_speed = test_internet_speed()
        st.success('Test completed')
        st.write(f"Download speed: {download_speed:.2f} Mbps")
        st.write(f"Upload speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    main()