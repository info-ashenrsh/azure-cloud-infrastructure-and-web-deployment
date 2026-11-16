import logging
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from werkzeug.exceptions import HTTPException

from config import Config
from models import Task, db

load_dotenv()

def create_app(test_config=None):
    app = Flask(
        __name__,
        template_folder="../frontend",
        static_folder="../frontend",
        static_url_path="/static",
    )
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/api/tasks")
    def list_tasks():
        tasks = Task.query.order_by(Task.id.desc()).all()
        return jsonify([task.to_dict() for task in tasks])

    @app.post("/api/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        title = str(data.get("title", "")).strip()
        description = str(data.get("description", "")).strip()

        if not title:
            return jsonify({"error": "A task title is required."}), 400
        if len(title) > 160:
            return jsonify({"error": "Title must be 160 characters or fewer."}), 400

        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        app.logger.info("Task created: id=%s", task.id)
        return jsonify(task.to_dict()), 201

    @app.patch("/api/tasks/<int:task_id>")
    def update_task(task_id):
        task = db.session.get(Task, task_id)
        if task is None:
            return jsonify({"error": "Task not found."}), 404

        data = request.get_json(silent=True) or {}
        if "title" in data:
            title = str(data["title"]).strip()
            if not title or len(title) > 160:
                return jsonify({"error": "Title must be 1 to 160 characters."}), 400
            task.title = title
        if "description" in data:
            task.description = str(data["description"]).strip()
        if "status" in data:
            if data["status"] not in {"Pending", "In Progress", "Completed"}:
                return jsonify({"error": "Invalid status."}), 400
            task.status = data["status"]

        db.session.commit()
        return jsonify(task.to_dict())

    @app.delete("/api/tasks/<int:task_id>")
    def delete_task(task_id):
        task = db.session.get(Task, task_id)
        if task is None:
            return jsonify({"error": "Task not found."}), 404
        db.session.delete(task)
        db.session.commit()
        app.logger.info("Task deleted: id=%s", task_id)
        return "", 204

    @app.errorhandler(Exception)
    def handle_exception(error):
        if isinstance(error, HTTPException):
            return jsonify({"error": error.description}), error.code
        app.logger.exception("Unhandled application error")
        return jsonify({"error": "Internal server error."}), 500

    return app

app = create_app()
