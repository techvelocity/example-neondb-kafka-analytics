from datetime import datetime
from fastapi import FastAPI
from db import Base, engine, SessionLocal
from models import AnalyticsData
from sqlalchemy import select

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_analytics_data(event_type: str, start_date: str = None, end_date: str = None):
    db = SessionLocal()
    # Prepare the start and end dates
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None

    # Create the base select statement
    select_stmt = select(AnalyticsData).where(AnalyticsData.event_type == event_type)

    # Apply date filters if provided
    if start_datetime:
        select_stmt = select_stmt.where(AnalyticsData.timestamp >= start_datetime)
    if end_datetime:
        select_stmt = select_stmt.where(AnalyticsData.timestamp <= end_datetime)

    # Execute the select statement and retrieve the results
    results = db.execute(select_stmt).scalars().all()

    return results


@app.get("/api/click-analytics")
def get_click_analytics(start_date: str = None, end_date: str = None):
    return get_analytics_data("click", start_date, end_date)


@app.get("/api/view-analytics")
def get_view_analytics(start_date: str = None, end_date: str = None):
    return get_analytics_data("view", start_date, end_date)
