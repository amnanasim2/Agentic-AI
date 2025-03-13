import streamlit as st

st.title("BMI Calculator 💪")

# User Input
weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.1, format="%.2f")

# Calculate BMI
if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.write(f"### Your BMI is: {bmi:.2f}")
    
    if bmi < 18.5:
        st.warning("You are underweight!")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight! 🎉")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight!")
    else:
        st.error("You are obese! Consider consulting a doctor.")
else:
    st.write("Please enter valid weight and height.")
