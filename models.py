from extensions import db


# -----------------------------
# NEWSLETTER
# -----------------------------
class Subscriber(db.Model):

    __tablename__ = "subscribers"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )


# -----------------------------
# CONTACT
# -----------------------------
class ContactMessage(db.Model):

    __tablename__ = "contact_messages"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(
        db.String(255),
        nullable=False
    )

    email = db.Column(
        db.String(255),
        nullable=False
    )

    phone = db.Column(
        db.String(100)
    )

    service = db.Column(
        db.String(255)
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )