import boto3
import hashlib
from env import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY


# Connect to the DynamoDB database
dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-northeast-1',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
table = dynamodb.Table('users')# type: ignore
"""
table.put_item(
   Item={
        'username': 'janedoe',
        'password': hashlib.sha256('Namaganda.7'.encode('utf-8')).hexdigest(),
        "age": 20,
        "email": "mbalireshawal@gmail.com",
        "gender": "male",
        "insurance": 'none',
        "surname": 'Mbalire',
        "other_name": 'Shawal',
        "phone_number": '0760044705',
        "role": 'patient',
        "records": {}
    }
)"""
def get_user(username,password):
    """Returns user dictionary if user exists, else returns None"""
    response = table.get_item(
        Key={
            'username': username,
            'password': password
        }
    )
    try:
        user = response['Item']
        return user
    except:
        return None


def insert_user(username, password,email,age,gender,insurance,surname,other_name,phone_number,role):
    table.put_item(
   Item={
        'username': username,
        'password': hashlib.sha256(password.encode('utf-8')).hexdigest(),
        "age": age,
        "email": email,
        "gender": gender,
        "insurance": insurance,
        "surname": surname,
        "other_name": other_name,
        "phone_number": phone_number,
        "role": role,
        "records": {}
    }
)

def fetch_all_users():
    """returns list of user dictionaries"""
    response=table.scan()
    return response['Items']
"""print(get_user(
    username='janedoe',
    password=hashlib.sha256('Namaganda.7'.encode('utf-8')).hexdigest()
))"""

def add_diagnosis(username,password,note):
    user = get_user(username,password)
    #records = user['records']
    #add note to records
    pass

