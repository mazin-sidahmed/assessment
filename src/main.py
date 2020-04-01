import sys, os
from flask import Flask


root = os.path.normpath(os.getcwd())

if root not in sys.path:
    sys.path.append(root)

from src.api.koncept import koncept
from src.api.new_company import new_company


app = Flask(__name__)
app.register_blueprint(koncept)
app.register_blueprint(new_company)

if __name__ == "__main__":
    app.run()
