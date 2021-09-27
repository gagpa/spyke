from datetime import datetime

import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from configs.db import DB_URL
Base = declarative_base()
engine = sql.create_engine(DB_URL)

connection = engine.connect()
SessionFactory = sessionmaker(bind=engine, autoflush=False)
Session = scoped_session(SessionFactory)


def auto_close_session(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        Session().close()
        return result

    return wrapper


class Container(Base):
    __tablename__ = 'containers'

    id = sql.Column(sql.Integer, primary_key=True)

    label = sql.Column(sql.VARCHAR(100), unique=True, nullable=False)
    host = sql.Column(sql.VARCHAR(255), nullable=True)
    name = sql.Column(sql.VARCHAR(500), nullable=False)
    curr_status = sql.Column(sql.VARCHAR(100), nullable=True)
    is_active = sql.Column(sql.Boolean, default=False)
    scanned_at = sql.Column(sql.DateTime, nullable=True)
    scan_delay = sql.Column(sql.Integer, default=3)
    chat_id = sql.Column(sql.VARCHAR(25), nullable=False)

    created_at = sql.Column(sql.DateTime, default=datetime.now(), nullable=False)
    updated_at = sql.Column(sql.DateTime, onupdate=datetime.now(), nullable=True)
