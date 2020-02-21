from flask import Flask

application = Flask(__name__)

from Sipher import routes

if __name__ == "__main__":
  application.run()
