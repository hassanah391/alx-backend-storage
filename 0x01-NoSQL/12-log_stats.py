#!/usr/bin/env python3
"""
12-log_stats.py

This script connects to a MongoDB database, specifically the `logs.nginx` collection,
and prints statistics about HTTP request methods and a specific endpoint (`/status`).

Expected Output Format:
<total number of logs> logs
Methods:
    method GET: <count>
    method POST: <count>
    method PUT: <count>
    method PATCH: <count>
    method DELETE: <count>
<status check count> status check
"""

from pymongo import MongoClient

def main():
    """
    Connects to the MongoDB instance, accesses the 'logs.nginx' collection,
    and prints the required statistics in a specific format.
    """
    # Connect to the MongoDB server running on localhost and default port
    client = MongoClient()

    # Access the 'logs' database and the 'nginx' collection
    db = client.logs
    collection = db.nginx

    # Count the total number of documents (logs) in the collection
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Define the list of HTTP methods to report statistics for
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Print method statistics with indentation
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count documents where method is GET and path is "/status"
    status_check_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    main()
