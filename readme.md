# Blog API

A RESTful API for blog management built with FastAPI.

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Starting the Server

To start the development server, run:

```bash
fastapi dev main.py
```

This command starts the FastAPI application with hot-reloading enabled for development.

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These documentation interfaces allow you to:

- View all available endpoints
- Test API requests directly from the browser
- See request/response schemas
- Understand authentication requirements (if any)

## Project Structure

```
blog-api/
├── app/
│   └── main.py
├── routes/
│   └── blog_route.py
└── requirements.txt
```

## License

[MIT](LICENSE)
