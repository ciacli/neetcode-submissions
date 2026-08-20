class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d.setdefault(key, {})
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        keydict = self.d.get(key, {})
        if not keydict:
            return ""
        for i in range(timestamp, -1, -1):
            val = keydict.get(i, "")
            if val != "":
                return val
        return ""
