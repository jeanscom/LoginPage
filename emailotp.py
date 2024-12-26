import streamlit as st
import sqlite3
import random
import smtplib

# Database Initialization
def init_db():
    conn = sqlite3.connect("userotp.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
            U_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email_ID TEXT UNIQUE NOT NULL,
            Phone_No TEXT NOT NULL,
            Course TEXT NOT NULL,
            OTP INTEGER
        )
    """)
    conn.commit()
    conn.close()

# Function to Check if Email is Registered
def is_email_registered(email):
    conn = sqlite3.connect("userotp.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM User WHERE Email_ID = ?", (email,))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

# Function to Send OTP
def send_otp(email):
    otp = random.randint(100000, 999999)
    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_email_password")  # Replace with your email and password

        # Email content
        subject = "Your Verification OTP"
        body = f"Your OTP for login is: {otp}"
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail("your_email@gmail.com", email, message)  # Replace with your email
        server.quit()

        return otp
    except Exception as e:
        st.error(f"Failed to send OTP: {e}")
        return None

# Register User
def register_user(name, email, phone, course):
    conn = sqlite3.connect("userotp.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO User (Name, Email_ID, Phone_No, Course) VALUES (?, ?, ?, ?)",
                       (name, email, phone, course))
        conn.commit()
        st.success("User registered successfully!")
    except sqlite3.IntegrityError:
        st.error("Email already exists. Please try a different email.")
    conn.close()

# Verify User with OTP
def verify_user(email, otp):
    conn = sqlite3.connect("userotp.db")
    cursor = conn.cursor()
    cursor.execute("SELECT OTP FROM User WHERE Email_ID = ?", (email,))
    record = cursor.fetchone()
    conn.close()
    if record and record[0] == otp:
        return True
    return False

# Update OTP in Database
def update_otp(email, otp):
    conn = sqlite3.connect("userotp.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE User SET OTP = ? WHERE Email_ID = ?", (otp, email))
    conn.commit()
    conn.close()

# Streamlit App
st.title("User Registration and Login")

# Choose between Registration or Login
choice = st.sidebar.selectbox("Choose an option", ["Register", "Login"])

if choice == "Register":
    st.subheader("Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    course = st.text_input("Course")

    if st.button("Register"):
        if name and email and phone and course:
            register_user(name, email, phone, course)
        else:
            st.error("All fields are required.")

elif choice == "Login":
    st.subheader("Login")
    email = st.text_input("Email", placeholder="Enter your registered email")

    if st.button("Send OTP"):
        if is_email_registered(email):
            otp = send_otp(email)
            if otp:
                update_otp(email, otp)
                st.success("OTP sent to your email.")
        else:
            st.error("Email not registered. Please register first.")

    entered_otp = st.text_input("Enter OTP", type="password")

    if st.button("Verify OTP"):
        if verify_user(email, int(entered_otp)):
            st.success("Login successful!")
        else:
            st.error("Invalid OTP. Please try again.")

if __name__ == "__main__":
    init_db()
