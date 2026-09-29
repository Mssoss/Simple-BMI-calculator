import streamlit as st  # type: ignore
st.title("Welcome to the BMI Calculator")

weight=st.number_input("Enter Your weight (in kgs)")

status = st.radio("Select your height format:", ("cms", "m", "feet"))
bmi = 0.0

if status == "cms":
    height = st.number_input("Enter your height (in cms)")
    if height > 0:
        bmi = weight / ((height / 100) ** 2)

elif status == "m":
    height = st.number_input("Enter your height (in m)")
    if height > 0:
        bmi = weight / (height ** 2)

elif status == "feet":
    height = st.number_input("Enter your height (in feet)")
    if height > 0:
        bmi = weight / (((height / 3.28)) ** 2)

if st.button("Calculate BMI"):
    if bmi > 0:
        st.text(f"Your BMI is {bmi:.2f}")

        if bmi < 16:
            st.text("You are very underweight")
        elif bmi >= 16 and bmi < 18.5:
            st.text("You are underweight")
        elif bmi >= 18.5 and bmi < 25:
            st.text("You are Healthy")
        elif bmi >= 25 and bmi < 30:
            st.text("You are overweight")
        elif bmi >= 30:
            st.text("You are suffering from obesity")
    else:
        st.text("Enter a valid height and weight")