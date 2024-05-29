# Hotel Reservation System

A Django-based hotel reservation system that allows users to book rooms, manage hotels, and handle reservations. This project provides a REST API for interacting with the system.

## Features

- Manage hotels and rooms.
- Create and manage reservations.
- Ensure no overlapping reservations for the same room.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/hotel_reservation.git
    cd hotel_reservation
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser to access the admin interface:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the API at `http://127.0.0.1:8000/api/` and the admin interface at `http://127.0.0.1:8000/admin/`.

## API Endpoints

The following endpoints are available:

- `/api/hotels/` - List and create hotels.
- `/api/rooms/` - List and create rooms.
- `/api/reservations/` - List and create reservations.

## Running Tests

To run the tests for this project, use the following command:

```bash
python manage.py test
