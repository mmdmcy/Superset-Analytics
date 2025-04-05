FROM apache/superset:latest

USER root

# Install any additional dependencies here
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && apt-get clean

USER superset

# Copy the superset_config.py file into the container
COPY superset_config.py /app/pythonpath/superset_config.py

# Expose the port for Superset
EXPOSE 8088

# Start Superset
CMD ["superset", "run", "-h", "0.0.0.0", "-p", "8088"]