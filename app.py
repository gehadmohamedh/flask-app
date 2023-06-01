from flask import Flask, request
from app_service import AppService
import json
import os 

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello Here is Gehad From her laptop to jenkins then to pod in gke cluster ISA :3"


@app.route('/api/tasks')
def tasks():
    return appService.get_tasks()

@app.route('/api/task', methods=['POST'])
def create_task():
    request_data = request.get_json()
    task = request_data['task']
    return appService.create_task(task)


@app.route('/api/task', methods=['PUT'])
def update_task():
    request_data = request.get_json()
    return appService.update_task(request_data['task'])


@app.route('/api/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    return appService.delete_task(id)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
