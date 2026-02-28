# FastAPI-Guard 🛡️

A lightweight security middleware for FastAPI applications to detect and prevent common **SQL Injection** and **XSS** attacks.

## Installation

```bash
pip install fastapi-guard
Usage
Here is a simple example of how to use FastAPI-Guard in your FastAPI application
from fastapi import FastAPI
from fastapi_guard import SecurityGuard

app = FastAPI()

# Add the security middleware to check all requests
app.add_middleware(SecurityGuard)

@app.get("/")
def read_root():
    return {"Hello": "World"}
Features
SQL Injection Detection: Identifies potentially malicious SQL patterns in request bodies and URLs.
XSS Protection: Identifies malicious scripts and script tags.
Easy Integration: Simply add the middleware to your FastAPI app.
License
This project is licensed under the MIT License - see the LICENSE file for details
