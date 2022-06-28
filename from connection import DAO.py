from connection import DAO

dao = DAO()
a = dao.listTable('customer')
print(type(a))