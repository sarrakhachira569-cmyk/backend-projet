from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"
    # Identifiant unique
    id = Column(Integer, primary_key=True, index=True)

    # Nom utilisateur
    name = Column(String(100), nullable=False)

    # Email unique
    email = Column(String(150), unique=True, nullable=False, index=True)

    # Mot de passe sécurisé (hash)
    password = Column(String(255), nullable=False)

    # Rôle utilisateur (admin, user, etc.)
    role = Column(String(50), default="user")

    # Compte actif ou non
    is_active = Column(Boolean, default=True)

    # Dernière connexion
    last_login = Column(DateTime, nullable=True)

    # Dates système
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Suppression logique
    deleted_at = Column(DateTime, nullable=True)


