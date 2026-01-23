from models import db

class CostEstimation(db.Model):
    __tablename__ = "cost_estimations"

    cost_id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(
        db.Integer, db.ForeignKey("building_plans.plan_id"), nullable=False
    )

    rate_per_sqft = db.Column(db.Float, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    budget_status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<CostEstimation {self.total_cost}>"
