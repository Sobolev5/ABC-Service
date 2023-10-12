from simple_print import sprint


def test_db_via_simple_console_script():
    # lesson5 lesson6 

    # python run.py chat.db_test "test_db_via_simple_console_script()" 

    from chat.db import RamDB
    db = RamDB()

    # create table
    sprint("create table", c="green")
    created = db.create_table(table_name="chat", fields=("name", "description"))  
    assert created == True
    sprint(RamDB.show_me_db(), i=4)  

    # create record
    sprint("create record", c="green")
    record = db.create_record(table_name="chat", record=["Stuff chat", "For admins"])
    record = db.create_record(table_name="chat", record=["Dev chat", "For developers"])
    assert isinstance(record["id"], int)
    sprint(record, i=4) 
    sprint(RamDB.show_me_db(), i=4) 

    # read record
    sprint("read record", c="green")
    records = db.read_record(table_name="chat", query={"name": "Dev chat"})
    assert isinstance(records, list)
    if records:
        sprint(records)
        assert isinstance(records[0]["id"], int) 
    sprint(RamDB.show_me_db(), i=4)   

    # read record sql
    sprint("read record sql", c="green")
    records = db.read_record_sql(sql_query='SELECT * FROM chat WHERE name="Dev chat";')
    assert isinstance(records, list)
    
    record_id = None
    if records:
        sprint(records)
        assert isinstance(records[0]["id"], int) 
        record_id = records[0]["id"]

    sprint(RamDB.show_me_db(), i=4)  

    if record_id:
        # update record
        sprint("update record", c="green")
        updated_record = db.update_record(table_name="chat", record_id=record_id, query={"description": "For developers111"})
        assert isinstance(updated_record, dict)
        sprint(updated_record, i=4) 
        sprint(RamDB.show_me_db(), i=4)  

        # delete record
        sprint("delete record", c="green")
        deleted = db.delete_record(table_name="chat", record_id=record_id)
        assert deleted
        sprint(RamDB.show_me_db(), i=4)  

