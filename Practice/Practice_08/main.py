import pytube as pt

path = r'C:\Users\nekit\Desktop\GB\Python\GB_Python\Practice\Practice_08'
link = 'https://www.youtube.com/watch?v=Q3oItpVa9fs'
name = 'test video download'
yt = pt.YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4')
yt.streams.order_by('resolution')
yt.streams.desc()
yt.streams.first().download(path)