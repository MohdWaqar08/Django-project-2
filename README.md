# Reddit-Inspired Discussion Platform (Traditional Django MVT)

A Reddit-inspired full-stack web application built using **traditional Django (MVT architecture & Class-Based Views)** and **Tailwind CSS**, created to showcase core Django backend development, relational database modeling, authentication, and authorization.

## Key Features
- **Authentication & Account Management:** User registration, login/logout, and password change flows.
- **Communities & Content:** Create and browse subreddits, publish posts with image upload support, and participate in nested comments.
- **Engagement & Discovery:** Upvote/downvote score sorting, search, pagination, and author-only edit/delete authorization.
- **Responsive UI:** Styled with Tailwind CSS using a shared base template architecture and dark mode support.

## Tech Stack
- **Backend:** Python, Django (MVT, Class-Based Views, ORM)
- **Frontend:** Django Templates, Tailwind CSS
- **Database:** SQLite
- **Deployment:** WhiteNoise, Gunicorn

## Running Locally

```bash
git clone [https://github.com/](https://github.com/)MohdWaqar08/Django-project-2.git
cd Django-project-2
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Live Demo
[Live Demo](https://MohdWaqar08.pythonanywhere.com/blog/)
> **Viewing Note:** Best experienced on desktop or laptop screens. Mobile view is functional, though a few minor layout/UI rough edges remain.