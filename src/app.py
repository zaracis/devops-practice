from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>✅ CI/CD работает!</h1><p>Deployed via GitHub Actions + Ansible</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)