import time
import os
from flask import Blueprint, render_template, request

from models import db
from models.building_plan import BuildingPlan
from models.room import Room
from models.cost_estimation import CostEstimation

from utils.plan_generator import generate_plan
from utils.cost_calculator import calculate_cost
from utils.plan_drawer import draw_floor_plan
from utils.pdf_generator import generate_pdf


planner_bp = Blueprint("planner", __name__)


@planner_bp.route("/")
def home():
    return render_template("index.html")


@planner_bp.route("/create-plan", methods=["GET", "POST"])
def create_plan():
    if request.method == "POST":

        #  GET FORM DATA
        length = float(request.form["length"])
        width = float(request.form["width"])
        floors = int(request.form["floors"])
        bedrooms = int(request.form["bedrooms"])
        budget = float(request.form["budget"])

        #  PLAN & COST LOGIC
        total_area, rooms_data = generate_plan(length, width, floors, bedrooms)
        estimated_cost, status = calculate_cost(total_area, budget)

        #  SAVE BUILDING PLAN
        building_plan = BuildingPlan(
            plot_length=length,
            plot_width=width,
            floors=floors,
            total_area=total_area,
            estimated_cost=estimated_cost
        )
        db.session.add(building_plan)
        db.session.commit()  # get plan_id

        #  SAVE ROOMS (SAFE SIZE PARSING)
        for room in rooms_data:
            l, w = map(float, room["size"].split("x"))

            room_obj = Room(
                plan_id=building_plan.plan_id,
                room_type=room["name"],
                length=l,
                width=w,
                floor_no=1
            )
            db.session.add(room_obj)

        #  SAVE COST ESTIMATION
        cost_obj = CostEstimation(
            plan_id=building_plan.plan_id,
            rate_per_sqft=1500,
            total_cost=estimated_cost,
            budget_status=status
        )
        db.session.add(cost_obj)
        db.session.commit()

        #  CREATE REQUIRED FOLDERS
        os.makedirs("static/images", exist_ok=True)
        os.makedirs("static/pdfs", exist_ok=True)

        #  GENERATE FLOOR PLAN IMAGE
        timestamp = int(time.time() * 1000)
        image_path = f"static/images/floor_plan_{timestamp}.png"

        draw_floor_plan(
            rooms_data,
            image_path,
            length,
            width
        )

    
        #  GENERATE PDF
     
        pdf_path = f"static/pdfs/building_plan_{timestamp}.pdf"

        plan_data = {
            "area": total_area,
            "cost": estimated_cost
        }

        generate_pdf(plan_data, image_path, pdf_path)

        #  SHOW RESULT PAGE
        return render_template(
            "result.html",
            total_area=total_area,
            rooms=rooms_data,
            estimated_cost=estimated_cost,
            status=status,
            image_path=image_path,
            pdf_path=pdf_path
        )

    return render_template("input_plan.html")
