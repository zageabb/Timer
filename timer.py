import streamlit as st
import time

# Streamlit app setup
st.title("Large Number Timer")

if st.button("Start Timer"):
    placeholder = st.empty()
    start_time = time.time()

    while True:
        elapsed = int(time.time() - start_time)
        mins, secs = divmod(elapsed, 60)
        hrs, mins = divmod(mins, 60)
        timer_display = f"{hrs:02}:{mins:02}:{secs:02}"

        # Display timer in large font
        placeholder.markdown(
            f"<h1 style='text-align: center; font-size: 72px;'>{timer_display}</h1>",
            unsafe_allow_html=True,
        )

        time.sleep(1)
