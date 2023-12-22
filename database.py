from motor.motor_asyncio import AsynIOMotor

class Database:
    def _init_(self, uri, database):
      self._client = AsyncIOMotor(uri)
      self.db = self._client[database_name]
      self.col = self.db.user
