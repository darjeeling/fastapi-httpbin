# fastapi-httpbin

A simple httpbin-like HTTP testing service built with FastAPI. This lightweight service provides essential endpoints for testing HTTP requests and responses.

## Features

- Built with FastAPI for high performance
- Minimal dependencies
- Docker support with port 80
- Easy to deploy and use

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) for dependency management

## Local Development

### 1. Create virtual environment with uv

```bash
uv venv --python 3.13
```

### 2. Activate the virtual environment

```bash
# On macOS/Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
uv pip install -e .
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

## Docker

### Build the Docker image

```bash
docker build -t fastapi-httpbin .
```

### Run the container

```bash
docker run -p 80:80 fastapi-httpbin
```

The application will be available at `http://localhost`

## API Endpoints

### `GET /`
Welcome endpoint with available endpoints information.

**Example:**
```bash
curl http://localhost:8000/
```

### `GET /get`
Returns GET request data including query parameters, headers, origin IP, and URL.

**Example:**
```bash
curl "http://localhost:8000/get?param1=value1&param2=value2"
```

### `POST /post`
Returns POST request data including body, form data, JSON, headers, origin IP, and URL.

**Example:**
```bash
curl -X POST http://localhost:8000/post \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### `GET /headers`
Returns all request headers.

**Example:**
```bash
curl http://localhost:8000/headers
```

### `GET /ip`
Returns the client's IP address.

**Example:**
```bash
curl http://localhost:8000/ip
```

### `GET /user-agent`
Returns the User-Agent header.

**Example:**
```bash
curl http://localhost:8000/user-agent
```

## Interactive API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## License

MIT
