# Use a secure, minimal base image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Install system build tools required for Python packages (like Flask)
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy only requirements first for better caching
COPY requirements.txt .

# Upgrade pip, setuptools and install project dependencies
RUN pip install --upgrade pip setuptools && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose the application port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
