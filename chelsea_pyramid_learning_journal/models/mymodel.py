"""Creating Journal class to create database entries."""

from sqlalchemy import (
    Column,
    Integer,
    Unicode,
)

from .meta import Base


class Journal(Base):
    """Describing properties of each LJ entry in DB."""

    __tablename__ = 'learning_journals'
    id = Column(Integer, primary_key=True)
    author = Column(Unicode)
    creation_date = Column(Unicode)
    title = Column(Unicode)
    body = Column(Unicode)

    def __repr__(self):
        """Return LJ id."""
        return '<{}, {}, {}, {}, {}>'.format(self.id, self.author, self.creation_date, self.title, self.body)
