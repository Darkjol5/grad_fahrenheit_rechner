import streamlit as st
 
# Fahrenheit → Celsius
def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    return c
 
def animate():
    st.balloons()
    st.snow()
 
print("32°F sind:", fahrenheit_to_celsius(32), "°C")
 
st.title("Fahrenheit -> Celsius Rechner")
st.header("Wir rechnen Temperaturen um")
st.image("thermometer.jpg", "Temperaturen umrechnen macht Spaß", width=400)
 
zahl1 = st.number_input("Geben Sie eine Temperatur in Fahrenheit ein:")
 
buttonCalculate = st.button("Umrechnen")
buttonAnimate = st.button("Animiere")
 
if buttonCalculate:
    wert = fahrenheit_to_celsius(zahl1)
    st.write("Das sind", wert, "Grad Celsius")
    animate()
 
if buttonAnimate:
    animate()
 