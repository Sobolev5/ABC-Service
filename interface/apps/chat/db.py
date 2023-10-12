import re
import json
from datetime import datetime
from simple_print import sprint

# lesson5 lesson6 
class RamDB:
    db = {}  

    def __new__(cls, *args, **kwargs):
        with open('db.json', 'w+') as f:
            try:
                cls.db = json.load(f)
            except:
                cls.db = {}
        return super(RamDB, cls).__new__(cls, *args, **kwargs)


    def create_table(self, table_name: str, fields: tuple) -> bool:
        db = RamDB.db

        assert isinstance(table_name, str) == True, "table name must be str"
        assert isinstance(fields, tuple) == True, "fields must be tuple"

        if table_name not in db:
            db[table_name] = {}
            db[table_name]["fields"] = ("id",) + fields
            db[table_name]["records"] = []
            return True
        else:
            return False


    def create_record(self, table_name: str, record: list) -> dict:
        db = RamDB.db
        
        assert isinstance(table_name, str) == True, "table name must be str"
        assert (table_name in db) == True, "invalid table name"
        assert isinstance(record, list) == True, "record must be list"
        assert len(db[table_name]["fields"]) - 1 == len(record), "invalid record"

        fields = db[table_name]["fields"]
        record_id = int(round(datetime.now().timestamp()))
        record = [record_id] + record
        db[table_name]["records"].append(record)
        record_as_dict = dict(zip(fields, record))
        RamDB.dump_to_hdd()
        return record_as_dict


    def read_record(self, table_name: str, query: dict = {}) -> list:
        db = RamDB.db
        
        assert isinstance(table_name, str) == True, "table name must be str"
        assert isinstance(query, dict) == True, "query must be dict"

        if table_name in db:
            fields = db[table_name]["fields"]
            records = []
            if not query: # get all
                for record in db[table_name]["records"]:
                    record_as_dict = dict(zip(fields, record))
                    records.append(record_as_dict)                       
                return records
            else:
                for record in db[table_name]["records"]:
                    record_as_dict = dict(zip(fields, record))
                    for k, v in query.items():
                        if k in record_as_dict and record_as_dict[k] != v: 
                            break
                    else:
                        records.append(record_as_dict)    
                    
                return records
        else:
            return []


    def read_record_sql(self, sql_query: str) -> list:
        # https://regex101.com/
        db = RamDB.db
        
        assert isinstance(sql_query, str) == True, "sql_query must be str"

        sql_regexp = re.compile(r'SELECT \* FROM (?P<table_name>\w+) WHERE (?P<condition>.+);')
        named_re_groups = sql_regexp.search(sql_query)

        table_name = named_re_groups["table_name"]
        condition = named_re_groups["condition"]

        condition_key, condition_value = condition.split("=")
        query = {condition_key: condition_value.strip('"')}
        return self.read_record(table_name=table_name, query=query)


    def update_record(self, table_name: str, record_id, query: dict = {}) -> dict:
        db = RamDB.db
        
        assert isinstance(table_name, str) == True, "table name must be str"
        assert isinstance(record_id, int) == True, "record id must be int"
        assert isinstance(query, dict) == True, "query must be dict"

        fields = db[table_name]["fields"]
        records = []

        record_updated = []
        for record_num, record in enumerate(db[table_name]["records"]):
            record_as_dict = dict(zip(fields, record))

            if record_as_dict["id"] != record_id:
                continue
            else:
                for k, v in query.items():
                    if k in record_as_dict:
                        updated = True
                        record_as_dict[k] = v
                record_updated = [v for k, v in record_as_dict.items()]     
                db[table_name]["records"][record_num] = record_updated
                break
        
        if record_updated:
            return dict(zip(fields, record_updated))
        else:
            return {"error": "no update"}


    def delete_record(self, table_name: str, record_id: int) -> bool:
        db = RamDB.db
        
        assert isinstance(table_name, str) == True, "table name must be str"
        assert isinstance(record_id, int) == True, "record id must be int"

        fields = db[table_name]["fields"]
        records = []
        record_num_to_delete = None
        for record_num, record in enumerate(db[table_name]["records"]):
            record_as_dict = dict(zip(fields, record))

            if record_as_dict["id"] != record_id:
                continue
            else:
                record_num_to_delete = record_num   
                break
        
        if record_num_to_delete:
            del db[table_name]["records"][record_num] 
            return True
        else:
            return False


    @classmethod
    def show_me_db(cls):
        return cls.db


    @classmethod
    def dump_to_hdd(cls): 
        with open('db.json', 'w+') as f:
            json.dump(RamDB.db, f)
