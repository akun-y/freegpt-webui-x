import sqlite3
import string

from server.config import get_config


models_init = get_config("models",{})
db_name = 'db/user_database.db'
class UserDatabase:
    def __init__(self, db_name=db_name):
        self.db_name = db_name

    def _connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _disconnect(self):
        self.conn.close()

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, userid TEXT UNIQUE, model_list TEXT, username TEXT, email TEXT)''')
        self.conn.commit()

    def create_user(self, userid, model_list=models_init, username=None, email=None):
        if not username:
            username = userid
        if not email:
            email = f'{userid}@example.com'
        self._connect()
        self.cursor.execute('INSERT OR REPLACE INTO users (userid, model_list, username, email) VALUES (?, ?, ?, ?)',
                            (userid, model_list, username, email))
        self.conn.commit()
        self._disconnect()

    def record_choice(self, userid, model_list: string):
        self._connect()
        self.cursor.execute(
            'SELECT userid FROM users WHERE userid = ?', (userid,))
        existing_user = self.cursor.fetchone()

        if existing_user:
            self.cursor.execute(
                'UPDATE users SET model_list = ? WHERE userid = ?', (model_list, userid))
            self.conn.commit()
            self._disconnect()
        else:
            self.create_user(userid, model_list)

    def get_choice(self, userid):
        self._connect()
        self.cursor.execute(
            'SELECT model_list FROM users WHERE userid = ?', (userid,))
        choice = self.cursor.fetchone()
        self._disconnect()
        if choice:
            return choice[0]
        else:
            return None

# # 使用示例
# db = UserDatabase()

# # 记录用户的选择
# db.record_choice('user123', 'model1', 'some choice')

# # 获取用户的选择
# choice = db.get_choice('user123')
# print("用户 user123 的选择:", choice)
