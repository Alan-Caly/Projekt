# File to initialize Flask application
# This file should not be changed

# <import modules from flask>
from flask import Flask, session

# Flask initialization
app = Flask(__name__,
            template_folder='template',
            static_folder='static')

############################################################
# <initialize session>
from server.src.server.ServerSession import Session
serverSession = Session()

# <import route modules>
import server.route.IndexController
import server.route.LoginController
import server.route.RegisterController
