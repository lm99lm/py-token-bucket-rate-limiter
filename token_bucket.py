"""Token-bucket rate limiter. Standard library only; clock is injectable."""


class TokenBucket:
    def __init__(self, rate_per_sec, capacity, now):
        self.rate = float(rate_per_sec)
        self.capacity = float(capacity)
        self.tokens = float(capacity)
        self._last = now()
        self._now = now

    def allow(self, cost=1.0):
        t = self._now()
        self.tokens = min(self.capacity, self.tokens + (t - self._last) * self.rate)
        self._last = t
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False
