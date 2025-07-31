from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    age_group = Column(String(20))  # 'elementary', 'middle', 'high'
    skill_level = Column(String(20), default="beginner")

    # relationships
    projects = relationship("Project", back_populates="owner")
    learning_progress = relationship("LearningProgress", back_populates="user")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    language = Column(String(20))
    code_content = Column(JSON)  # store versioned code
    visibility = Column(String(20), default="private")

    # relationships
    owner = relationship("User", back_populates="projects")
    collaborators = relationship("ProjectCollaborator", back_populates="project")

class LearningProgress(Base):
    __tablename__ = "learning_progress"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    module_id = Column(String(50))
    completion_percentage = Column(Integer, default=0)
    last_accessed = Column(DateTime)
    performance_metrics = Column(JSON)  # detailed metrics

    # relationships
    user = relationship("User", back_populates="learning_progress")

class CodeExecution(Base):
    __tablename__ = "code_executions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    code = Column(Text)
    language = Column(String(20))
    execution_time = Column(DateTime)
    result = Column(JSON)
    errors = Column(JSON)
    visualization_data = Column(JSON)  # data for visualization

class ProjectCollaborator(Base):
    __tablename__ = "project_collaborators"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    project = relationship("Project", back_populates="collaborators")
