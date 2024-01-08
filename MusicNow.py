class Manager:
    from pytube import YouTube
    import requests

    embedd_image = False

    def __init__(self,UID):
        self.UID = UID

    # Download YouTube thumbnail from URL
    def __downloadImage(self,url):
        id = self.__getVideoId(url)
        jpg_url = "https://img.youtube.com/vi/"+id+"/maxresdefault.jpg"
        data = self.requests.get(jpg_url).content
        f = open("img.jpg","wb")
        f.write(data)
        f.close()

    # Extract YouTube video ID from URL
    def __getVideoId(self,url):
        query_start = '?v='
        query_end = '&'
        id = url[url.find(query_start)+len(query_start):url.index(query_end)]
        return id
    
    # Download YouTube audio contents, convert to mp3 and embed meta-data
    def download(self,url):
        self.YouTube(url).streams.get_audio_only().download()
        if self.embedd_image:
            self.__downloadImage(url)
