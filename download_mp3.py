import os
import yt_dlp

# Dossier pour enregistrer les MP3
output_folder = os.path.join(os.path.expanduser("~"), "Music", "mp3_youtube")
os.makedirs(output_folder, exist_ok=True)

def download_mp3(url, output_path=output_folder):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    # Lecture du fichier urls.txt
    if os.path.exists("urls.txt"):
        with open("urls.txt", "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]

        for url in urls:
            print(f"🎶 Téléchargement : {url}")
            try:
                download_mp3(url)
            except Exception as e:
                print(f"❌ Erreur avec {url} : {e}")
    else:
        print("⚠️ Fichier urls.txt introuvable !")
