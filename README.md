
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

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PeymanNr/MailQueueService
   cd AsyncMailer
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file with your configuration:
   ```bash
   DEBUG= True or false
   DB_NAME= your_db_name
   DB_USER= your_db_user
   DB_PASSWORD= your_db_password
   DB_HOST= your_db_host
   DB_PORT=your_db_port
   SECRET_KEY= your_django_secret_key
   RABBITMQ_USER= your_rabbitmq_user
   RABBITMQ_PASSWORD= your_rabbitmq_password
   RABBITMQ_PORT= your_rabbitmq_port
   RABBITMQ_HOST= your_rabbitmq_host
   CELERY_BROKER_URL= pyamqp://your_broker_user:your_broker_password@your_broker_host:5672//
   CELERY_RESULT_BACKEND=rpc://
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_email_password
   ```

5. Apply the database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start RabbitMQ and Celery worker:
   ```bash
   # Ensure RabbitMQ is running
   sudo service rabbitmq-server start

   # Start Celery worker
   celery -A config worker --loglevel=info
   ```

7. Start the Django server:
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

