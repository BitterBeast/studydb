from motor.motor_asyncio import AsynIOMotor
from config import *


class Database:
    def _init_(self, uri, database_name):
      self._client = AsyncIOMotor(uri)
      self.db = self._client[database_name]
      self.col = self.db.user

    def new_user(self, id):
        dict(
            _id=id,
            file_id=none,
            caption=none
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = self.col.find_one({'_id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'_id': int(user_id)})
        

db = Database(DB_URL, DB_NAME)
