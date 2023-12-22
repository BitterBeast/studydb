from motor.motor_asyncio import AsynIOMotor
from config import config


class Database:
    def _init_(self, uri, database_name):
      self._client = AsyncIOMotor(uri)
      self.db = self._client[database_name]
      self.col = self.db.user



db = Database(config.DB_URL, config.DB_NAME)
