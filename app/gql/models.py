from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.models.users import User

class UserModel(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = ( relay.Node, )
     
class UserConnection(relay.Connection):
    class Meta:
        node = UserModel

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = ( relay.Node, )
        connection_class = UserConnection
  
  # reg_dttm을 출력할 때, 처리하는 로직
  #def resolve_reg_dttm(parent, info, **input):
  #  return datetime.datetime.strptime(parent.reg_dttm, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
  #
  ## upd_dttm을 출력할 때, 처리하는 로직
  #def resolve_upd_dttm(parent, info, **input):
  #  if parent.upd_dttm is not None:
  #    return datetime.datetime.strptime(parent.upd_dttm, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
  #  else:
  #    return parent.upd_dttm