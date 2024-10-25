import modal
import yank_module
import asyncio

image = (
    modal.Image.debian_slim(python_version="3.10")
    .apt_install("git")
    .run_commands("git clone")
)

app = modal.App(name="spotify-downloader")

@app.function()
@modal.web_endpoint(method = "GET")
def download_title(spotify_id):
    return asyncio.run(yank_module.serve_audio(spotify_id))