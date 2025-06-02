#!/bin/bash

echo "Activating virtual environment..."
source venv/bin/activate

echo "Starting MongoDB service..."
sudo systemctl start mongod

echo "Running Django development server..."
python manage.py runserver

echo "Development server started. Press Ctrl+C to stop."

# Optionally, go back to the project root after stopping the server
# echo "Returning to project root..."
# cd ..
