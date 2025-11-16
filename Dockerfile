FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements separately for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Run the app
CMD ["python", "src/main.py"]
