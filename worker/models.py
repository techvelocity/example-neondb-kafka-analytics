from sqlalchemy import create_engine, Column, Integer, String
from db import Base


class AnalyticsData(Base):
    __tablename__ = 'analytics_data'
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(Integer)
    event_type = Column(String)
    user_id = Column(String)
    page_id = Column(String)
    duration = Column(Integer)
