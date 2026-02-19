from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.order_model import Order
from app.models.order_item_model import OrderItem
from app.models.audit_log_model import AuditLog
from app.schemas.order_schema import OrderCreate
from app.auth.dependencies import cashier_required

router = APIRouter(prefix="/orders", tags=["Orders"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", dependencies=[Depends(cashier_required)])
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    user=Depends(cashier_required)
):
    new_order = Order()
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    total = 0
    for item in order.items:
        order_item = OrderItem(
            order_id=new_order.id,
            item_id=item.item_id,
            quantity=item.quantity
        )
        db.add(order_item)
        total += item.price * item.quantity

    new_order.total_amount = total

    log = AuditLog(
        user=user["sub"],
        role=user["role"],
        action=f"Created order ID {new_order.id}"
    )
    db.add(log)

    db.commit()

    return {
        "order_id": new_order.id,
        "total_amount": total
    }
