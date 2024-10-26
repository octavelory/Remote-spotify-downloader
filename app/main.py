from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
import threading
import time

from app.util.spotify import start_token_thread
from app.util.download import start

app = FastAPI()

# Start the Spotify token retrieval thread
def initiate_token_thread():
    token_thread = threading.Thread(target=start_token_thread, daemon=True)
    token_thread.start()
    print("Retrieving Spotify token...")
    time.sleep(1)  # Adjust sleep time as necessary
    print("Token retrieval initiated.")

initiate_token_thread()

@app.get("/audio/{id}", response_class=Response)
async def serve_audio(id: str):
    try:
        filename = await start(id)
        return FileResponse(filename, media_type='audio/mpeg', filename=filename)
    except Exception as e:
        # Log the exception details if needed
        print(f"Error serving audio for ID {id}: {e}")
        raise HTTPException(status_code=404, detail="Song not found")
