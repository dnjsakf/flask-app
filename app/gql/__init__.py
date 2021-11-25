from app.gql.queries import Query
from graphene import Schema

schema = Schema(
    query=Query
)