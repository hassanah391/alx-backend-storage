# 0x01-NoSQL

This directory contains scripts and Python programs that demonstrate the use of MongoDB, a NoSQL database. The tasks focus on performing various database operations such as creating, reading, updating, and deleting documents in MongoDB collections.

## Files and Descriptions

### MongoDB Shell Scripts
- **0-list_databases**: Lists all databases in the MongoDB instance.
- **1-use_or_create_database**: Creates or uses the database `my_db`.
- **2-insert**: Inserts a document into the `school` collection.
- **3-all**: Lists all documents in the `school` collection.
- **4-match**: Lists all documents in the `school` collection where `name="ALX"`.
- **5-count**: Displays the number of documents in the `school` collection.
- **6-update**: Updates the `address` field of documents where `name="Holberton school"`.
- **7-delete**: Deletes all documents where `name="Holberton school"`.

### Python Scripts
- **8-all.py**: Contains the `list_all` function to list all documents in a MongoDB collection.
- **9-insert_school.py**: Contains the `insert_school` function to insert a new document into a MongoDB collection.
- **10-update_topics.py**: Contains the `update_topics` function to update the `topics` field of a school document.
- **11-schools_by_topic.py**: Contains the `schools_by_topic` function to find schools with a specific topic.
- **12-log_stats.py**: Analyzes logs stored in the `logs.nginx` collection and prints statistics about HTTP methods and `/status` endpoint usage.

### Python Test Files
- **8-main.py**: Tests the `list_all` function.
- **9-main.py**: Tests the `insert_school` function.
- **10-main.py**: Tests the `update_topics` function.
- **11-main.py**: Tests the `schools_by_topic` function.

### Other Files
- **.gitignore**: Ignores temporary files created by the Emacs editor.

## Requirements
- MongoDB must be installed and running on `localhost` with the default port `27017`.
- Python 3.x and the `pymongo` library are required for the Python scripts.

## Usage
1. Start the MongoDB server:
   ```bash
   sudo service mongod start
   ```

2. Run the MongoDB shell scripts using the `mongo` command:
    ```
    mongo <script_name>
    ```

3. Run the Python scripts:
    ```
    python3 <script_name>.py
    ```



