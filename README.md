# Flask URL Shortener

A simple, clean, and modular URL shortener built with Flask and SQLAlchemy. This project demonstrates a professional deployment setup using Gunicorn and is designed to be easily deployed on platforms like Render or Railway.

## 🚀 Live Demo

Check out the live application here: **[https://url-trim.onrender.com/](https://url-trim.onrender.com/)**

## ✨ Features

-   **Shorten URLs**: Paste any long URL and get a short, shareable link.
-   **Instant Redirect**: Short links redirect users to the original long URL.
-   **Click Tracking**: Keeps a count of how many times each short link has been clicked.
-   **Duplicate Prevention**: If a URL has already been shortened, it returns the existing short link.
-   **Modular Structure**: The application is organized into separate components for scalability and maintainability.
-   **Production Ready**: Configured with Gunicorn for a robust production environment.

## 🛠️ Tech Stack

-   **Backend**: [Python](https://www.python.org/) with [Flask](https://flask.palletsprojects.com/)
-   **Database**: [SQLite](https://www.sqlite.org/) with [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) ORM
-   **Deployment**: [Render](https://render.com/)
-   **WSGI Server**: [Gunicorn](https://gunicorn.org/)

## 📁 Project Structure

The project follows a modular structure to keep the code organized and scalable.

```
url-shortener-flask/
├── app/
│   ├── __init__.py      # Application factory and configuration
│   ├── models.py        # Database model definitions
│   ├── routes.py        # Application routes and logic
│   └── templates/
│       └── index.html   # Main HTML template
├── run.py               # Entry point to run the application
├── Procfile             # Instructions for deployment (Render/Railway)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 🚀 Local Setup

To run this project on your local machine, follow these steps.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```
*(Remember to replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub details.)*

### 2. Set Up a Virtual Environment

It's highly recommended to use a virtual environment.

```bash
# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required Python packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

Create the SQLite database file and the necessary tables.

```bash
python
```

Then, in the Python shell:

```python
>>> from run import app
>>> from app import db
>>> with app.app_context():
...     db.create_all()
...
>>> exit()
```

### 5. Run the Application

Start the local development server.

```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000`.

## 🌐 Deployment

This project is configured for easy deployment on services like Render or Railway.

1.  **Connect to GitHub**: Push your code to a GitHub repository.
2.  **New Project**: In your deployment provider's dashboard, create a new project and deploy from your GitHub repo.
3.  **Automatic Deploy**: The service will automatically detect the Python project, install dependencies from `requirements.txt`, and use the `Procfile` to start the application with Gunicorn.

The `Procfile` handles both database creation and starting the server:

```
web: gunicorn run:app
beforeCommand: python -c "from app import db, create_app; app = create_app(); app.app_context().push(); db.create_all()"
```

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### What I Changed:

1.  **Live Demo Link:** I replaced the placeholder with your actual URL: `https://url-trim.onrender.com/`.
2.  **Deployment Platform:** I updated the "Tech Stack" and "Deployment" sections to mention Render, since that's where your app is hosted.
3.  **Clone URL:** I put a placeholder in the "Clone the Repository" section. You should update this with your actual GitHub repository link so others can easily clone your project.

Your project now has a fantastic, professional-looking `README.md` file. Great job
