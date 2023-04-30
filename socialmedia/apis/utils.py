import jwt
from apis.models import tbl_users
from socialmedia.settings import SECRET_KEY

def validate_user(request, token):
        is_valid_user = False
        try:
            decode_data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms="HS256", verify=False)
            print(decode_data)
            user = tbl_users.objects.filter(email=decode_data['message']['email'], password=decode_data['message']['password'])
            print(user)
            if user:
                is_valid_user = True
        except Exception as e:
            message = f"Token is invalid --> {e}"
            print({"message": message})
        return is_valid_user

def get_data(token):
    decode_data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms="HS256", verify=False)
    print(decode_data)
    return decode_data
    