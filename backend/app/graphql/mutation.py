import strawberry

from app.usecases import direct_message as usecase

from .schemas import User, DirectMessageRequest, DirectMessage
from ..resolvers import users as users_resolver
from .subscription import direct_message_subscriptions


@strawberry.type
class Mutation:
    create_user: User = strawberry.mutation(resolver=users_resolver.create)

    @strawberry.mutation
    async def post_dm(self, data: DirectMessageRequest, info: strawberry.Info) -> DirectMessage:
        new_dm = await usecase.create_dm(data, info.context.db)
        await direct_message_subscriptions.publish(new_dm)
        return DirectMessage(
            id=new_dm.id,
            created_at=new_dm.created_at,
            receiver_id=new_dm.receiver_id,
            sender_id=new_dm.sender_id,
            text=new_dm.text,
        )
