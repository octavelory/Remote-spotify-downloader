import modal
import yank_module as yank_module
import asyncio

image = (
    modal.Image.debian_slim(python_version="3.10")
    .apt_install("git")
    .run_commands("git clone https://github.com/octavelory/Remote-spotify-downloader")
    .run_commands("mv Remote-spotify-downloader Remote_spotify_downloader")
    .run_commands("pip install -r Remote-spotify-downloader/requirements.txt")
)

app = modal.App(name="spotify-downloader")

@app.function(image = image)
@modal.web_endpoint(method = "GET")
def download_title(spotify_id):
    return asyncio.run(yank_module.serve_audio(spotify_id))