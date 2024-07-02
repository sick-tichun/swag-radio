import yt_dlp
import os

#format of music_list.txt is $playlist = $playlist_link
# playlist_link is a yt link
def read_sources(file):
    playlists = {}
    with open('music_list.txt', 'r+') as file:
        for line in file:
            if line.startswith('#'):
                continue
            temp = line.split(' = ')
            name = temp[0]
            link = temp[1].strip()
            playlists[name] = link
    return playlists

def download_playlist(name, link):
    ytdl = yt_dlp.YoutubeDL({
        'verbose' : True,
        #'directory_path' : name,
        'extract_audio' : True,
        'embed_thumbnail' : True,
        'embed_metadata' : True,
        'format' : 'bestaudio',
        'audio_format' : 'wav',
        'ignore_errors' : True,
        'download_archive' : 'archive.txt',
        'yes_playlist' : True,
        'no_warnings' : True,
        'geo_bypass' : True,
        'skip_unavailable_fragments' : True
        })
    ytdl.download([link]) 
    return None

def make_m3u(path):
    tracks = []
    out = open('tracklist.m3u', 'w+')
    directory = os.fsencode(path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if not filename.endswith('.txt'):
            tracks.append(filename)
    out.writelines(tracks)
    out.close()

playlists = read_sources('music_list.txt')
#make radio dir if doesent exist already
if not os.path.exists('/srv/radio/stations'):
    os.makedirs('/srv/radio/stations/')
os.chdir('/srv/radio/stations/')
#iterates over 
for name in playlists:
    if not os.path.exists(name):
        os.makedirs(name+'/music')
    os.chdir(name+'/music')
    download_playlist(name, playlists[name])
    os.chdir('..')
    if not os.path.exists('playlists'):
        os.mkdir('playlists')
    os.chdir('playlists')
    make_m3u('../music')
    os.chdir('../..')
    print(os.getcwd())     

