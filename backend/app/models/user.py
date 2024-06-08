from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from . import base
from .direct_message import DirectMessage



class User(base.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(50), unique=True)

    sent_direct_messages: Mapped[list["DirectMessage"]] = relationship(back_populates="sender", foreign_keys=[DirectMessage.sender_id])
    received_direct_messages: Mapped[list["DirectMessage"]] = relationship(back_populates="receiver", foreign_keys=[DirectMessage.receiver_id])
