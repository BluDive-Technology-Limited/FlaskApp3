from flask import Flask, request, render_template
import logging
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Set up logging
logging.basicConfig(filename='logs/access.log', level=logging.INFO)

@app.route('/')
def home():
    user_ip = request.remote_addr
    logging.info(f"Access from: {user_ip}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
