from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Interger, db.Foreign_key("stores.id"), unique=False, nullable=False)
    store = db.relationship("StoreModel", back_populates="items")



