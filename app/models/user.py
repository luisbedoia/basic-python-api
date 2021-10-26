from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

class users(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    ts = fields.FloatField()
    cumulative_steps = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


user = pydantic_model_creator(users, name="user")
user_in = pydantic_model_creator(users, name="user_in", exclude_readonly=True)