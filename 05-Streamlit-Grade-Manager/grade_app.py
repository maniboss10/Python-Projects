import streamlit as st


def get_grade(mark):
    """Return the letter grade for a mark between 0 and 100."""
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")

    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


st.set_page_config(page_title="Student Grade Manager", page_icon="📚")
st.title("Student Grade Manager")
st.write("Add student marks to see grades and class statistics.")

if "students" not in st.session_state:
    st.session_state.students = []

with st.form("add_student_form"):
    name = st.text_input("Name")
    mark = st.number_input(
        "Mark",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1,
        format="%.1f",
    )
    submitted = st.form_submit_button("Add")

if submitted:
    student_name = name.strip()
    if not student_name:
        st.error("Name cannot be empty.")
    elif not 0 <= mark <= 100:
        st.error("Mark must be between 0 and 100.")
    else:
        st.session_state.students.append({"name": student_name, "mark": mark})
        st.success(f"{student_name} was added successfully.")

if st.session_state.students:
    students = st.session_state.students
    results = [
        {
            "Name": student["name"],
            "Mark": student["mark"],
            "Grade": get_grade(student["mark"]),
        }
        for student in students
    ]
    st.table(results)

    marks = [student["mark"] for student in students]
    average, highest, lowest = st.columns(3)
    average.metric("Average", f"{sum(marks) / len(marks):.1f}")
    highest.metric("Highest", f"{max(marks):g}")
    lowest.metric("Lowest", f"{min(marks):g}")
else:
    st.info("Add a student to see the class results.")
