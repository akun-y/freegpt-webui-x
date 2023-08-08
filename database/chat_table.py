import sqlite3

db_name = 'db/chat_records.db'
def create_chat_table():
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)

    # Create the chat_records table if it doesn't exist
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS chat_records (
                        id INTEGER PRIMARY KEY,
                        userid TEXT,
                        model TEXT,
                        conversation_id TEXT,
                        action TEXT,
                        jailbreak INTEGER,
                        content_type TEXT,
                        internet_access INTEGER,
                        role TEXT,
                        content TEXT,
                        response TEXT
                    )''')

    # Close the connection
    conn.close()


def insert_chat_record(userid: str, model: str, conversation_id: str, action: str, jailbreak: str, content_type: str, internet_access: bool, role, content, response: str):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)

    # Insert the chat record into the chat_records table
    with conn:
        conn.execute('INSERT INTO chat_records (userid, model, conversation_id, action, jailbreak, content_type, internet_access, role, content,response) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)',
                     (userid, model, conversation_id, action, jailbreak, content_type, internet_access, role, content, response.decode('utf-8')))

    # Close the connection
    conn.close()


def retrieve_chat_records():
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)

    # Retrieve all chat records from the chat_records table
    with conn:
        cursor = conn.execute(
            'SELECT userid, model, conversation_id, action, jailbreak, content_type, internet_access, role, content FROM chat_records')
        chat_records = cursor.fetchall()

    # Close the connection
    conn.close()

    return chat_records


# # Create the chat_records table (if not exists)
create_chat_table()
