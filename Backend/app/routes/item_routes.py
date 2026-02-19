from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.item_model import Item
from app.models.audit_log_model import AuditLog
from app.schemas.item_schema import ItemCreate
from app.auth.dependencies import admin_required

router = APIRouter(prefix="/items", tags=["Items"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()


@router.post("/", dependencies=[Depends(admin_required)])
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    new_item = Item(name=item.name, price=item.price)
    db.add(new_item)

    log = AuditLog(
        user=user["sub"],
        role=user["role"],
        action=f"Created item: {item.name}"
    )
    db.add(log)

    db.commit()
    db.refresh(new_item)
    return new_item
