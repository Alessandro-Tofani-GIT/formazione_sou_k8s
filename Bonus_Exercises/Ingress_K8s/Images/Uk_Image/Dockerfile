# Step 1: Use the official Python base image
FROM python:3.13-slim


# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the requirements.txt file (which includes Flask) into the container
COPY requirments.txt /app/

# Step 5: Install Python dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirments.txt

# Step 6: Copy the rest of the application code into the container
COPY . /app/

# Step 7: Expose the port that the Flask app will run on (default Flask port is 5000)
EXPOSE 5000

# Step 8: Set the default command to run the Flask app
CMD ["python", "app.py"]
