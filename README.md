# Marks Calculator on AWS EC2

A web-based application that calculates student marks, percentage, and overall result, deployed on Amazon EC2 to demonstrate cloud hosting and application deployment.

---

## Overview

This project is a simple web application designed to calculate student marks and percentage based on user input.

The application is deployed on an Amazon EC2 instance, providing hands-on experience with cloud deployment, web hosting, and basic application management on AWS.

---

## Project Objective

* Build a web-based marks calculator
* Deploy the application on AWS EC2
* Understand cloud-based application hosting
* Gain practical experience with AWS infrastructure

---

## Architecture

```text
User Browser
      │
      ▼
Amazon EC2 Instance
      │
      ▼
Marks Calculator Application
      │
      ▼
Calculated Result
```

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Amazon EC2
* Linux
* Git & GitHub

---

## Features

* Calculate total marks
* Calculate percentage
* Display results instantly
* Simple and user-friendly interface
* Cloud-hosted application
* Accessible through a public EC2 endpoint

---

## Project Structure

```text
marks-calculator-ec2/

├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

---

## Prerequisites

Before running the application, ensure you have:

* Python 3.x
* Flask
* AWS Account
* EC2 Instance
* Git installed

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/marks-calculator-ec2.git
cd marks-calculator-ec2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## Deployment on AWS EC2

1. Launch an EC2 instance.
2. Configure Security Group rules.
3. Install Python and required dependencies.
4. Clone the repository.
5. Start the Flask application.
6. Access the application using the EC2 public IP.

Example:

```text
http://<EC2-Public-IP>:5000
```

---

## Learning Outcomes

Through this project, I gained practical experience with:

* AWS EC2 deployment
* Linux server management
* Flask web applications
* Security Group configuration
* GitHub version control
* Cloud application hosting

---

## Future Enhancements

* User authentication
* Database integration
* Student record management
* Result history tracking
* Responsive UI improvements
* Docker containerization

---

## Author

**Yash Devdhe**

AWS Cloud & DevOps Enthusiast

Interested in cloud computing, DevOps practices, and building scalable applications on AWS.
