# Use a lightweight Python base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install Apache Spark
RUN apt-get update && apt-get install -y default-jdk
RUN wget -q https://archive.apache.org/dist/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz
RUN tar xf spark-2.4.7-bin-hadoop2.7.tgz
RUN mv spark-2.4.7-bin-hadoop2.7 /usr/local/spark
ENV SPARK_HOME /usr/local/spark

# Add Spark bin directory to PATH
ENV PATH $PATH:$SPARK_HOME/bin

# Copy the Python script into the container
COPY preprocess_data.py .

# Run the Python script when the container launches
CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.7", "preprocess_data.py"]
