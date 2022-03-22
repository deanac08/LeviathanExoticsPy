from flask import flash

from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models.user_model import User


class LeopardGecko:
    db = 'leviathan_exotics'
    def __init__(self, data):
        self.id = data['id']
        self.genetics = data['genetics']
        self.sex = data['sex']
        self.hatch_date = data['hatch_date']
        self.description = data['description']
        self.gecko_ID = data['gecko_ID']
        self.breeder = data['breeder']
        self.weight = data['weight']
        self.dam = data['dam']
        self.sire = data['sire']
        self.location = data['location']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def save(cls,data:dict) -> int:
        query = "INSERT INTO leopard_geckos (genetics, sex, hatch_date, gecko_id, description, breeder, weight, dam, sire, location, image) VALUES (%(genetics)s,%(sex)s,%(hatch_date)s,%(gecko_id)s,%(description)s, %(breeder)s,%(weight)s,%(dam)s,%(sire)s, %(location)s, %(image)s);"
        results= connectToMySQL("leviathan_exotics").query_db(query, data)
        return results


    @classmethod
    def get_one(cls,data:dict) -> list:
        query = 'SELECT * FROM leopard_geckos WHERE id = %(id)s;'
        results = connectToMySQL('leviathan_exotics').query_db(query,data)
        if results:
            return cls(results[0])
        return False

    
    # @classmethod
    # def get_all_from_user(cls,data:dict) -> list:
    #     query = 'SELECT * FROM leopard_geckos WHERE user_id = %(user_id)s;'
    #     results = connectToMySQL('leviathan_exotics').query_db(query,data)         
    #     if results:
    #         all_leopard_geckos =[]
    #         for leopard_gecko in results:
    #             all_leopard_geckos.append(cls(leopard_gecko))
    #         return all_leopard_geckos
    #     return False


    @classmethod
    def get_all(cls) -> list:
        query = 'SELECT * FROM leopard_geckos;'
        results = connectToMySQL('leviathan_exotics').query_db(query)
        if results:
            leopard_geckos = []
            for leopard_gecko in results:
                leopard_geckos.append( cls(leopard_gecko) )
            return leopard_geckos 
        return False

    @classmethod
    def update(cls, data:dict) -> None:                        #is it here?!#
        query = "UPDATE leopard_geckos SET genetics=%(genetics)s, sex=%(sex)s, hatch_date=%(hatch_date)s, gecko_id=%(gecko_id)s, descrption=%(description)s, breeder=%(breeder)s, weight=%(weight)s, dam=%(dam)s, sire=%(sire)s, location=%(location)s, image=%(image)s, updated_at=NOW() WHERE id = %(id)s;"
        results = connectToMySQL('leviathan_exotics').query_db(query,data)
        return results
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM leopard_geckos WHERE id = %(id)s;"
        results = connectToMySQL('leviathan_exotics').query_db(query,data)
        return results

    @staticmethod
    def validate(leopard_gecko):
        is_valid = True
        if len(leopard_gecko['genetics']) < 2:
            is_valid = False
            flash("genetics must be at least 2 characters")
        if len(leopard_gecko['sex']) < 2:
            is_valid = False
            flash("sex must be at least 2 characters")
        return is_valid
        return is_valid
        if len(leopard_gecko['breeder']) < 2:
            is_valid = False
            flash("breeder must be at least 2 characters")
        if len(leopard_gecko['gecko_id']) < 2:
            is_valid = False
            flash("gecko_id must be at least 2 characters")
        return is_valid