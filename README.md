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

