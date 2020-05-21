from flask import Flask

app = FLask(__name__)

@aap.route('/')
def index():
    return "Hello World"

if __name__ == "main":
    app.run(debug=True)