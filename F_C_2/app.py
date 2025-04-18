from flask import Flask,request, jsonify
from pizza_class import FoodClassification
import os

app = Flask(__name__)