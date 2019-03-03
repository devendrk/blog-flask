from service-jobboard import db
from datetime import datetime


class Jobs(db.Model):
    company = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    expire = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
