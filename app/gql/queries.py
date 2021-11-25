import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.gql.models import UserModel, UserConnection, UserType

class UserQuery(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    
    user = graphene.Field(UserType, email=graphene.String(required=True))
    user_list = graphene.List(UserType)
    
    user_edges = SQLAlchemyConnectionField(UserConnection)
    
    def resolve_user(self, info, email, **kwargs):
        return UserModel.get_query(info).filter_by(email=email).first()
    
    def resolve_user_list(self, info, **kwargs):
        return UserModel.get_query(info).filter_by()
        
    def resolve_user_edges(self, info, **kwargs):
        return UserModel.get_query(info).filter_by()
        
class Query(UserQuery):
    pass