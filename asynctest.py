import asyncio

async def delayed_hi(seconds: int):
    await asyncio.sleep(seconds)
    print(f"Hi after {seconds}")

async def delayed_hi_2(seconds: int):
    await asyncio.sleep(seconds)
    print(f"Hi after {seconds}")

async def main():
    await asyncio.gather(
        delayed_hi(1),
        delayed_hi(5),
        delayed_hi(3),
        delayed_hi_2(4),
    )

asyncio.run(main())