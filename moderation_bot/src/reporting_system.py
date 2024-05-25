```python
# reporting_system.py

import pymongo
import discord
import pandas as pd

class ReportingSystem:
    def __init__(self, db_uri, db_name, collection_name):
        self.client = pymongo.MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def flag_content(self, user_id, content):
        report = {
            "user_id": user_id,
            "content": content,
            "status": "pending"
        }
        self.collection.insert_one(report)

    def get_pending_reports(self):
        pending_reports = list(self.collection.find({"status": "pending"}))
        return pending_reports

    def process_report(self, report_id, action):
        if action == "delete":
            self.collection.update_one({"_id": report_id}, {"$set": {"status": "deleted"}})
        elif action == "ignore":
            self.collection.update_one({"_id": report_id}, {"$set": {"status": "ignored"}})

    def get_reported_content(self):
        reported_content = list(self.collection.find())
        return reported_content

    def export_reports_to_csv(self, filename):
        reported_content = self.get_reported_content()
        df = pd.DataFrame(reported_content)
        df.to_csv(filename, index=False)

    def close_connection(self):
        self.client.close()
```