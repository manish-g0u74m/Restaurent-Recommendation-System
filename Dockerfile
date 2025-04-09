FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create the SQLite database directory
RUN mkdir -p instance

# Import data and initialize the database
RUN python import_data.py

EXPOSE 5000

CMD ["python", "run.py"] 