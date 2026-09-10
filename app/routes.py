from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "devops-flask-api"
    }), 200


@api.get("/api/status")
def status():
    return jsonify({
        "service": "devops-flask-api",
        "status": "running"
    }), 200


@api.get("/api/info")
def info():
    return jsonify({
        "application": "DevOps Flask API",
        "version": "1.0.0",
        "environment": "production"
    }), 200