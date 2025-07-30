import yt_dlp
import os

def download_video(url, resolution):
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


def download_playlist(url, resolution):
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'merge_output_format': 'mkv',
        'outtmpl': 'downloads/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
        'quiet': False,
        'socket_timeout': 30,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    url = input("Enter YouTube video or playlist URL: ").strip()
    resolution = input("Enter max resolution (e.g., 720 or 1080): ").strip()

    # Ensure 'downloads' folder exists
    os.makedirs("downloads", exist_ok=True)

    if 'playlist' in url.lower():
        download_playlist(url, resolution)
    else:
        download_video(url, resolution)
