import streamlit as st
try:
    def  bmi_c():
        y=st.text_input("choose your hegiht type : (cm , m , feet) = ")
        h=st.number_input("enter your height in cm , m, feet")
        if y=="cm":
            h1=h/100
        elif y=="m":
         y1=y
        elif y=="feet":
         y2=h*0.304
        w=st.number_input("inter your weight in kg")
        if y=="cm":
            h1=h/100
            bmi= w/h1**2
        elif y=="m":
            y1=y
            bmi= w/h**2
        
        elif y=="feet":
            y2=h*0.304
            bmi= w/y2**2
        
   
        st.write(f"your bmi is fitness = {bmi}")
        if bmi<18.5:
            st.info("underweight")
        elif bmi>=18.5 and bmi<25:
            st.success("normal")
        elif bmi>=25 and bmi<30:
            st.warning("overweight")
        else:
            st.info("obesity, kills")

except Excption as e:
    st.warning('encountered an error')

try:
    if __name__ == "__main__": 
        bmi_c()
except Exception as e:
    st.warning('please enter correct values')
hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)