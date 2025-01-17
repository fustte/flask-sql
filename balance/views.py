from . import app

@app.route('/')
def home():
    return 'Hello, balance'