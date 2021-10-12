from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    ts = fields.FloatField()
    cumulativeSteps = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)