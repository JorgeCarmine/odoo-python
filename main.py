import xmlrpc.client
from config import Settings

settings = Settings()

url = settings.url
db = settings.database
username = settings.username
password = settings.password

print('url', url)
print('db', db)
print('username', username)
print('password', password)

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print('UID: ', uid)
