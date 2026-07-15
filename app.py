import streamlit as st
import numpy as np
from model import train

# title
st.title("Hello World AI App ")
st.subheader("A simple regression model")

# Train model
model=train()

 # Sidebar
 st.sidebar.header("Input features")
 input_value=st.sidebar.slider("Select value f x",1,10,1)
 # Prediction
 input_array=np.array([[input_value]])
 prediction=model.predict(input_array)

 # Display result
 st.write(f'### Input value : {input_value}')
 st.write(f'### output value : {prediction[0]:.2f}')
