from pydantic import BaseModel
from typing import List

class BillItem(BaseModel):
    name: str
    price: float
    quantity: int
    subtotal: float

class BillResponse(BaseModel):
    order_id: int
    items: List[BillItem]
    total_amount: float
