from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))