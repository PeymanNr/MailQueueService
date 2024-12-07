
# AsyncMailer Project

This project is a Django-based asynchronous email sending application using Celery and RabbitMQ. 
It provides scalable email processing and supports attachments and multiple recipients.

## Features

- **Django Backend**: Handles email management and processing.
- **Celery Integration**: Manages asynchronous tasks.
- **RabbitMQ Broker**: Facilitates message passing between Django and Celery.
- **PostgreSQL Database**: Stores email metadata.
- **SMTP Configuration**: Sends emails via an external mail server.

## Requirements

- Python 3.x
- Django
- Celery
- RabbitMQ
- PostgreSQL
- Docker
- Docker Compose

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PeymanNr/MailQueueService
   cd AsyncMailer
   ```

2. **Docker Setup**:

   If you want to run the application using Docker, follow the steps below:

   - **Build the Docker images**:
     ```bash
     docker-compose build
     ```

   - **Start the services**:
     ```bash
     docker-compose up
     ```

   This will start the following services:
   - `django_app`: Django application running on port 8000.
   - `postgres_db`: PostgreSQL database running on port 5431.
   - `rabbitmq`: RabbitMQ message broker running on port 5673.
   - `celery_worker`: Celery worker for processing email tasks.

   By default, Docker will set up a PostgreSQL database and RabbitMQ instance, as well as run the Django app and Celery worker.

3. Set up the `.env` file with your configuration:

   - Copy `.env.sample` to `.env`:
     ```bash
     cp .env.sample .env
     ```

   - Edit the `.env` file with your credentials:
     ```bash
     DEBUG=True or False
     DB_NAME=your_db_name
     DB_USER=your_db_user
     DB_PASSWORD=your_db_password
     DB_HOST=postgres_db
     DB_PORT=5432
     SECRET_KEY=your_django_secret_key
     RABBITMQ_USER=your_rabbitmq_user
     RABBITMQ_PASSWORD=your_rabbitmq_password
     RABBITMQ_PORT=5672
     RABBITMQ_HOST=rabbitmq
     CELERY_BROKER_URL=pyamqp://your_broker_user:your_broker_password@rabbitmq:5672//
     CELERY_RESULT_BACKEND=rpc://
     EMAIL_HOST_USER=your_email@example.com
     EMAIL_HOST_PASSWORD=your_email_password
     ```

4. **Apply the database migrations**:

   If you're running the project without Docker, apply the database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

   **Note**: If you're using Docker, the migrations will be applied automatically when the Django container starts.

5. **Start RabbitMQ and Celery worker** (if not using Docker):

   - Ensure RabbitMQ is running:
     ```bash
     sudo service rabbitmq-server start
     ```

   - Start Celery worker:
     ```bash
     celery -A config worker --loglevel=info
     ```

6. Start the Django server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the web application:
   ```
   http://localhost:8000
   ```

2. Use the interface or API to send emails. Celery will process them asynchronously.

## Environment Variables

- **DEBUG**: Django debug mode.
- **DB_NAME, DB_USER, DB_PASSWORD**: PostgreSQL database credentials.
- **RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_HOST**: RabbitMQ configuration.
- **CELERY_BROKER_URL, CELERY_RESULT_BACKEND**: Celery broker and result backend settings.
- **EMAIL_HOST_USER, EMAIL_HOST_PASSWORD**: SMTP email server credentials.