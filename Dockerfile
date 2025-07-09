# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Run Django app using gunicorn from root
CMD ["gunicorn", "sanctity_comments.wsgi:application", "--chdir", "sanctity_comments", "--bind", "0.0.0.0:8000"]
