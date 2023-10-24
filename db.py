from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, BigInteger, String, Integer, DateTime, Text, ForeignKey, Boolean, Date
from datetime import datetime
import uuid
import random

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    id = Column(BigInteger().with_variant(Integer, 'sqlite'), primary_key=True, autoincrement=True)
    created_date = Column(DateTime(), nullable=False, default=datetime.utcnow)



class AdminUser(Base):
    __tablename__ = "admin_users"
    name = Column(String(64), nullable=False)
    email_address = Column(String(200), unique=True, nullable=False)
    password = Column(Text(), nullable=False)
    suspended = Column(Boolean(), nullable=False, default=False)

    user_sessions = db.relationship('AdminUserSession', backref='user', uselist=False, passive_deletes=True)
    notifications = db.relationship('Notification', backref='user', uselist=False, passive_deletes=True)

    def __repr__(self):
        return f"<AdminUser:{self.name}>"


class AdminUserSession(Base):
    __tablename__ = "admin_user_sessions"
    session_id = Column(String(200), unique=True, nullable=False, default=lambda:uuid.uuid4().hex+"__-__"+uuid.uuid4().hex)
    ipaddress = Column(String(200))
    city = Column(String(128))
    region = Column(String(128))
    country = Column(String(128))
    allowed = Column(Boolean(), nullable=False, default=True)
    admin_id = Column(BigInteger().with_variant(Integer, 'sqlite'), ForeignKey('admin_users.id', ondelete='CASCADE'))

    def __repr__(self):
        return f"<AdminUserSession:{self.session_id}>"



class UserVisit(db.Model):
    __tablename__ = "_user_visits"
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    endpoint = Column(String(128), nullable=False)
    user_ip_address = Column(String(128), nullable=False, default=get_user_ip_address)
    created_date = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<UserVisit:{self.id}:{self.user_ip_address}>"


class User(Base):
    __tablename__ = "users"
    name = Column(String(64), nullable=True)
    avatar_url = Column(Text(), nullable=True)
    username = Column(String(100), nullable=False)
    email_address = Column(String(256), nullable=True, unique=True)
    api_key = Column(String(128), nullable=True, unique=True)
    api_key_created = Column(Date(), nullable=True)
    auth_method = Column(String(32), nullable=True)
    receive_emails = Column(Boolean(), default=True, nullable=True)

    sessions = db.relationship("UserSession", backref="user", cascade="all, delete", passive_deletes=True)
    
    def __repr__(self):
        return "<User:{}>".format(self.name)


class UserSession(Base):
    __tablename__ = "user_sessions"
    session_id = Column(String(128), nullable=False)
    user_id = Column(BigInteger().with_variant(Integer, 'sqlite'), ForeignKey("users.id", ondelete="CASCADE"))

    def __repr__(self):
        return "<UserSession:{}>".format(self.session_id)



class Notification(Base):
    __tablename__ = "notifications"
    render_data = Column(Text(), nullable=False)
    from_ = Column(DateTime(), nullable=False)
    to = Column(DateTime(), nullable=False)
    public_id = Column(String(), nullable=False, unique=True, default=uuid.uuid4)

    admin_id = Column(BigInteger().with_variant(Integer, 'sqlite'), ForeignKey("admin_users.id", ondelete="CASCADE"))

    def __repr__(self):
        return f"<Notification:{self.id}>"
