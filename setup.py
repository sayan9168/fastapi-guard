from setuptools import setup, find_packages

setup(
    name="fastapi-guard",
    version="1.0.0",
    author="Your Name",
    description="A simple security middleware for FastAPI to prevent SQL injection and XSS.",
    packages=find_packages(),
    install_requires=[
        "fastapi",
    ],
)
