
# login.py
import sqlite3
import streamlit as st
import os
import pandas as pd
import random
import smtplib

# Initialize SQLite database
MAIN_FOLDER = "Course"

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
            U_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email_ID TEXT UNIQUE NOT NULL,
            Password TEXT NOT NULL,
            Course TEXT NOT NULL,   
            Status INTEGER,
            OTP INTEGER
        )
    """)
    conn.commit()
    conn.close()

def fetch_all_users():
    conn = sqlite3.connect("users.db")
    query = "SELECT U_ID, Name, Email_ID, Course FROM User"
    users = pd.read_sql_query(query, conn)  # Return data as a pandas DataFrame
    conn.close()
    return users

# Function to Check if Email is Registered
def is_email_registered(email):
    conn = sqlite3.connect("users.db")
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
        server.login("scomcoaching@gmail.com", "xgbf hqum tlys gweq")  # Replace with your email and password

        # Email content
        subject = "Your Verification OTP"
        body = f"Your OTP for login is: {otp}"
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail("scomcoaching@gmail.com", email, message)  # Replace with your email
        server.quit()

        return otp
    except Exception as e:
        st.error(f"Failed to send OTP: {e}")
        return None

# Verify User with OTP
def verify_user(email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Name, Email_ID, Password, Course FROM User WHERE Email_ID = ? AND Password = ? AND Status = 1", (email, password))
    user = cursor.fetchone()  # This will return a tuple
    conn.close()
    return user    


# Update OTP in Database
def update_otp(email, otp):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE User SET OTP = ? WHERE Email_ID = ?", (otp, email))
    conn.commit()
    conn.close()

# User registration
def register_user(name, email, password, course):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    status = 0
    try:
        cursor.execute("INSERT INTO User (Name, Email_ID, Password, Course, Status) VALUES (?, ?, ?, ?, ?)",
                       (name, email, password, course, status))
        conn.commit()
        st.success("User registered successfully!")
    except sqlite3.IntegrityError:
        st.error("Email already exists. Please try a different email.")
    conn.close()

# Initialize database
init_db()

def login_page():
    # Initialize session state
    if "user" not in st.session_state:
        st.session_state.user = None

    if "otp_sent" not in st.session_state:
        st.session_state.otp_sent = False

    # Streamlit app
    if st.session_state.user:
        # Redirect to appropriate page
        if st.session_state.user["role"] == "Admin":
            st.success(f"Welcome, Admin!")
            admin_page()  # Ensure you have this function for admin actions
        else:
            user_page()  # Ensure you have this function for user actions
    else:
        # Sidebar: Choose between login or register
        choice = st.sidebar.selectbox("Choose an option", ["Login", "Register"])

        def list_folders(main_folder):
            try:
                return [folder for folder in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, folder))]
            except FileNotFoundError:
                st.error(f"The folder '{main_folder}' does not exist.")
                return []

        # User Registration Page
        if choice == "Register":
            st.subheader("User Registration")
            name = st.text_input("Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")

            # Dynamically list courses from subfolders
            main_folder = MAIN_FOLDER
            courses = list_folders(main_folder)

            if courses:
                course = st.selectbox("Select a Course", courses)
            else:
                st.error("No courses available.")
                course = None

            if st.button("Register"):
                if name and email and password and course:
                    register_user(name, email, password, course)
                    st.success(f"Successfully registered for {course}.")
                else:
                    st.error("All fields are required.")

        elif choice == "Login":
            st.subheader("Login")
            email = st.text_input("Email", placeholder="Enter Your Email ID")
            password = st.text_input("Password", placeholder="Enter Your Password", type="password")
        
            if st.button("Send OTP"):
                if email == "admin@gmail.com" and password == "123":
                    st.session_state.user = {
                        "role": "Admin",
                        "name": "Admin",
                        "email": email,
                    }
                    st.success("Welcome, Admin!")
                    st.rerun()
                    
                if is_email_registered(email):
                    otp = send_otp(email)
                    if otp:
                        update_otp(email, otp)
                        st.session_state.otp_sent = True
                        st.success("OTP sent to your email.")
                else:
                    st.error("Email not registered. Please register first.")

            if st.session_state.otp_sent:
                entered_otp = st.text_input("Enter OTP", type="password")

                if st.button("Verify OTP"):
                    if verify_user(email, entered_otp):
                        user = fetch_user(email, password)  # Fetch user details again
                        if user:
                            st.session_state.user = {
                                "role": "User",
                                "name": user[0],  # Accessing by index
                                "email": user[1],
                                "password": user[2],  # This is now correctly accessed
                                "course": user[3],
                            }
                            st.success(f"Welcome, {user[0]}!")
                            st.rerun()
                        else:
                            st.error("Invalid credentials.")
                    else:
                        st.error("Invalid OTP. Please try again.")

def fetch_user(email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Name, Email_ID, Password, Course FROM User WHERE Email_ID = ? AND Password = ? AND Status = 1", (email, password))
    user = cursor.fetchone()  # This will return a tuple
    conn.close()
    return user   


# import sqlite3
# import streamlit as st
# import os
# import pandas as pd
# import random
# import smtplib

# # Initialize SQLite database
# MAIN_FOLDER = "Course"

# def init_db():
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS User (
#             U_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#             Name TEXT NOT NULL,
#             Email_ID TEXT UNIQUE NOT NULL,
#             Password TEXT NOT NULL,
#             Course TEXT NOT NULL,   
#             Status INTEGER,
#             OTP INTEGER
#         )
#     """)
#     conn.commit()
#     conn.close()

# def fetch_all_users():
#     conn = sqlite3.connect("users.db")
#     query = "SELECT U_ID, Name, Email_ID, Course FROM User"
#     users = pd.read_sql_query(query, conn)  # Return data as a pandas DataFrame
#     conn.close()
#     return users

# # Function to Check if Email is Registered
# def is_email_registered(email):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT COUNT(*) FROM User WHERE Email_ID = ?", (email,))
#     count = cursor.fetchone()[0]
#     conn.close()
#     return count > 0

# # Function to Send OTP
# def send_otp(email):
#     otp = random.randint(100000, 999999)
#     try:
#         # Set up the SMTP server
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login("scomcoaching@gmail.com","xgbf hqum tlys gweq")  # Replace with your email and password

#         # Email content
#         subject = "Your Verification OTP"
#         body = f"Your OTP for login is: {otp}"
#         message = f"Subject: {subject}\n\n{body}"

#         server.sendmail("scomcoaching@gmail.com", email, message)  # Replace with your email
#         server.quit()

#         return otp
#     except Exception as e:
#         st.error(f"Failed to send OTP: {e}")
#         return None

# # Verify User with OTP
# def verify_user(email, otp):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT OTP FROM User WHERE Email_ID = ?", (email,))
#     record = cursor.fetchone()
#     conn.close()
#     if record and record[0] == otp:
#         return True
#     return False

# # Update OTP in Database
# def update_otp(email, otp):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("UPDATE User SET OTP = ? WHERE Email_ID = ?", (otp, email))
#     conn.commit()
#     conn.close()

# # User registration
# def register_user(name, email, password, course):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     status = 0
#     try:
#         cursor.execute("INSERT INTO User (Name, Email_ID, Password, Course, Status) VALUES (?, ?, ?, ?, ?)",
#                        (name, email, password, course, status))
#         conn.commit()
#         st.success("User  registered successfully!")
#     except sqlite3.IntegrityError:
#         st.error("Email already exists. Please try a different email.")
#     conn.close()

# # Initialize database
# init_db()

# def login_page():
#     # Initialize session state
#     if "user" not in st.session_state:
#         st.session_state.user = None

#     # Streamlit app
#     if st.session_state.user:
#         # Redirect to appropriate page
#         if st.session_state.user["role"] == "Admin":
#             st.success(f"Welcome, Admin!")
#             admin_page()  # Ensure you have this function for admin actions
#         else:
#             user_page()  # Ensure you have this function for user actions
#     else:
#         # Sidebar: Choose between login or register
#         choice = st.sidebar.selectbox("Choose an option", ["Login", "Register"])

#         def list_folders(main_folder):
#             try:
#                 return [folder for folder in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, folder))]
#             except FileNotFoundError:
#                 st.error(f"The folder '{main_folder}' does not exist.")
#                 return []

#         # User Registration Page
#         if choice == "Register":
#             st.subheader("User Registration")
#             name = st.text_input("Name")
#             email = st.text_input("Email")
#             password = st.text_input("Password", type="password")

#             # Dynamically list courses from subfolders
#             main_folder = MAIN_FOLDER
#             courses = list_folders(main_folder)

#             if courses:
#                 course = st.selectbox("Select a Course", courses)
#             else:
#                 st.error("No courses available.")
#                 course = None

#             if st.button("Register"):
#                 if name and email and password and course:
#                     register_user(name, email, password, course)
#                     st.success(f"Successfully registered for {course}.")
#                 else:
#                     st.error("All fields are required.")

#         elif choice == "Login":
#             st.subheader("Login")
#             email = st.text_input("Email", placeholder="Enter Your Email ID")
#             password = st.text_input("Password", placeholder="Enter Your Password", type="password")
        
#             if st.button("Send OTP"):
                    
#                 if email == "admin@gmail.com" and password == "123":
#                     st.session_state.user = {
#                         "role": "Admin",
#                         "name": "Admin",
#                         "email": email,
#                     }
#                     st.success("Welcome, Admin!")
#                     st.rerun()
                    
#                 if is_email_registered(email):
#                     otp = send_otp(email)
#                     if otp:
#                         update_otp(email, otp)
#                         st.success("OTP sent to your email.")
#                 else:
#                     st.error("Email not registered. Please register first.")

#             entered_otp = st.text_input("Enter OTP", type="password")

#             if st.button("Verify OTP"):
#                 if verify_user(email, password):
#                     user = verify_user(email, password)  # Fetch user details again
#                     if user:
#                         st.session_state.user = {
#                             "role": "User ",
#                             "name": user[0],  # Accessing by index
#                             "email": user[1],
#                             "password": user[2],  # This is now correctly accessed
#                             "course": user[3],
#                         }
#                         st.success(f"Welcome, {user[0]}!")
#                         st.rerun()
#                     else:
#                         st.error("Invalid credentials.")
#                 else:
#                     st.error("Invalid OTP. Please try again.")

# def verify_user(email, password):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT Name, Email_ID, Password, Course FROM User WHERE Email_ID = ? AND Password = ? AND Status = 1", (email, password))
#     user = cursor.fetchone()  # This will return a tuple
#     conn.close()
#     return user    

def admin_page(): 
    if st.sidebar.button("Logout"):
        st.session_state.user = None  # Clear user session  
        st.success("You have been logged out successfully!")
        st.rerun()

    st.title("Admin Dashboard")
    main_folder = MAIN_FOLDER  # Shared folder path

    admin_option = st.sidebar.selectbox(
    "Choose an action:",
    ["Manage Files", "Manage Users", "Manage Courses"])
    #course_action = st.sidebar.selectbox("Manage Course:", ["Add New Course", "View Courses", "Edit Courses", "Delete Courses"])

    if admin_option == "Manage Files":
        file_action = st.sidebar.selectbox("Manage files:", ["Upload Files", "Delete Uploaded Files"])
        if file_action == "Upload Files":
        # File management logic 
            st.subheader("Manage Program Files")
            program_folders = list_folders(main_folder)
            if program_folders:
                selected_program_folder = st.selectbox("Select a program folder:", program_folders)
                if selected_program_folder:
                    program_folder_path = os.path.join(main_folder, selected_program_folder)

                    # Get the expected file extension for this course
                    metadata_path = os.path.join(program_folder_path, "metadata.txt")
                    if os.path.exists(metadata_path):
                        with open(metadata_path, "r") as meta_file:
                            expected_extension = meta_file.readline().strip().replace("File Extension: ", "")
                        st.write(f"Expected File Extension: **{expected_extension}**")
                    else:
                        expected_extension = None
                        st.warning(f"Metadata not found for {selected_program_folder}. File extension validation will be skipped.")

                    # List subfolders in the program folder
                    subfolders = list_folders(program_folder_path)
                    if subfolders:
                        selected_subfolder = st.selectbox("Select a subfolder to upload files:", subfolders)
                        if selected_subfolder:
                            subfolder_path = os.path.join(program_folder_path, selected_subfolder)

                            uploaded_files = st.file_uploader(
                                "Upload files", 
                                type=None,  # Allow all file types initially
                                accept_multiple_files=True
                            )

                            if uploaded_files:
                                for uploaded_file in uploaded_files:
                                    file_extension = os.path.splitext(uploaded_file.name)[1]

                                    # Check if the file extension matches the expected one
                                    if expected_extension and file_extension != expected_extension:
                                        st.error(f"File '{uploaded_file.name}' has an invalid extension. Expected: {expected_extension}")
                                    else:
                                        # Save the file
                                        save_file_to_folder(uploaded_file, subfolder_path)
                    else:
                        st.info(f"No subfolders found in {selected_program_folder}. Create a new subfolder to proceed.")

                    # Create a new subfolder
                    new_subfolder_name = st.text_input("Enter the name of the new subfolder:")
                    if st.button("Create Subfolder"):
                        if new_subfolder_name.strip():
                            create_subfolder(program_folder_path, new_subfolder_name.strip())
                        else:
                            st.warning("Please enter a valid subfolder name.")
            else:
                st.info(f"No program folders found in {main_folder}. Add program folders first.")

        elif file_action == "Delete Uploaded Files":
            st.subheader("Delete Uploaded Files")
            program_folders = list_folders(main_folder)
            if program_folders:
                selected_program_folder = st.selectbox("Select a program folder:", program_folders)
                if selected_program_folder:
                    program_folder_path = os.path.join(main_folder, selected_program_folder)

                    subfolders = list_folders(program_folder_path)
                    if subfolders:
                        selected_subfolder = st.selectbox("Select a subfolder:", subfolders)
                        subfolder_path = os.path.join(program_folder_path, selected_subfolder)
                        
                        # List files in the subfolder
                        uploaded_files = os.listdir(subfolder_path)
                        if uploaded_files:
                            selected_file = st.selectbox("Select a file to delete:", uploaded_files)
                            if st.button("Delete File"):
                                delete_file(subfolder_path, selected_file)
                        else:
                            st.info("No files found in the selected subfolder.")
                    else:
                        st.info(f"No subfolders found in {selected_program_folder}.")
            else:
                st.info(f"No program folders found in {main_folder}. Add program folders first.")

        
    elif admin_option == "Manage Users":
        user_action = st.sidebar.selectbox("User Management Options:", ["View Users", "Edit User", "Delete User"])
        if user_action == "View Users":
            st.subheader("All Registered Users")

            # Filter users by status
            user_status_filter = st.selectbox(
                "Filter Users by Status:",
                ["All Users", "Active Users", "Inactive Users"]
            )

            # Determine status filter value
            if user_status_filter == "Active Users":
                status_filter_value = 1
            elif user_status_filter == "Inactive Users":
                status_filter_value = 0
            else:
                status_filter_value = None  # No filter applied for "All Users"

            # Fetch filtered users
            users_df = fetch_all_users(status_filter_value)

            if not users_df.empty:
                st.dataframe(users_df)  # Display in tabular form
            else:
                st.info(f"No {user_status_filter.lower()} found in the database.")

        elif user_action == "Edit User":
            st.subheader("Edit User")

            # Select Active or Inactive users
            user_status_filter = st.selectbox(
                "Filter Users by Status:",
                ["Active Users", "Inactive Users"]
            )
            status_filter_value = 1 if user_status_filter == "Active Users" else 0

            # Fetch users based on the selected status
            conn = sqlite3.connect("users.db")
            query = "SELECT U_ID, Name FROM User WHERE Status = ?"
            users_df = pd.read_sql_query(query, conn, params=(status_filter_value,))
            conn.close()

            if not users_df.empty:
                user_options = users_df.set_index("U_ID")["Name"].to_dict()
                selected_user_id = st.selectbox(
                    "Select a user to edit:",
                    options=list(user_options.keys()),
                    format_func=lambda x: f"{x} - {user_options[x]}"
                )

                # Fetch details of the selected user
                conn = sqlite3.connect("users.db")
                cursor = conn.cursor()
                cursor.execute("SELECT Name, Email_ID, Password, Course, Status FROM User WHERE U_ID = ?", (selected_user_id,))
                user_data = cursor.fetchone()
                conn.close()

                if user_data:
                    # Dynamically list courses from subfolders
                    courses = list_folders(MAIN_FOLDER)
                    if courses:
                        # Populate with the current course as default
                        selected_course = st.selectbox(
                            "Select a Course",
                            options=courses,
                            index=courses.index(user_data[3]) if user_data[3] in courses else 0
                        )
                    else:
                        st.error("No courses found.")
                        selected_course = None

                    # Pre-fill the form fields with existing user data
                    name = st.text_input("Name", value=user_data[0])
                    email = st.text_input("Email", value=user_data[1])
                    password = st.text_input("Password", value=user_data[2], type="password")
                    status1 = st.selectbox(
                        "Status",
                        options=["Active", "Inactive"],
                        index=0 if user_data[4] == 1 else 1
                    )
                    # Map status label to corresponding value
                    status_value = 1 if status1 == "Active" else 0

                    # Button to update the profile
                    if st.button("Update Profile"):
                        if name.strip() and email.strip() and password.strip() and selected_course:
                            # Update user in the database
                            edit_user(selected_user_id, name.strip(), email.strip(), password.strip(), selected_course, status_value)
                        else:
                            st.warning("All fields are required.")
                else:
                    st.error("Error fetching user details. Please try again.")
            else:
                st.info(f"No {user_status_filter.lower()} found in the database.")
    
        elif user_action == "Delete User":
                st.subheader("Delete User")
                
                # Fetch all users as a DataFrame
                users_df = fetch_all_users()
                if not users_df.empty:
                    user_options = users_df.set_index("U_ID")["Name"].to_dict()
                    selected_user_id = st.selectbox(
                        "Select a user to delete:",
                        options=list(user_options.keys()),
                        format_func=lambda x: f"{x} - {user_options[x]}"
                    )

                    if st.button("Delete User"):
                        confirm = st.confirmation("Are you sure you want to delete this user?")
                        if confirm:
                            delete_user(selected_user_id)
                        else:
                            st.warning("No user was deleted.")
                else:
                    st.info("No users found in the database.")
    
    elif admin_option == "Manage Courses":
        course_action = st.sidebar.selectbox("Course Management Options:", ["Add New Course", "View Courses", "Edit Courses", "Delete Courses", "Add New Module"])
        if course_action == "Add New Course":
            st.subheader("Add New Course")
            
            # Input fields for the course name and file extension
            new_course_name = st.text_input("Enter the name of the new course:")
            file_extension = st.text_input("Enter the file extension for this course (e.g., '.py', '.txt'):")

            if st.button("Create Course"):
                if new_course_name.strip() and file_extension.strip():
                    # Ensure the file extension starts with a dot
                    if not file_extension.startswith("."):
                        file_extension = f".{file_extension}"

                    course_path = os.path.join(main_folder, new_course_name.strip())
                    try:
                        if not os.path.exists(course_path):
                            # Create the course folder
                            os.makedirs(course_path)

                            # Save the file extension to a metadata file or database
                            metadata_path = os.path.join(course_path, "metadata.txt")
                            with open(metadata_path, "w") as meta_file:
                                meta_file.write(f"File Extension: {file_extension}\n")

                            st.success(f"Course '{new_course_name}' has been added successfully with file extension '{file_extension}'.")
                        else:
                            st.warning(f"Course '{new_course_name}' already exists.")
                    except Exception as e:
                        st.error(f"Error creating course: {e}")
                else:
                    st.warning("Please enter both the course name and file extension.") 

        elif course_action == "View Courses":
            st.subheader("View Courses")

            # List all courses
            courses = list_folders(main_folder)
            if courses:
                st.write("Courses Available:")
                for course in courses:
                    metadata_path = os.path.join(main_folder, course, "metadata.txt")
                    if os.path.exists(metadata_path):
                        with open(metadata_path, "r") as meta_file:
                            file_extension = meta_file.readline().strip().replace("File Extension: ", "")
                        st.write(f"- **{course}** (File Extension: {file_extension})")
                    else:
                        st.write(f"- **{course}** (No metadata found)")
            else:
                st.info("No courses available. Please add a new course.")

        elif course_action == "Edit Courses":
            st.subheader("Edit Course")

            # Select a course to edit
            courses = list_folders(main_folder)
            if courses:
                selected_course = st.selectbox("Select a course to edit:", courses)

                if selected_course:
                    metadata_path = os.path.join(main_folder, selected_course, "metadata.txt")
                    if os.path.exists(metadata_path):
                        with open(metadata_path, "r") as meta_file:
                            file_extension = meta_file.readline().strip().replace("File Extension: ", "")
                    else:
                        file_extension = ""

                    # Input fields to edit course name and file extension
                    new_course_name = st.text_input("Edit Course Name:", value=selected_course)
                    new_file_extension = st.text_input("Edit File Extension:", value=file_extension)

                    if st.button("Update Course"):
                        if new_course_name.strip() and new_file_extension.strip():
                            # Ensure the file extension starts with a dot
                            if not new_file_extension.startswith("."):
                                new_file_extension = f".{new_file_extension}"

                            # Rename course folder
                            new_course_path = os.path.join(main_folder, new_course_name.strip())
                            try:
                                if selected_course != new_course_name.strip():
                                    os.rename(os.path.join(main_folder, selected_course), new_course_path)

                                # Update metadata
                                metadata_path = os.path.join(new_course_path, "metadata.txt")
                                with open(metadata_path, "w") as meta_file:
                                    meta_file.write(f"File Extension: {new_file_extension}\n")

                                st.success(f"Course '{selected_course}' updated successfully!")
                            except Exception as e:
                                st.error(f"Error updating course: {e}")
                        else:
                            st.warning("Please enter valid values for course name and file extension.")
            else:
                st.info("No courses available to edit.")

        elif course_action == "Delete Courses":
            st.subheader("Delete Course")

            # Select a course to delete
            courses = list_folders(main_folder)
            if courses:
                selected_course = st.selectbox("Select a course to delete:", courses)

                if selected_course:
                    if st.button("Confirm Delete"):
                        try:
                            # Delete the course folder and its contents
                            course_path = os.path.join(main_folder, selected_course)
                            for root, dirs, files in os.walk(course_path, topdown=False):
                                for file in files:
                                    os.remove(os.path.join(root, file))
                                for dir in dirs:
                                    os.rmdir(os.path.join(root, dir))
                            os.rmdir(course_path)

                            st.success(f"Course '{selected_course}' has been deleted successfully!")
                        except Exception as e:
                            st.error(f"Error deleting course: {e}")
            else:
                st.info("No courses available to delete.")
        
        elif course_action == "Add New Module":
            # Create a new subfolder
            program_folders = list_folders(main_folder)
            if program_folders:
                selected_program_folder = st.selectbox("Select a program folder:", program_folders)
                new_subfolder_name = st.text_input("Enter the name of the Module:")
                if selected_program_folder:
                    program_folder_path = os.path.join(main_folder, selected_program_folder)
                    if st.button("Create Subfolder"):
                            if new_subfolder_name.strip():
                                create_subfolder(program_folder_path, new_subfolder_name.strip())
                            else:
                                st.warning("Please enter a valid subfolder name.")
                            if selected_program_folder:
                                program_folder_path = os.path.join(main_folder, selected_program_folder)
                            
# Helper Function for Deleting Files
def delete_file(folder_path, file_name):
    """Deletes a file from the specified folder."""
    file_path = os.path.join(folder_path, file_name)
    try:
        os.remove(file_path)
        st.success(f"File '{file_name}' has been deleted successfully.")
    except FileNotFoundError:
        st.error(f"File '{file_name}' not found.")
    except Exception as e:
        st.error(f"Error deleting file: {e}")

# Utility Functions (unchanged from previous)
def list_folders(main_folder):
    """List all subfolders in the specified main folder."""
    try:
        return [folder for folder in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, folder))]
    except FileNotFoundError:
        st.error(f"The folder '{main_folder}' does not exist.")
        return []

def save_file_to_folder(file, folder_path):
    """Save the uploaded file to the specified folder."""
    os.makedirs(folder_path, exist_ok=True)
    try:
        if isinstance(file, list):  # Check if file is a list (in case of multiple uploads)
            for single_file in file:
                with open(os.path.join(folder_path, single_file.name), "wb") as f:
                    f.write(single_file.getbuffer())
                st.success(f"File '{single_file.name}' saved to folder '{folder_path}'.")
        else:  # If a single file
            with open(os.path.join(folder_path, file.name), "wb") as f:
                f.write(file.getbuffer())
            st.success(f"File '{file.name}' saved to folder '{folder_path}'.")
    except Exception as e:
        st.error(f"Error saving file: {e}")

def create_subfolder(parent_folder, subfolder_name):
    """Create a new subfolder inside an existing subfolder."""
    folder_path = os.path.join(parent_folder, subfolder_name)
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            st.success(f"Subfolder '{subfolder_name}' created successfully in '{parent_folder}'.")
        else:
            st.warning(f"Subfolder '{subfolder_name}' already exists in '{parent_folder}'.")
    except Exception as e:
        st.error(f"Error creating subfolder: {e}")

def edit_user(user_id, name, email, password, course, status1):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE User
            SET Name = ?, Email_ID = ?, Password = ?, Course = ?, status=?
            WHERE U_ID = ?
        """, (name, email, password, course, status1, user_id))
        conn.commit()
        st.success("User updated successfully!")
    except sqlite3.IntegrityError:
        st.error("Email already exists. Please try a different email.")
    conn.close()

# Delete a user
def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM User WHERE U_ID = ?", (user_id,))
    conn.commit()
    conn.close()
    st.success("User deleted successfully!")

# Update user password
def updatepassword(email, new_password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE User SET Password = ? WHERE Email_ID = ?", (new_password, email))
    conn.commit()
    conn.close()


def user_page():
    """Main User Page containing navigation to Profile, File Browsing, and Change Password."""
        
    if st.sidebar.button("Logout"):
        st.session_state.user = None  # Clear user session  
        st.success("You have been logged out successfully!")
        st.rerun()
    # Change Password Page
    def profile_page():
        """Display the user's profile page."""
        if "user" not in st.session_state or not st.session_state.user:
            st.error("User session expired. Please log in again.")
            st.stop()

        user = st.session_state.user

        # Display user details
        st.subheader("Your Profile")
        st.write(f"**Name:** {user['name']}")
        st.write(f"**Email:** {user['email']}")
        st.write(f"**Password:** {user['password']}")
        st.write(f"**Course Enrolled:** {user['course']}")
        st.button("Change Password")

        # Button to navigate to change password page
        if st.button("Change Password"):
            st.session_state.page = "change_password"
            st.rerun()


    def change_password_page():
        """Allows the user to change their password."""
        if "user" not in st.session_state or not st.session_state.user:
            st.error("User session expired. Please log in again.")
            st.stop()

        user = st.session_state.user

        st.subheader("Change Your Password")

        # Input fields for password change
        current_password = st.text_input("Current Password", type="password")
        new_password = st.text_input("New Password", type="password")
        reenter_new_password = st.text_input("Re-enter New Password", type="password")

        # Validate and process the password change
        if st.button("Change Password"):
            if current_password != user["password"]:
                st.error("The current password is incorrect.")
            elif new_password != reenter_new_password:
                st.error("New passwords do not match. Please try again.")
            elif len(new_password) < 3:
                st.error("Password should be at least 3 characters long.")
            else:
                # Update password in the database
                updatepassword(email=user["email"], new_password=new_password)

                # Update session state with new password
                st.session_state.user["password"] = new_password

                st.success("Password changed successfully!")

    def change_password_page():
        """Allows the user to change their password."""
        if "user" not in st.session_state or not st.session_state.user:
            st.error("User session expired. Please log in again.")
            st.stop()

        user = st.session_state.user

        st.subheader("Change Your Password")

        # Input fields for password change
        current_password = st.text_input("Current Password", type="password")
        new_password = st.text_input("New Password", type="password")
        reenter_new_password = st.text_input("Re-enter New Password", type="password")

        # Validate and process the password change
        if st.button("Change Password"):
            if current_password != user["password"]:
                st.error("The current password is incorrect.")
            elif new_password != reenter_new_password:
                st.error("New passwords do not match. Please try again.")
            elif len(new_password) < 3:
                st.error("Password should be at least 3 characters long.")
            else:
                # Update password in the database
                updatepassword(email=user["email"], new_password=new_password)

                # Update session state with new password
                st.session_state.user["password"] = new_password

                st.success("Password changed successfully!")

    # Profile Page
    def profile_page():
        """Display the user's profile page."""
        if "user" not in st.session_state or not st.session_state.user:
            st.error("User session expired. Please log in again.")
            st.stop()

        user = st.session_state.user

        # Display user details
        st.subheader("Your Profile")
        st.write(f"**Name:** {user['name']}")
        st.write(f"**Email:** {user['email']}")
        st.write(f"**Password:** {user['password']}")
        st.write(f"**Course Enrolled:** {user['course']}")

        # Logout Button
    def file_browsing_page():
        """Allows users to browse and view course files."""
        
        main_folder = MAIN_FOLDER
        user_course = st.session_state.user.get("course", "Unknown")

        folder_path = os.path.join(main_folder, user_course)
        subfolders = list_folders(folder_path)

        if subfolders:
            selected_folder = st.sidebar.selectbox("Select a subfolder:", subfolders, key="folder_select")
            full_subfolder_path = os.path.join(folder_path, selected_folder)
            formatted_folder_name = selected_folder.replace("_", " ").replace("-", " ")  # Replace underscores and hyphens with spaces
            st.title(f"Module: {formatted_folder_name}")  # Display formatted subfolder name as title

            files = list_files(full_subfolder_path)
            #st.write(files)
            if files:
                if "current_file_index" not in st.session_state:
                    st.session_state.current_file_index = 0

                file_index = st.session_state.current_file_index
                #st.write(file_index)
                selected_file = files[file_index]
                file_path = os.path.join(full_subfolder_path, selected_file)

                try:
                    lines = read_file(file_path)
                    if lines:
                        lines_per_page = st.sidebar.slider("Lines per page", 5, 20, 10, key="lines_per_page_slider")
                        total_pages = (len(lines) - 1) // lines_per_page + 1
                        page = st.number_input("Page", min_value=0, max_value=total_pages - 1, value=0, step=1, key="page_number_input")
                        st.write(f"Displaying file: **{selected_file}** from folder: **{selected_folder}**")
                        display_code_page(lines, page, lines_per_page)

                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button("Previous Slide"):
                                st.session_state.current_file_index = (file_index - 1) % len(files)
                                st.rerun()
                        with col2:
                            if st.button("Next Slide"):
                                st.session_state.current_file_index = (file_index + 1) % len(files)
                                st.rerun()

                        st.caption(f"Slide {file_index + 1} of {len(files)}")
                    else:
                        st.warning(f"The file `{selected_file}` appears to be empty.")
                except Exception as e:
                    st.error(f"Unable to read the file `{selected_file}`: {e}")
            else:
                st.info(f"No files found in {selected_folder}.")
        else:
            st.info(f"No subfolders found in {folder_path}.")

    def display_code_page(lines, page, lines_per_page=10):
        """Displays a specific page of code."""
        start_line = page * lines_per_page
        end_line = start_line + lines_per_page
        code_page = lines[start_line:end_line]

        if code_page:
            st.code(''.join(code_page))
        else:
            st.warning("No more lines to display.")
        return len(code_page)

    def list_folders(main_folder):
        """List all subfolders in the specified main folder."""
        try:
            return [folder for folder in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, folder))]
        except FileNotFoundError:
            st.error(f"The folder '{main_folder}' does not exist.")
            return []

    def list_files(folder_path):
        """List all files in the specified folder."""
        try:
            return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        except FileNotFoundError:
            st.error("Folder not found. Please check the folder path.")
            return []

    def read_file(filepath):
        """Reads the file and returns its content split into lines."""
        try:
            with open(filepath, 'r') as file:
                return file.readlines()
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return []
   
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Profile", "Browse Files", "Change Password"])



    if page == "Profile":
        profile_page()
    elif page == "Browse Files":
        file_browsing_page()
    elif page == "Change Password":
        change_password_page()


if __name__ == "__main__":
    init_db()  # Initialize the database
    login_page()

