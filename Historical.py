from connection import DAO

def queryIdCustomer(id):
    dao = DAO()
    sql = """   select s.id, 
                    s.description_service, 
                    s.price, 
                    s.idVeterinarian, 
                    CONCAT(v.name, ' ', v.last_name) as veterinarian_name,
                    s.create_at as date_service
                from services s
                inner join veterinarian v on s.idVeterinarian = v.id
                where idCustomer = {};"""
    sql = sql.format(id)

    return dao.customQuery(sql)

def queryIdVeterinarian(id):
    dao = DAO()
    sql = """   select s.id, 
                    s.description_service, 
                    s.price, 
                    s.idCustomer, 
                    CONCAT(c.name, ' ', c.last_name) as customer_name, 
                    s.create_at as date_service
                from services s
                inner join customer c on s.idCustomer = c.id
                where idVeterinarian = {};"""
    sql = sql.format(id)

    return dao.customQuery(sql)