from flask import Blueprint, render_template

planner_bp = Blueprint("planner", __name__)

@planner_bp.route("/")
def home():
    return render_template("index.html")

@planner_bp.route("/create-plan")
def create_plan():
    return render_template("input_plan.html")
