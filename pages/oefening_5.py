import streamlit as st
from utils import make_chart
from simulated_PID_controller import PID_Controller, SMD_System_Sim

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

# Begin main code
kp = st.number_input('Waarde voor Kp')
Ti = st.number_input('Waarde voor Ti', value=10000.0)
Td = st.number_input('Waarde voor Td', value=0.0)
# Create Controller object
controller = PID_Controller(kp, Ti=Ti, Td=Td)
system_simulator = SMD_System_Sim(mass = 1, k = 100, c = 2)

p = make_chart(controller, system_simulator)

st.bokeh_chart(p, use_container_width=True)
