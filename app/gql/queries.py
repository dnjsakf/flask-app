import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.gql.models import User, UserModel, UserType, UserConnection

class UserQuery(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    
    user = graphene.Field(UserType, email=graphene.String(required=True))
    user_list = graphene.List(
        UserType,
        search=graphene.String(),
        offset=graphene.Int(),
        limit=graphene.Int()
        )
    
    user_edges = SQLAlchemyConnectionField(UserConnection)
    
    def resolve_user(self, info, email, **kwargs):
        return UserModel.get_query(info).filter_by(email=email).first()
    
    def resolve_user_list(self, info, **kwargs):
        query = UserModel.get_query(info)
                
        search = kwargs.get("search", None)
        if search is not None:
            # Equal: query.filter_by(email=search) or query.filter(User.email==search)
            # Like: query.filter(User.email.contains(search))
            query = query.filter(UserModel._meta.model.email.contains(search))
            # query = query.filter(User.email.contains(search))
        
        limit = kwargs.get("limit", None)
        if limit is not None:
            query = query.limit(limit)
        
        offset = kwargs.get("offset", 0)
        if offset is not None:
            query = query.offset(offset)
        
        return query
        
    def resolve_user_edges(self, info, **kwargs):
        return UserModel.get_query(info).filter_by()
        
class Query(UserQuery):
    pass