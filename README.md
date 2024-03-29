### If you're creating a new repository:

1. Create a new repository on GitHub.

2. Open a terminal and navigate to your project directory.

3. Initialize a new Git repository:

   ```bash
   git init
   ```
4. Create a README file:

    ```bash
   echo "your-repo" >> README.md # replace "your-repo" with your desired name
    ```

5. Add the README file to the staging area
    ```bash
    git add README.md
    ```

6. Commit the changes:
    ```bash
   git commit -m "first commit"
    ```

7. Set the branch to main:
    ```bash
   git branch -M main
    ```

8. Add the remote repository:
    ```bash
   git remote add origin https://github.com/your-username/your-repo.git # Replace "your-username" with your actual username.
    ```

9. Push the changes to GitHub:
    ```bash
   git push -u origin main
    ```

### If you want to work on an existing repository:

1. Clone the repository:
    ```bash
   git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the cloned repository:
    ```bash
   cd your-repo
    ```

3. Set the branch to main (if not already set):
    ```bash
   git branch -M main
    ```

4. Add the remote repository (if not already added):
    ```bash
   git remote add origin https://github.com/your-username/your-repo.git
    ```

5. Push changes to the repository:
    ```bash
   git push -u origin main
    ```

# cb_sport Project

#### short-description:

Sport blog where you can pick or demand a product/accesory!
We will contact ```YOU```!

#### interact with it:

### Prerequisites

Make sure you have the following installed on your machine:

- Python (3.11 recommended)
- Pip (Python package installer) (23.3.2 recommended)
- Virtualenv (optional but recommended for isolating dependencies)

1. Navigate to the project directory:
    ```bash
   cd your-repo
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
   python -m venv venv
    ```

3. Activate the virtual environment:
    ```bash
   .\venv\Scripts\activate #Windows
   source venv/bin/activate #macOS/Linux
    ```

4. Install project dependencies:
    ```bash
   pip install -r requirements.txt
    ```

5. Create project folder:
    ```bash
   django-admin startproject "your-project-name"
    ```

6. Create application:
    ```bash
   python manage.py startapp "your-application-name"
    ```

7. Apply migrations:
    ```bash
   python manage.py makemigrations
   python manage.py migrate
    ```
8. Create a superuser (for Django Admin):
    ```bash
   python manage.py createsuperuser
    ```
9. Run the development server:
    ```bash
   python manage.py runserver
    ```

#### Replace placeholders like "your-project-name", "your-username", "your-repo", "your-application-name", etc., with your actual project information.

Access the application at http://127.0.0.1:8000/