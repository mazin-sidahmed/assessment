import sys, os
from flask import Flask

root = os.path.normpath(os.getcwd())

if root not in sys.path:
    sys.path.append(root)

from src.api.koncept import koncept


app = Flask(__name__)
app.register_blueprint(koncept)

if __name__ == "__main__":
    app.run()
