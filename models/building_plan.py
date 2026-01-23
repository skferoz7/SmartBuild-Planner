from models import db
from datetime import datetime

class BuildingPlan(db.Model):
    __tablename__ = "building_plans"

    plan_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)

    plot_length = db.Column(db.Float, nullable=False)
    plot_width = db.Column(db.Float, nullable=False)
    floors = db.Column(db.Integer, nullable=False)

    total_area = db.Column(db.Float, nullable=False)
    estimated_cost = db.Column(db.Float, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    rooms = db.relationship("Room", backref="building_plan", lazy=True)
    cost_estimation = db.relationship(
        "CostEstimation", backref="building_plan", uselist=False
    )

    def __repr__(self):
        return f"<BuildingPlan {self.plan_id}>"
