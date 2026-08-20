class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d.setdefault(key, [])
        self.d[key].append(tuple((timestamp, value)))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.d.get(key, [])
        if not vals:
            return ""
        lb = 0
        ub = len(vals) -1 
        ans = ""
        while lb <= ub:
            mid = (lb + ub) // 2
            time = vals[mid][0]
            if time <= timestamp:
                ans = vals[mid][1]
                lb = mid + 1
            else:
                ub = mid - 1

        return ans
