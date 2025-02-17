import time
from RateLimiter import RateLimiter
rate_limiter = RateLimiter(6,10)

for i in range(10):
    if rate_limiter.allow_request():
        print(True,end=' ')
        # time.sleep(1)
    else:
        print(False,end=' ')
        # time.sleep(1)