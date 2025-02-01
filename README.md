# Social Media Project

This is a Django-based social media application that allows users to create posts, follow other users, and comment on posts. The application supports user authentication, including social authentication via Google.

## Features

- User registration and authentication
- Social authentication with Google
- Create, edit, and delete posts
- Follow and unfollow users
- Comment on posts
- User profile management

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/social_media.git
    cd social_media
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the project root and add the following variables:
    ```env
    SECRET_KEY=your_secret_key
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Register a new user or log in with an existing account
- Create posts, follow other users, and comment on posts
- Manage your profile and view other users' profiles

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

