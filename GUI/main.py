import streamlit as st
import numpy as np
import pandas as pd

st.title('Pico_W專案:更新')
st.header("雞舍:orange[溫度]和:rainbow[光線]狀態")
st.divider()


df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [23.487614, 120.959522],
    columns=['lat', 'lon'])

st.map(df)

#st.snow()

#sample_rate = 44100  # 44100 samples per second
#seconds = 2  # Note duration of 2 seconds

#frequency_la = 440  # Our played note will be 440 Hz

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
#t = np.linspace(0, seconds, seconds * sample_rate, False)

# Generate a 440 Hz sine wave
#note_la = np.sin(frequency_la * t * 2 * np.pi)
#st.audio(note_la, sample_rate=sample_rate)




