# Quiz App

A web-based quiz application that allows users to test their knowledge.

## Features
- Real-time scoring
- User-friendly interface

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/neths21/quiz-app.git
2. **Navigate to the project directory:**

   ```bash
   cd quiz-app
3. **Create a virtual environment:**

   ```bash
   python -m venv env

5. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt

6. **Set up environment variables:**

    Create a .env file in the project root and add any necessary environment variables, such as database configurations or secret keys.

7. **Apply database migrations:**

   ```bash
    python manage.py migrate

8. **Run the development server:**

   ```bash
   python manage.py runserver

9. **Access the application in your web browser at:**

   ```bash
   http://localhost:8000
