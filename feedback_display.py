import streamlit as st
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

# Database Connection
def connect_to_database():
    return mysql.connector.connect(
    host="localhost",
    user="YOUR-USER", 
    password="YOUR-DB-PASSWORD", 
    database="DB-NAME" 
)

# Function to display average feedback ratings for all questions based on the selected teacher
def display_average_ratings():
    conn = connect_to_database()
    cursor = conn.cursor()

    # Fetch distinct teacher names from the database
    cursor.execute("SELECT DISTINCT TEACHER_NAME FROM feedback")
    teachers = [row[0] for row in cursor.fetchall()]

    # Selectbox to choose the teacher (HOD can select any teacher)
    selected_teacher =  st.selectbox("Faculty Name", [None, "Anderson", "Davis", "James", "Johnson", "Michael", "Williams"], key="teacher_name")

    if selected_teacher:
        # Fetch feedback data for the selected teacher
        cursor.execute("SELECT * FROM feedback WHERE TEACHER_NAME=%s", (selected_teacher,))
        teacher_feedback = cursor.fetchall()

        if teacher_feedback:
            # Extract ratings for each question from the feedback data
            questions = ["Q1", "Q2", "Q3", "Q4", "Q5"]
            
            # Convert the values to float, filtering out non-numeric values
            average_ratings = [
                np.mean([float(str(row[questions.index(question) + 7]).replace('.', '', 1)) for row in teacher_feedback if str(row[questions.index(question) + 7]).replace('.', '', 1).isdigit()])
                for question in questions
            ]

            # Fetch subject name from the teachers table
            cursor.execute("SELECT SUBJECT FROM teachers WHERE TEACHER_NAME=%s", (selected_teacher,))
            subject_name = cursor.fetchone()[0]

            # Create a bar chart for average ratings
            plt.figure(figsize=(8, 6))
            plt.bar(questions, average_ratings, color='skyblue')
            plt.xlabel("Questions")
            plt.ylabel("Average Rating")
            plt.title(f"Average Ratings for Each Question - {selected_teacher}")

            # Display subject name above the graph
            plt.suptitle(f"Subject: {subject_name}", y=1.05, fontsize=14)

            st.pyplot(plt)

        else:
            st.write(f"No feedback received for {selected_teacher}.")
    else:
        st.write("Please select a teacher.")

# Main function
def main():
    st.title("Teacher Feedback (HOD View)")
    display_average_ratings()

if __name__ == "__main__":
    main()
