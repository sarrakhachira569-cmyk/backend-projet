from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from .model import User
from .schema import Create_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Création des tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

# Ouvre session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Create user
@router.post("/create")
def create_user(user_data: Create_user, db: Session = Depends(get_db)):
    # Vérifier si email existe déjà
    if db.query(User).filter(User.email == user_data.email).first():
        raise HTTPException(status_code=400, detail="Email déjà utilisé")
    
    user = User(
        name=user_data.name,
        email=user_data.email,
        password=user_data.password,  # يمكنك هنا تعمل hash إذا تحب
        role=user_data.role,
        is_active=user_data.is_active
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
# Read all users
@router.get("/userList")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
# Read user by ID
@router.get("/user/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User non trouvé")
    return user
# Read user by name
@router.get("/username/{user_name}")
def get_user_name(user_name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == user_name).first()
    if not user:
        raise HTTPException(status_code=404, detail="User non trouvé")
    return user
# Update user
@router.patch("/Users/{user_id}")
def update_user(user_id: int, user_update: Create_user, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User non trouvé")
    
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    return user
# Delete user
@router.delete("/Users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User non trouvé")
    
    db.delete(user)
    db.commit()
    return None
