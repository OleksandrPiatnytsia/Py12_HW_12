from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ContactSchema(BaseModel):
    name: str = Field('Albert', min_length=3, max_length=100)
    sur_name: str = Field('Einstein', min_length=3, max_length=100)
    email: EmailStr
    phone: str = Field('+380967774411', length=13)
    birthday: date


class ContactSchemaResponse(ContactSchema):
    id: str = Field('1', min_length=1, max_length=36)
