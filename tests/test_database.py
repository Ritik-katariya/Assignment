from src.database.mongo_utils import insert_record, fetch_latest_record

def test_database():
    sample_record = {
        "_id": "test_id",
        "trends": ["Test1", "Test2", "Test3", "Test4", "Test5"],
        "datetime": "2024-12-25T12:00:00",
        "ip_address": "127.0.0.1"
    }
    insert_record(sample_record)
    fetched = fetch_latest_record()
    assert fetched["_id"] == "test_id"
