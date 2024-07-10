#!/usr/bin/python3
"""flask clone"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status():
    """route status"""
    return jsonify({
        "status": "OK"
        })
