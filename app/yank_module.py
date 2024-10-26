from util.spotify import start_token_thread
from util.download import start
import threading
import time

token_thread = threading.Thread(target=start_token_thread, daemon=True)
token_thread.start()
print("Retreiving Spotify token...")
time.sleep(1)
print("Done !")

async def serve_audio(id):
    try:
        filename = await start(id)
        with open(filename, "rb") as f:
            return f.read()
    except:
        return {
            "failed": True,
            "message": "Song not found"
        }, 404