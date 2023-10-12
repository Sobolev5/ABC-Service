from ninja.security import HttpBearer
from ninja.security import HttpBasicAuth

# lesson9
class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        if username == "abc@abc.abc" and password == "abc":
            return username

# lesson9
class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "my_secret_token":
            return token

# lesson9
# Идея в том, что у разных пользователей разные Bearer токены.
# Пользователь копирует сгенерированный токен у себя в ЛК (или получает на почту)
# И далее подписывает запросы к API с полученным ключом.
# Authorization: Bearer 1:super_hash_key_md5
#
# class AuthBearerFromRealLife(HttpBearer):
#     def authenticate(self, request, token):
#         user_id, key_verify = token.split(':')
#         key = hashlib.md5()
#         key.update((f"{user_id}{API_SALT}").encode()) # Вычисляю токен еще раз (такая же операция происходит и при его генерации)
#         key = "%s" % key.hexdigest()  
#         if key_verify == key: # И сравниваю вычисленный токен с полученным из запроса токеном
#             request.user_id = user_id
#             return token


