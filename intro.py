import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welkom 👋")

st.markdown( """
Op deze website kan je oefeningen maken met een gesimuleerd systeem
Het voorbeeld dat gegeven wordt is de hoogteregeling van een drone. 
In volgende video wordt een versimpelde versie gegeven hoe zo een systeem kan werken.          
"""
)

st.video('https://youtu.be/QNnx2evKb_0?si=0s1S4yWZuPnfQC0f')

st.markdown("""
De regelkring van het systeem ziet er als volgt uit. 
De **setwaarde of referentiewaarde** wordt vergelijk met het **meetsignaal** van de *sensor*. In dit geval is de meetwaarde de hoogte van de drone in meter.
Het resulterende **foutsignaal** zal dan door de *controler of regelaar* omgezet worden naar een **regelsignaal**.
In dit geval is het regelsignaal het vermogen dat naar de motoren van de drone gaat.

Het doel is om een systeem te hebben dat snel reageert en geen oscillatie vertoont.
""")

st.image('images/500px-Gesloten_regelsysteem.png')
st.sidebar.success('Kies een oefening.')