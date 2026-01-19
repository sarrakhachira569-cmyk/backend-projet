from pydantic import BaseModel, EmailStr
from typing import Optional

class Create_user(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[str] = "user"
    is_active: Optional[bool] = True

	
	
	
	
	
	

	
 
    
 