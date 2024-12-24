# Blog App with Django

Welcome to the Blog App project! This is a simple but fully functional blog application built using Django, the popular web framework for Python. It allows users to create, edit, delete, and read blog posts. The app also includes user authentication features such as sign-up, login, and logout, as well as other useful functionalities like categories and tags for organizing posts.

## Features

- **Blog Posts**: Create, read, update, and delete blog posts.
- **Categories**: Assign posts to different categories for better organization.
- **Tags**: Add tags to posts to make them easily searchable.
- **Post Pagination**: Supports paginated list of posts on the homepage.
- **Comments**: Users can leave comments on posts (optional).
- **Share Posts**: Users can share posts by email
- **Search**: A basic search functionality to find posts by title or content.

## Technologies Used

- **Django**: A high-level Python web framework that simplifies the process of building web applications.
- **SQLite**: The default database used by Django for this project. You can configure a different database such as PostgreSQL or MySQL if desired.
- **PostgreSQL**: 
- **Docker**: 
- **HTML and CSS**: For structuring and styling of page
- **Python**: The programming language used for the server-side logic.

---

## Setup Instructions

### Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.x**: The application is built using Python 3.
- **pip**: Python's package installer for managing dependencies.
- **Django**: The web framework used to develop this application.

### Installation

Follow these steps to get the project up and running on your local machine:

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/yourusername/blog-app.git](https://github.com/Kujt/blog.git)
   cd blog
   ```

2. ** Create a virtual environment**

It's a good practice to create a virtual environment for your project to isolate dependencies.

```bash
python -m venv venv
```
Once the virtual environment is created, activate it using the following commands:
  On Windows:
  ```bash
venv\Scripts\activate
```
On MacOS/Linux:
  ```bash
source venv/bin/activate
```
Apply database migrations
  ```bash
python manage.py migrate
`````
3. ** Create a superuser (optional) **
   To access the Django admin panel and manage your blog content, you can create an admin user (superuser). Run the following command and follow the prompts to set up your superuser credentials:
```bash
python manage.py createsuperuser
```
4. ** Run the development server**
   After setting up your environment and applying migrations, you can run the development server with the following command:
```bash
python manage.py runserver
```   
This will start the server at http://127.0.0.1:8000/, where you can view the blog.

5. **Access the app**
Homepage: Open your web browser and go to http://127.0.0.1:8000/ to view the blog posts.
Admin Panel: The admin panel is available at http://127.0.0.1:8000/admin/. You can log in using the superuser credentials you created.
