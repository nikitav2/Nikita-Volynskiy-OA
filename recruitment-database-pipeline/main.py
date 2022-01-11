from os import major
from flask.sessions import NullSession
import pymysql
from app import app
from config import mysql
from flask import json, jsonify
from flask import flash, request