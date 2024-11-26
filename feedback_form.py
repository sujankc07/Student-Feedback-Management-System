import streamlit as st
import mysql.connector

# Database Connection
def connect_to_database():
    return mysql.connector.connect(
    host="localhost",
    user="YOUR-USER", 
    password="YOUR-DB-PASSWORD", 
    database="DB-NAME" 
)

# Function to create feedback table with USN as primary key
def create_feedback_table():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            USN VARCHAR(10),
            NAME VARCHAR(25),
            SEM INT,
            SEC CHAR(1),
            TEACHER_NAME VARCHAR(25),
            SUBJECT_NAME VARCHAR(20),
            Q1 INT,
            Q2 INT,
            Q3 INT,
            Q4 INT,
            Q5 INT
        )
    """)
    conn.commit()

# Function to display student feedback form
def student_feedback_form():
    st.title("Student Feedback Form")
    if 'teacher_name' not in st.session_state:
        st.session_state.teacher_name = None
    
    st.write(f"Welcome, {st.session_state.student_name}!")  # Display welcome message with student's name
    conn = connect_to_database()
    cursor = conn.cursor()
    create_feedback_table()

    teacher_name = st.selectbox("Faculty Name", [None, "Anderson", "Davis", "James", "Johnson", "Michael", "Williams"], key="teacher_name")

    # Fetch subjects based on the selected teacher
    if teacher_name:
        cursor.execute("SELECT SUBJECT FROM teachers WHERE TEACHER_NAME = %s", (teacher_name,))
        subjects = cursor.fetchall()
        subject_names = [subject[0] for subject in subjects]
        subject_name = st.selectbox("Select Subject", subject_names, key="subject_name")
    else:
        subject_name = None

    q1 = st.slider("Does the faculty cover the syllabus in depth?", 0, 5, 0, key="q01")
    q2 = st.slider("Is the faculty audible?", 0, 5, 0, key="q02")
    q3 = st.slider("Does the faculty make you think creatively?", 0, 5, 0, key="q03")
    q4 = st.slider("Does the faculty encourage you to ask questions?", 0, 5, 0, key="q04")
    q5 = st.slider("Overall satisfaction level", 0, 5, 0, key="q05")

    submitted = st.button("Submit Feedback")

    if submitted:
        cursor.execute("SELECT USN, NAME, SEM, SEC FROM students WHERE USN=%s", (st.session_state.usn,))
        student_details = cursor.fetchone()
        cursor.execute(
            "INSERT INTO feedback (USN, NAME, SEM, SEC, TEACHER_NAME, SUBJECT_NAME, Q1, Q2, Q3, Q4, Q5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (student_details[0], student_details[1], student_details[2], student_details[3], teacher_name, subject_name, q1, q2, q3, q4, q5))
        conn.commit()
        st.success("Feedback submitted successfully")


# Main function
def main():
    st.title("Student Feedback Form")
    create_feedback_table()
    student_feedback_form()

if __name__ == "__main__":
    main()