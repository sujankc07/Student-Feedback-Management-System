import streamlit as st
import mysql.connector
from feedback_display import display_average_ratings

# Database Connection
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SujanKC@9448",
        database="student_feedback"
    )

# Function to handle HOD login
def hod_login():
    conn = connect_to_database()
    cursor = conn.cursor()

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.hod_name = ""

    if not st.session_state.logged_in:
        st.title("HOD Login")
        with st.form(key="hod_login_form", clear_on_submit=True):
            username = st.text_input("Enter HOD Username", key="hod_username")
            password = st.text_input("Enter HOD Password", type="password", key="hod_password")
            submitted = st.form_submit_button("Login")

            if submitted:
                cursor.execute("SELECT * FROM hod WHERE user_name=%s AND PASSWORD=%s", (username, password))
                hod_data = cursor.fetchone()

                if hod_data:
                    st.session_state.logged_in = True
                    st.session_state.hod_name = hod_data[0]
                    st.success("HOD Login Successful")
                    st.rerun()
                else:
                    st.error("Invalid HOD Username or Password")

    if st.session_state.logged_in:
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.usn = ""
            st.rerun()

    if st.session_state.logged_in:
        display_average_ratings()
# Main function for HOD login
def main():
    hod_login()

if __name__ == "__main__":
    main()
