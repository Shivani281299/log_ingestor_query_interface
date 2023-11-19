from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'logs.db'

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level TEXT,
            message TEXT,
            resourceId TEXT,
            timestamp TEXT,
            traceId TEXT,
            spanId TEXT,
            commit_hash TEXT,  -- Changed from "commit" to "commit_hash"
            parentResourceId TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return "Welcome to the Log Ingestor! Use the /ingest endpoint to send logs."

@app.route('/ingest', methods=['POST'])
def ingest_log():
    log_data = request.json
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (
            level, message, resourceId, timestamp, traceId, spanId, commit_hash, parentResourceId
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        log_data['level'],
        log_data['message'],
        log_data['resourceId'],
        log_data['timestamp'],
        log_data['traceId'],
        log_data['spanId'],
        log_data['commit'],
        log_data['metadata']['parentResourceId'] if 'metadata' in log_data else None
    ))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/favicon.ico')
def favicon():
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    create_table()
    app.run(port=3000)

