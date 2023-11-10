import streamlit as st
from utils import make_chart
from simulated_PID_controller import PID_Controller, SMD_System_Sim

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown(
"""

1. Zet de Kp waarde op 1. Wat merk je op? Kijk hierbij naar:
    * Hoe lang duurt het voordat de gewenste waarde bereikt wordt?
    * Wordt de werkelijke waarde soms grote dan de referentiewaarde?
    * Is er oscillatie in het systeem? 

2. Zet de Kp Waarde op 10. Wat merk je op? Vergelijk met je antwoorden op vraag 1.
3. Zet de Kp waarde op 100. Wat merk je op? Vergelijk met je antwoorden op vraag 1 en 2.
4. Wat zou je nemen als de ideale waarde voor Kp?
"""
)

# Begin main code
kp = st.number_input('Waarde voor Kp', step=1)
ki = 0
kd = 0
# Create Controller object
controller = PID_Controller(kp, ki, kd)
system_simulator = SMD_System_Sim(mass = 10, k = 0, c = 10)

p = make_chart(controller, system_simulator)

st.bokeh_chart(p, use_container_width=True)