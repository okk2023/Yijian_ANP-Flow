from flask import Flask, render_template, request, jsonify, Blueprint
import sys
sys.path.append('./backend')
from params import *
import subprocess

blueprint = Blueprint('compilation', __name__)

@blueprint.route('/')
def compilation_homepage():
    return render_template('compilation.html')

# To be developed ...
