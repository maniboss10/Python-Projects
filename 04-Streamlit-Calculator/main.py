import streamlit as st


def calculate(first_number: float, operator: str, second_number: float) -> float:
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "×":
        return first_number * second_number
    if operator == "÷":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError(f"Unsupported operator: {operator}")


st.set_page_config(page_title="Calculator", page_icon="🧮")
st.title("Simple Calculator")
st.write("Choose an operation and enter two numbers.")

first_number = st.number_input("First number", value=0.0, key="first_number")
operator = st.selectbox("Operation", ["+", "-", "×", "÷"])
second_number = st.number_input("Second number", value=0.0, key="second_number")

if st.button("Calculate", type="primary"):
    try:
        result = calculate(first_number, operator, second_number)
    except ZeroDivisionError as error:
        st.error(str(error))
    else:
        st.metric("Result", f"{result:.12g}")
