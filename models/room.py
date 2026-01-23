from models import db

class Room(db.Model):
    __tablename__ = "rooms"

    room_id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(
        db.Integer, db.ForeignKey("building_plans.plan_id"), nullable=False
    )

    room_type = db.Column(db.String(50), nullable=False)
    length = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    floor_no = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Room {self.room_type}>"
