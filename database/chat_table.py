import sqlite3

import requests

from server.config import get_config

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


def post_insert_record(userid: str, model: str, conversation_id: str, action: str, jailbreak: str, content_type: str, internet_access: bool, role, content, response: str):
    query_json = {
        "payload": {
            "userAvator": "https://pix.veryjack.com/i/2023/04/04/fsxnkv.webp",
            "userName": "akun",
            "title": "wechat-miniapp",
            "message": content,
            "openId": userid,
            "conversationId": conversation_id,
            "action": action,
            "jailbreak": jailbreak,
            "contentType": content_type,
            "internetAccess": internet_access,
            "aiResponse": response.decode("utf-8"),
        },
        "params": {
            "addr": "0xb8F33dAb7b6b24F089d916192E85D7403233328A",
            "random": "a9a58d316a16206ca2529720d01f8a9d10779eb330902f4ec05cf358a3418a9f",
            "nonce": "1a9b1b1d9e854196143504b776b65e9fb5c87fe4930466a8fe68763fa6e48aed",
            "ts": "1680592645793",
            "hash": "0xc324d54dc3f613b8b33ce60d3085b5fc16b9012fa1df733361b370fec663bc67",
            "method": 2,
            "msg": "Please sign this message"
        },
        "sig": "825ccf873738de91a77b0de19b0f2db7e549efcca36215743c184197173967d770b141201651b21d6d89d27dc8d6cde6ccdc3151af67ed29b5cdaed2cecf3950"
    }
    host = get_config('groupx_api_url')
    response = requests.post(
        host+'/v1/chat/0xb8F33dAb7b6b24F089d916192E85D7403233328A', json=query_json, verify=False)
    ret = response.text
    print("post chat to group api:", ret)
    return ret


def insert_chat_record(userid: str, model: str, conversation_id: str, action: str, jailbreak: str, content_type: str, internet_access: bool, role, content, response: str):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)

    # Insert the chat record into the chat_records table
    with conn:
        conn.execute('INSERT INTO chat_records (userid, model, conversation_id, action, jailbreak, content_type, internet_access, role, content,response) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)',
                     (userid, model, conversation_id, action, jailbreak, content_type, internet_access, role, content, response.decode('utf-8')))

    # Close the connection
    conn.close()
    post_insert_record(userid, model, conversation_id, action, jailbreak,
                       content_type, internet_access, role, content, response)


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
