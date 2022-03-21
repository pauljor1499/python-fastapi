from pydantic import BaseModel
from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
)

class Student(BaseModel):
    first_name: str = None
    middle_init: Optional[str] = None
    last_name: str = None
    title: str = None
    school: str = None
    school_email: str = None
    password1: str = None
    password2: str = None