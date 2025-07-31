import yt_dlp
import os
import re

def sanitize_filename(name, max_length=50):
    # Remove invalid characters and truncate
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name[:max_length]

def download_video(url, resolution, audio_only=False):
    if audio_only:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': False,
            'socket_timeout': 30,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_opts = {
            'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
            'merge_output_format': 'mkv',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': False,
            'socket_timeout': 30,
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_playlist(url, resolution, folder_name=None, audio_only=False):
    if folder_name:
        folder_name = sanitize_filename(folder_name)
        outtmpl = f'downloads/{folder_name}/%(playlist_index)s - %(title)s.%(ext)s'
    else:
        outtmpl = 'downloads/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s'

    if audio_only:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': outtmpl,
            'quiet': False,
            'socket_timeout': 30,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_opts = {
            'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
            'merge_output_format': 'mkv',
            'outtmpl': outtmpl,
            'quiet': False,
            'socket_timeout': 30,
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    url = input("Enter YouTube video or playlist URL: ").strip()
    audio_choice = input("Download only audio (mp3)? If yes type 'y', if no type 'n' [default: n]: ").strip().lower()
    # Ensure 'downloads' folder exists
    os.makedirs("downloads", exist_ok=True)

    if audio_choice in ['1', 'audio', 'y']:
        audio_only = True
        resolution = None  # Not needed for audio
    else:
        audio_only = False
        resolution = input("Enter max resolution (e.g., 720 or 1080): ").strip()

    if 'playlist' in url.lower():
        folder_name = input("Enter folder name for playlist (leave blank to use playlist name): ").strip()
        download_playlist(url, resolution, folder_name if folder_name else None, audio_only)
    else:
        download_video(url, resolution, audio_only)
