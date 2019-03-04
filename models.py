from service-jobboard import db
from datetime import datetime
from flask_sqlalchemy import SQLAalchemy


class Jobs(db.Model):
    id = db.Column(db.Integer)
    company = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    expire = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def to_dict(self):
        return {
            'id': self.id,
            'company': self.company,
            'description': self.description,
            'expire': self.expire
        }
