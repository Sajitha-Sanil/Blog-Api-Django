# Django Blog API

## Overview

This project is a RESTful API for a blog platform built using Django and Django REST Framework. It supports features like user creation, blog posts with titles, text, images, pagination, and hashtag search.

## Features

- User Login and Token Refresh
- Create, Read, Update, and Delete (CRUD) operations for blog posts
- Pagination for blog posts
- Upload and manage images for blog posts
- Search blog posts by hashtag

## Technologies Used

- Django
- Django REST Framework
- SQLite (default, can be configured to use PostgreSQL or other databases)
- JWT (JSON Web Token) for authentication
- Pillow for image handling

## Installation

- Install dependencies: pip install -r requirements.txt
- Set up Django environment variables and database configurations.
- Run migrations: python manage.py migrate
- Create a superuser: python manage.py createsuperuser
- Start the development server: python manage.py runserver

## Api Endpoints

- User Login:

  POST /login/
  {
    "username": "exampleuser",
    "password": "examplepassword"
  }
- Token Refresh:

  POST /refresh-token/
  {
    "refresh": "your_refresh_token"
  }
- Create a new blog post:

  POST /blog/create/
  {
    "title": "Sample Title",
    "text": "Sample text content",
    "image": "path/to/image.jpg"
  }
- List all blog posts (with pagination):

  GET /blog/
- Retrieve a single blog post:

  GET /blog/{slug}/
- Update or delete a blog post:

  PUT /blog_edit/{slug}/
  {
    "title": "Updated Title",
    "text": "Updated text content",
    "image": "path/to/new-image.jpg"
  }
  DELETE /blog_edit/{slug}/
- Search blog posts by hashtag:

  GET /blog/hashtag/{hashtag}/



