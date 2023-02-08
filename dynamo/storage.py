
class StorageEngine:
  def __init__(self) -> None:
    self.d = {"1": "998", "2": "997"}

  def get(self, key: str) -> str:
    return self.d[key]

