# YouTube Downloader (yt_dlp)

A simple Python script to download YouTube videos or playlists in a selected resolution using [`yt_dlp`](https://github.com/yt-dlp/yt-dlp).

---

## 🚀 Features

- Download **individual videos** or **full playlists**
- Select **maximum resolution** (e.g., 720p, 1080p)
- Automatically organizes downloads into folders
- Uses `yt_dlp` for reliable and fast downloading
- Combines separate video and audio streams using `ffmpeg`

---

## 📁 Project Structure

```
youtube_downloader/
│
├── downloader.py          # Main script
├── requirements.txt       # Dependency list
├── downloads/             # Downloaded videos go here (auto-created)
└── venv/                  # Virtual environment (not included in GitHub)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube_downloader.git
cd youtube_downloader
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### On Windows Git Bash:
```bash
source venv/Scripts/activate
```

#### On Windows CMD:
```cmd
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
python downloader.py
```

You will be prompted to enter:

- A **YouTube URL** (either video or playlist)
- A **maximum resolution** (e.g., `720`, `1080`)

---

## 📦 Output

- Individual videos are saved to:  
  `downloads/Video Title.mkv`

- Playlists are saved to:  
  `downloads/Playlist Title/01 - Video Title.mkv`

---

## 📄 Requirements

- Python 3.7+
- [`yt_dlp`](https://github.com/yt-dlp/yt-dlp)
- [`ffmpeg`](https://ffmpeg.org/) (required to merge audio and video)

---

## 🔧 How to Install `ffmpeg`

### On Windows

1. Download from: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Extract the ZIP file.
3. Copy the path to the `bin/` folder.
4. Add that path to your system **Environment Variables** → `Path`.
5. Verify installation:

```bash
ffmpeg -version
```

### On macOS

```bash
brew install ffmpeg
```

### On Ubuntu/Debian Linux

```bash
sudo apt update
sudo apt install ffmpeg
```

> ⚠️ Without `ffmpeg`, `yt_dlp` cannot combine audio and video streams, and downloads may fail or result in separate files.

---

## 🛑 Notes

- Ensure `ffmpeg` is installed and available in your system path.
- Make sure the `downloads/` folder is writeable.
- Do not use this tool to violate YouTube's Terms of Service.

---

## 🧾 License

This project is licensed under the MIT License.
