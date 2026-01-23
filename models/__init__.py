from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.user import User
from models.building_plan import BuildingPlan
from models.room import Room
from models.cost_estimation import CostEstimation
