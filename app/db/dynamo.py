import boto3
from app.models.user import User

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")

def insert_user_dynamo(user: User):
    table.put_item(Item=user.dict())