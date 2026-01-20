from pydantic import BaseModel, EmailStr
from typing import Optional

class Create_user(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[str] = "user"
    is_active: Optional[bool] = True
class User_login(BaseModel):
    email:EmailStr
    password: str


	
	
	
	
	
	

	
 
    
 