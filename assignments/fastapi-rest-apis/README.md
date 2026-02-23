# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, high-performance REST APIs using the FastAPI framework. You'll create API endpoints to handle HTTP requests and responses while applying best practices for API design and validation.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with basic endpoints that handle different HTTP methods.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application
- Create a GET endpoint that returns a welcome message (e.g., `/` or `/api/welcome`)
- Create a GET endpoint that accepts a path parameter (e.g., `/api/greet/{name}`)
- Run the application using `uvicorn` and test endpoints in a browser or with curl
- Example output:
  ```
  GET /api/welcome → {"message": "Welcome to the API"}
  GET /api/greet/Alice → {"greeting": "Hello, Alice!"}
  ```


### 🛠️ Implement CRUD Operations with Data Models

#### Description
Build endpoints that perform Create, Read, Update, and Delete operations on a simple data model.

#### Requirements
Completed program should:

- Define a Pydantic model for your data (e.g., `Item`, `Task`, `Product`)
- Create POST endpoint to add new items
- Create GET endpoint to retrieve all items or a specific item by ID
- Create PUT endpoint to update an existing item
- Create DELETE endpoint to remove an item
- Store data in memory (using a list or dictionary) for this assignment


### 🛠️ Add Request Validation and Error Handling

#### Description
Enhance your API with proper input validation and meaningful error responses.

#### Requirements
Completed program should:

- Use Pydantic models to validate request data with data types and constraints
- Return appropriate HTTP status codes (200, 201, 400, 404, 500)
- Provide descriptive error messages for invalid requests
- Test with invalid inputs and verify error responses are helpful
- Example: Attempting to delete a non-existent item returns 404 with an error message
