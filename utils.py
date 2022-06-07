from pytube import Playlist, YouTube
from moviepy.editor import VideoFileClip
import os

def download(youtube_urls, mp3_path ='songs_mp3', mp4_path ='songs_mp4'):
    '''download a bunch of tracks into mp3 & mp4 folders;
    if they don't exist, create them automatically'''
    if mp4_path not in os.listdir(): os.mkdir(mp4_path)
    if mp3_path not in os.listdir(): os.mkdir(mp3_path)

    video = YouTube(youtube_urls)
    video = video.streams.get_highest_resolution()
    mp4_name = os.path.join(mp4_path, video.default_filename)
    mp3_name = os.path.join(mp3_path, os.path.splitext(video.default_filename)[0]+'.mp3')
    video.download(mp4_path)
    print('MP4 done:', mp4_name)
    VideoFileClip(mp4_name).audio.write_audiofile(mp3_name)
    print('MP3 done:', mp3_name)

def playlist_to_songs(playlist_url):
    '''Print urls included in a playlist'''
    playlist = Playlist(playlist_url)
    plain_text = ',\n'.join([f"'{n}'" for n in playlist.video_urls])
    print('Playlist:', playlist.title)
    print('Songs:', len(playlist.video_urls))
    print(f"[{plain_text}]")

def instant_download(youtube_url):
    '''Download a single song in a current location
    e.g. this movie: https://www.youtube.com/watch?v=ZhwK9dP3MJ8'''
    YouTube(youtube_url).streams.get_highest_resolution().download()