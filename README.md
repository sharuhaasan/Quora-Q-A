# Quora-Q-A

A simple Q&A web application built using Django — inspired by Quora.  
Users can register, log in, post questions, answer the questions, and like answers.

---

## Features

- User registration and login/logout system
- Post new questions
- View all posted questions
- Answer any question
- Like answers posted by other users
- Login required for posting, answering, or liking

---

##  Setup Instructions

###  Clone the Repository

```
git clone https://github.com/sharuhaasan/Quora-Q-A.git
cd quora
```

##  Create and Activate Virtual Environment:
```
python -m venv venv
venv\Scripts\activate
```

##  Install Dependencies:
```
pip install -r requirements.txt
```

##  Run Migrations:
```
python manage.py makemigrations
python manage.py migrate
```

##  Start the Development Server:
```
python manage.py runserver
```
---

##  URL Patterns & What They Do

Here’s a breakdown of each view and its purpose:

| URL                         | View Name         | Method(s) | Description                                                  | Login Required   |
|---------------------------- |-------------------|-----------|--------------------------------------------------------------|------------------|
| `/`                         | `home`            | GET       | Displays all posted questions.                               | ❌               |
| `/login/`                   | `login`           | GET, POST | Displays login form and handles login.                       | ❌               |
| `/logout/`                  | `logout`          | POST      | Logs out the current user.                                   | ✅               |
| `/register/`                | `register`        | GET, POST | Displays registration form and creates new user.             | ❌               |
| `/ask/`                     | `ask_question`    | GET, POST | Displays question form; allows users to post.                | ✅               |
| `/question/<int:pk>/`       | `question_detail` | GET, POST | Shows question details and its answers. Handles new answers. | ✅ (for posting) |
| `/like/<int:answer_id>/`    | `like_answer`     | GET       | Increments like count for the specified answer.              | ✅               |

---

##  Forms Used

| Form Name          | Purpose                          |
|--------------------|----------------------------------|
| `UserRegisterForm` | For registering new users        |
| `QuestionForm`     | For posting new questions        |
| `AnswerForm`       | For answering questions          |

All forms are built using **Django Forms** and rendered in templates using `{{ form.as_p }}`.

---

##  Authentication & Access Control

- Users must **log in** to:
  - Ask a question
  - Submit an answer
  - Like an answer
- Unauthenticated users can:
  - View questions
  - See answers
  - Navigate to login/register

---

##  Example Workflow

1. User visits homepage: `/`
2. Clicks "Register" or "Login"
3. Once logged in, can:
   - Ask a question via `/ask/`
   - Click on a question to view answers
   - Submit an answer and like others’ responses

---

##  Notes

- CSRF protection is enabled on all forms.
- Login/logout use Django's built-in `LoginView` and `LogoutView`.


##  Testing in Django Shell:
```
from django.contrib.auth.models import User
from yourapp.models import Question, Answer, Like

User.objects.all()
Question.objects.all()
```


