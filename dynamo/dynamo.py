from .storage import StorageEngine

class Dynamo:
  def __init__(self) -> None:
    self.storage_engine = StorageEngine()
  

  def get(self, key) -> str:
    return self.storage_engine.get(key)
