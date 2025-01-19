# Tkinter-Login-Form
# Login and Registration Form

This is a login and registration form application developed using Python's Tkinter library and MySQL. The application allows users to register with a unique username and password, which are stored in a MySQL database. Users can log in using their registered credentials, and the application provides error messages for empty fields or mismatched data.

## Features

- User registration with unique username and password
- User login with registered credentials
- Error messages for empty fields
- Error messages for data mismatches
- Developed using Tkinter for the GUI
- Uses MySQL for database management

## Prerequisites

- Python 3.x
- MySQL
- Visual Studio Code (or any other IDE)
- Required Python libraries:
  - tkinter
  - mysql-connector-python

## Installation

Installation of mysql-connector for making connection between the mysql and tkinter. The command is given below, type it in terminal.
  pip install mysql-connector-python

## Set up the MySQL database:

- Create a new database named student
- Create a table named registered with the following columns:
- Id(INTEGER, AUTO_INCREMENT, PRIMARY KEY)
- Username (VARCHAR(50), UNIQUE, NOT NULL)
- password (VARCHAR(50), NOT NULL)

## Usage
- Run the application in terminal of vscode : python main.py
- The login and registration form window will appear.
- Register a new user by entering a unique username and password.
- Log in using the registered username and password.
- The application will display error messages for empty fields or data mismatches.

## Screenshots

The below screenshots will be helful to understand the GUI of this form.

![Screenshot (316)](https://github.com/user-attachments/assets/344cc509-0326-4454-93a3-e4785810d960)
![Screenshot (317)](https://github.com/user-attachments/assets/b3a607d3-c8c3-4929-b3c6-615b892d65cb)
![Screenshot (318)](https://github.com/user-attachments/assets/bc0b6871-ca7e-4789-a90a-3993417d4879)
![Screenshot (319)](https://github.com/user-attachments/assets/0ecf2818-f822-48fe-ac8e-81d8a4ed78f4)
![Screenshot (320)](https://github.com/user-attachments/assets/0272f42a-ed98-4d92-a1ce-feb4cc25aff7)
![Screenshot (321)](https://github.com/user-attachments/assets/35475624-f161-4094-ab34-75c4b03f7c83)
![Screenshot (322)](https://github.com/user-attachments/assets/7db1c8bd-94b2-40b5-8968-e8c6623eb673)
![Screenshot (323)](https://github.com/user-attachments/assets/228df9b5-c911-43ad-b40a-bf774a84046f)
![Screenshot (324)](https://github.com/user-attachments/assets/941adae0-43d5-4cae-b31b-37b74c7d51f4)
![Screenshot (325)](https://github.com/user-attachments/assets/104c7c09-e331-4223-b5df-31b2ba82f0f0)

## Acknowledgements

- Tkinter - Python's standard GUI library
- MySQL - Open-source relational database management system
