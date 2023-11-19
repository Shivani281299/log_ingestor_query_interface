from codecs import escape_decode
from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = 'logs.db'

def execute_query(query, params=()):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_logs():
    query = 'SELECT * FROM logs WHERE 1=1'
    params = []

    for field in ('level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit_hash', 'parentResourceId'):
        value = request.form.get(field)
        if value:
            query += f' AND {field} = ?'
            params.append(value)

    results = execute_query(query, params)
    return render_template('result.html', results=results)

@app.route('/query', methods=['GET', 'POST'])
def query_logs():
    if request.method == 'POST':
        query = request.form.get('query', '')
        start_time_str = request.form.get('start_time', '')
        end_time_str = request.form.get('end_time', '')

        index_name = 'logs'

        if start_time_str and end_time_str:
            start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%SZ')
            end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M:%SZ')

            # Add range filter to the query
            timestamp_range_filter = {
                'range': {
                    'timestamp': {
                        'gte': start_time,
                        'lte': end_time,
                    }
                }
            }

            # Combine the range filter with the original query
            query = {'bool': {'must': [{'query_string': {'query': query}}, timestamp_range_filter]}}

        else:
            query = {'query_string': {'query': query}}

        results = escape_decode.search(index=index_name, body={'query': query})
        hits = results['hits']['hits']

        return render_template('query.html', hits=hits)

    return render_template('query.html', hits=[])

if __name__ == '__main__':
    app.run(port=5000)

