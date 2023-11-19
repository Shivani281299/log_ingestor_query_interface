# log_ingestor_query_interface
This project is a log ingestor system and query interface designed to efficiently handle vast volumes of log data. It provides a simple interface for querying data using full-text search and specific field filters.

# Log Ingestor and Query Interface

## Features

### Log Ingestor

The Log Ingestor is responsible for ingesting log data in the provided JSON format and ensuring scalability and efficiency.

#### Mechanism to Ingest Logs

The log ingestor uses an HTTP server to accept logs in the provided JSON format. The server is configured to run on port `3000` by default. Logs are ingested using HTTP POST requests.

### Log Ingestor

- **Mechanism to Ingest Logs:** Accepts logs in JSON format via HTTP POST requests on port `3000`.
- **Scalable Architecture:** Utilizes asynchronous processing, parallelism, and load balancing for efficient log handling.
- **Bottleneck Mitigation:** Optimizes I/O operations and database write speeds to prevent bottlenecks.

### Query Interface

- **User Interface:** Provides a user-friendly Web UI for interactive log querying.
- **Filters:** Supports filtering based on log level, message, resource ID, timestamp, trace ID, span ID, commit, and metadata.parent Resource ID.
- **Efficient Search Results:** Ensures quick and efficient search results.

### ingestion of data to the log_ingestor

- ** here i inserted data using curl in powershell or any cmd terminal

- ********************************************************************************************************************************
-  Invoke-WebRequest -Uri http://localhost:3000/ingest -Method POST -Headers @{"Content-Type"="application/json"} -Body '{
>>   "level": "error",
>>   "message": "Failed to connect to DB",
>>   "resourceId": "server-1234",
>>   "timestamp": "2023-09-15T08:00:00Z",
>>   "traceId": "abc-xyz-123",
>>   "spanId": "span-456",
>>   "commit": "5e5342f",
>>   "metadata": {
>>     "parentResourceId": "server-0987"
>>   }
>> }' -UseBasicParsing
>>**********************************************************************************************************************************
-**invoking the info we can add data to the log_ingest

### Advanced Features

- **Search Within Date Ranges:** Filters logs between specified timestamp ranges.
- **Regular Expression Search:** Enables the use of regular expressions for searching.
- **Combining Multiple Filters:** Allows users to combine multiple filters for precise queries.
- **Real-time Log Ingestion and Search:** Provides real-time capabilities for log ingestion and searching.
- **Role-Based Access:** Implements role-based access control to the query interface.

- >> ### these are the addition search which we can search in the log query interface
  >> ### i have also provided the images of the output with differnt kind of filters provided 

  ## Sample Queries

Execute these sample queries for validation:

- Find all logs with the level set to "error."
- Search for logs with the message containing the term "Failed to connect."
- Retrieve all logs related to resource ID "server-1234."
-  Filter logs between the timestamp

## Getting Started

Follow these steps to set up and run the log ingestor and query interface locally
and u will get the output where localhost running in both port:3000 and port:5000


