Smart Feedback QR System

Project Overview

Smart Feedback QR System is a Python and Streamlit application that generates QR codes for feedback records, scans uploaded QR code images, and retrieves the corresponding business information.

Features

Dashboard displaying feedback record statistics
QR code generation for feedback IDs
Download QR codes as PNG images
QR code scanning using OpenCV
Feedback record lookup using NumPy
Invalid feedback ID handling
Feedback URL display and navigation
Interactive Streamlit user interface
Technologies Used
Python
Streamlit
NumPy
qrcode
OpenCV
Pillow
Git and GitHub
Installation

Clone the repository:

git clone https://github.com/YOUR_GITHUB_USERNAME/smart-feedback-qr.git
cd smart-feedback-qr

Create and activate a virtual environment.

On Windows PowerShell:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Install dependencies:

python -m pip install -r requirements.txt
Run the Application
python -m streamlit run app.py
Feedback Data

The demonstration application stores sample feedback records in a NumPy array.

Replace the example feedback URLs with valid URLs before using the application in a real business environment.

Future Improvements

Store feedback records in MongoDB
Add authentication and role-based access
Generate QR codes for dynamically created records
Add feedback analytics and reporting
Deploy the application to Streamlit Community Cloud
Author

Add your name and professional portfolio links here.