# In-memory token-bucket rate limiter

`bucket = TokenBucket(rate=10, capacity=10, clock=time.monotonic)`

This uses only the Python standard library. No Redis. No external dependencies. The main gotcha in ETL pipelines is mocking time during integration tests. Injecting the clock function solves this. You can advance time manually without blocking.

```
token_bucket.py
```
Run the test suite next to the implementation for concrete examples.