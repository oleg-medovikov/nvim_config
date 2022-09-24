from disp import dp, on_startup
import logging, asyncio

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    try:
        asyncio.run(on_startup(dp))
    except KeyboardInterrupt:
        pass