from fastapi import FastAPI, HTTPException, Response
import threading
import time
from util.spotify import start_token_thread
from util.download import start

app = FastAPI()

# Start the Spotify token retrieval thread
def initiate_token_thread():
    token_thread = threading.Thread(target=start_token_thread, daemon=True)
    token_thread.start()
    print("Retrieving Spotify token...")
    time.sleep(1)
    print("Token retrieval initiated.")

initiate_token_thread()

@app.get("/audio/{id}", response_class=Response)
async def serve_audio(id: str):
    try:
        filename = await start(id)
        print(filename)
        with open(filename, "rb") as file:
            contents = file.read()
        return Response(content=contents, media_type="audio/mpeg")
    except Exception as e:
        # Log the exception details if needed
        print(f"Error serving audio for ID {id}: {e}")
        raise HTTPException(status_code=404, detail="Song not found")
