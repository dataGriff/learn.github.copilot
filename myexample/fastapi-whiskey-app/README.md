# FastAPI Whiskey App

This project is a FastAPI application for managing an inventory of distilleries and whiskies. It provides a RESTful API to perform CRUD operations on distilleries and whiskies.

## Project Structure

```
fastapi-whiskey-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── distilleries.py
│   │   └── whiskies.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── distillery.py
│   │   └── whisky.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── distillery.py
│   │   └── whisky.py
│   └── database.py
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-whiskey-app
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application, execute the following command:

```
uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`.

## API Endpoints

- **Distilleries**
  - `GET /distilleries`: List all distilleries
  - `POST /distilleries`: Create a new distillery
  - `GET /distilleries/{distillery_id}`: Get a distillery by ID

- **Whiskies**
  - `GET /whiskies`: List all whiskies
  - `POST /whiskies`: Create a new whisky
  - `GET /whiskies/{whisky_id}`: Get a whisky by ID

## Database Migrations

This project uses Alembic for database migrations. To run migrations, use the following command:

```
alembic upgrade head
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.