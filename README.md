# Flask Notes Application

This is a simple Flask-based notes application that allows users to create, read, update, and delete notes. The app uses SQLite3 as the database and implements basic CRUD operations for managing notes.

## Features

- **Create**: Add new notes to the application.
- **Read**: View all the saved notes.
- **Update**: Edit existing notes.
- **Delete**: Remove notes from the application.
  
## Tech Stack

- **Backend**: Flask
- **Database**: SQLite3
- **Containerization**: Docker
- **Deployment**: Docker on a Virtual Machine (VM)

## Getting Started

### Prerequisites

Before running this application, make sure you have the following installed on your local machine:

- Docker
- Python 3.x
- SQLite3

### Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/flask-notes-app.git
   cd flask-notes-app
   ```
2. **Create the docker image**
   ```bash
    docker build -t flask-notes-app .
   ```
3. **Running the container**
   ```bash
    docker run -d -p 5000:5000 flask-notes-app
   ```
4. **Verify the application**
    To verify that the application is running inside the Docker container, visit  on your browser
   ```
   http://localhost:5000
   ```

   
