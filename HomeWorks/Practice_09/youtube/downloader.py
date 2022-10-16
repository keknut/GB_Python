import pytube as pt

def download(link, path):
    yt = pt.YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4')
    yt.streams.order_by('resolution')
    yt.streams.desc()
    yt.streams.get_highest_resolution().download(path)