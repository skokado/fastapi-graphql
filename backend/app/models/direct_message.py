from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from . import base

if TYPE_CHECKING:
    from .user import User


class DirectMessage(base.Model):
    __tablename__ = "direct_messages"

    id: Mapped[int] = mapped_column(primary_key=True)

    created_at: Mapped[datetime] = mapped_column(sa.DateTime, server_default=sa.func.now())

    sender_id: Mapped[int] = mapped_column(sa.ForeignKey("users.id"))
    sender: Mapped["User"] = relationship(back_populates="sent_direct_messages", foreign_keys=[sender_id])

    receiver_id: Mapped[int] = mapped_column(sa.ForeignKey("users.id"))
    receiver: Mapped["User"] = relationship(back_populates="received_direct_messages", foreign_keys=[receiver_id])

    text = sa.Column(sa.String)
