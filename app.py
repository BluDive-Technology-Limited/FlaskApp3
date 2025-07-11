from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='access.log', level=logging.INFO)

@app.route('/')
def log_access():
    user_ip = request.remote_addr
    logging.info(f"Access from: {user_ip}")
    return f"Your IP {user_ip} has been logged just now."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
