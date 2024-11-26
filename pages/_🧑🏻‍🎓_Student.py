import streamlit as st
import mysql.connector
from feedback_form import student_feedback_form

# Database Connection
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SujanKC@9448",
        database="student_feedback"
    )

# Function to handle student login
def student_login():
    conn = connect_to_database()
    cursor = conn.cursor()

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.usn = ""

    if not st.session_state.logged_in:
        st.title("Student Login")
        with st.form(key="student_login_form", clear_on_submit=True):
            usn = st.text_input("Enter Student USN", key="student_usn")
            password = st.text_input("Enter Student Password", type="password", key="student_password")
            submitted = st.form_submit_button("Login")

            if submitted:
                cursor.execute("SELECT PASSWORD, NAME FROM students WHERE USN=%s", (usn,))
                student_data = cursor.fetchone()

                if student_data:
                    if password == student_data[0]:
                        st.session_state.logged_in = True
                        st.session_state.usn = usn
                        st.session_state.student_name = student_data[1]  # Store student's name in session state
                        st.success("Student Login Successful")
                        st.rerun()  # Rerun the page to display feedback form
                    else:
                        st.error("Incorrect Student Password")
                else:
                    st.error("Student USN not found")

    # Logout button in the sidebar
    if st.session_state.logged_in:
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.usn = ""
            st.rerun()  # Rerun the page to display login form

    # Redirect to feedback form after login
    if st.session_state.logged_in:
        student_feedback_form()  # Display feedback form only after successful login

# Main function
def main():
    student_login()

if __name__ == "__main__":
    main()
