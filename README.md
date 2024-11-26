# **Student Feedback Management System**

A web application to collect and analyze student feedback for faculty performance, built using **Python**, **Streamlit**, and **MySQL**.

---

## **Features**
- **Student Feedback Form**  
  Allows students to rate faculty performance based on predefined questions using a simple slider interface.

- **HOD View**  
  Enables Heads of Departments to view and analyze average ratings for each faculty member using bar charts for better insights.

- **Dynamic Subject Selection**  
  Automatically fetches and displays subjects based on the selected faculty for more accurate feedback.

- **Database Integration**  
  MySQL database securely stores all feedback, faculty, and subject information.

---

## **Project Structure**
  ```bash
  ├── feedback_form.py       # Handles the student feedback form interface
  ├── feedback_display.py    # Displays feedback results for HOD analysis
  ├── Home.py                # Main navigation and welcome page
  ├── image.png              # Branding image displayed on the home page
  ├── README.md              # Project documentation
  └── requirements.txt       # List of dependencies
   ```
## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/sujankc07/Student-Feedback-Management-System.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd Student-Feedback-Management-System
    ```
3. **Install required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up the MySQL database:**

    - Install and configure MySQL Server and MySQL Workbench.
    - Use MySQL Workbench to create a database named student_feedback.
    - Create tables for feedback, teachers, and students as required.

5. **Update database connection details in the project: Replace the following section in feedback_form.py and feedback_display.py with your own MySQL database details:**
    ```python
      return mysql.connector.connect(
      host="localhost",
      user="YOUR-USER", 
      password="YOUR-DB-PASSWORD", 
      database="DB-NAME" 
    )
    ```
    - **YOUR-USER**: Replace with your MySQL username.
    - **YOUR-DB-PASSWORD**: Replace with your MySQL password.
    - **DB-NAME**: Replace with the name of your database (e.g., student_feedback).

## Usage
1. **Run the application:**
    ```bash
    streamlit run Home.py
    ```
2. **Open the app in your browser (default: http://localhost:8501).**

3. **Use the sidebar to navigate between the feedback form and the HOD view.**

    Requirements
    - Python: 3.7 or above
    - Streamlit: Latest version
    - MySQL Server: For database management
    - MySQL Workbench: For database configuration and management
    - Matplotlib: For data visualization
    - Pillow: For image handling

## Future Enhancements

- Add authentication for students and HODs.
- Generate detailed feedback reports in PDF/Excel formats.
- Include options for feedback summary and trends over time.
