from token_bucket import TokenBucket


def test_refills_over_time():
    clock = [0.0]
    tb = TokenBucket(rate_per_sec=1, capacity=1, now=lambda: clock[0])
    assert tb.allow()
    assert not tb.allow()
    clock[0] = 1.0
    assert tb.allow()
