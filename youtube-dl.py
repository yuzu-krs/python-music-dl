import os
import yt_dlp

def download_video_as_mp3(url, output_path='downloads'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_videos_from_list(url_list, output_path='downloads'):
    for url in url_list:
        download_video_as_mp3(url, output_path)

if __name__ == "__main__":
    url_list = [


        "https://youtu.be/mLW35YMzELE",


        # 他のURLをここに追加
    ]

    download_videos_from_list(url_list)