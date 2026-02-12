from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on Vercel 🚀"

# Required for Vercel
def handler(request):
    return app(request.environ, start_response)
