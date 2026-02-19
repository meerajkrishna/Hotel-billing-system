from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.order_model import Order
from app.models.order_item_model import OrderItem
from app.models.item_model import Item
from app.models.audit_log_model import AuditLog
from app.auth.dependencies import cashier_required

router = APIRouter(prefix="/bill", tags=["Billing"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{order_id}", dependencies=[Depends(cashier_required)])
def generate_bill(
    order_id: int,
    db: Session = Depends(get_db),
    user=Depends(cashier_required)
):
    order = db.query(Order).filter(Order.id == order_id).first()

    items = []
    total = 0

    for oi in db.query(OrderItem).filter(OrderItem.order_id == order_id):
        item = db.query(Item).filter(Item.id == oi.item_id).first()
        subtotal = item.price * oi.quantity
        total += subtotal
        items.append({
            "name": item.name,
            "price": item.price,
            "quantity": oi.quantity,
            "subtotal": subtotal
        })

    log = AuditLog(
        user=user["sub"],
        role=user["role"],
        action=f"Generated bill for order {order_id}"
    )
    db.add(log)
    db.commit()

    return {
        "order_id": order_id,
        "items": items,
        "total_amount": total
    }
