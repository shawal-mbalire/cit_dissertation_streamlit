import boto3
from dotenv import load_dotenv

load_dotenv('.env')

# Connect to the DynamoDB database
dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-northeast-1',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
table = dynamodb.Table('users')
"""
passw='Namaganda.7'
encoded_password = passw.encode('utf-8')
password = hashlib.sha256(encoded_password).hexdigest()
table.put_item(
   Item={
        'username': 'janedoe',
        'password': password,
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
    response = table.get_item(
        Key={
            'username': username,
            'password': password
        }
    )
    try:
        user = response['Item']
        print(user)
    except:
        user = None


def insert_user(username, password,email,age,gender,insurance,surname,other_name,phone_number,role):
    table.put_item(
   Item={
        'username': username,
        'password': password,
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
    response=table.scan()
    return response['Items']

print(fetch_all_users())

def add_diagnosis():
    pass
