"""
Starter code for Building REST APIs with FastAPI assignment.
Complete the tasks by implementing the required endpoints and functionality.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI()

# TODO: Task 1 - Create a basic FastAPI application
# 1. Create a GET endpoint at "/" that returns a welcome message
# 2. Create a GET endpoint at "/api/greet/{name}" that accepts a name parameter
#    and returns a personalized greeting

# TODO: Task 2 - Implement CRUD operations
# 1. Define a Pydantic model for your data (Item, Task, Product, etc.)
# Example:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float

# 2. Create a storage structure (e.g., items_db = [])
# 3. Implement POST endpoint to create a new item
# 4. Implement GET endpoint to retrieve all items
# 5. Implement GET endpoint to retrieve a specific item by ID
# 6. Implement PUT endpoint to update an item
# 7. Implement DELETE endpoint to remove an item

# TODO: Task 3 - Add validation and error handling
# 1. Use Pydantic models to validate incoming data
# 2. Return appropriate HTTP status codes:
#    - 200: Success
#    - 201: Created
#    - 400: Bad Request
#    - 404: Not Found
# 3. Raise HTTPException with descriptive error messages


if __name__ == "__main__":
    import uvicorn
    
    # Run the application with: python starter-code.py
    # Or use: uvicorn starter-code:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
