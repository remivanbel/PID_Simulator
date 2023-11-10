import streamlit as st
from utils import make_chart
from simulated_PID_controller import PID_Controller, SMD_System_Sim

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

# Begin main code
kp = st.number_input('Waarde voor Kp', step=1)
ki = 0
kd = 0
# Create Controller object
controller = PID_Controller(kp, ki, kd)
system_simulator = SMD_System_Sim(mass = 10, k = 0, c = 10)

p = make_chart(controller, system_simulator)

st.bokeh_chart(p, use_container_width=True)