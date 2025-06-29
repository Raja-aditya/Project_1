from flask import Flask, request, jsonify
import json
import uuid
from datetime import datetime
from utils import load_events, save_events, sort_events
from reminder import start_reminder_thread

app = Flask(__name__)
DATA_FILE = 'events.json'

@app.route('/events', methods=['GET'])
def get_events():
    events = load_events(DATA_FILE)
    return jsonify(sort_events(events))

@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    data['id'] = str(uuid.uuid4())
    events = load_events(DATA_FILE)
    events.append(data)
    save_events(DATA_FILE, events)
    return jsonify({"msg": "Event created", "event": data}), 201

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    events = load_events(DATA_FILE)
    for event in events:
        if event['id'] == event_id:
            event.update(data)
            save_events(DATA_FILE, events)
            return jsonify({"msg": "Event updated", "event": event})
    return jsonify({"error": "Event not found"}), 404

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_events(DATA_FILE)
    events = [e for e in events if e['id'] != event_id]
    save_events(DATA_FILE, events)
    return jsonify({"msg": "Event deleted"})

if __name__ == '__main__':
    start_reminder_thread(DATA_FILE)
    app.run(debug=True)
