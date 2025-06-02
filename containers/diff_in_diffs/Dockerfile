# Use a suitable Python base image
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy packaging and requirements files
COPY requirements.txt .
COPY pyproject.toml .
COPY setup.cfg .

# Copy the source code for the package
COPY src ./src

# Copy the main script
COPY main.py .

# Install the package and its dependencies
# Using -e . installs the package in editable mode from the current directory.
# This will use setup.cfg and pyproject.toml to build and install the 'did_tool' package
# and its dependencies (pandas, statsmodels).
RUN pip install --no-cache-dir -e .

# Set the command to run the application
# main.py is in /app and uses the installed did_tool package
CMD [ "python", "-m", "main"]
