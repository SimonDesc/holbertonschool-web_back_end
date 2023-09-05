#!/usr/bin/env python3
from pymongo import MongoClient
""" a Python script that provides some stats about Nginx logs stored in MongoDB"""

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    
    total_logs = nginx_logs.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = []
    for method in methods:
        count = nginx_logs.count_documents({"method": method})
        method_counts.append(count)

    status_count = nginx_logs.count_documents({"method": "GET", "path": "/status"})
    
    print(f"{total_logs} logs")
    print("Methods:")
    for i in range(len(methods)):
        print(f"\tmethod {methods[i]}: {method_counts[i]}")

    print(f"{status_count} status check")

