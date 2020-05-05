
Individual File
```
$ youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=gjQBsCqtfcs

$ youtube-dl -i -f mp4 --yes-playlist 'https://www.youtube.com/watch?v=7Vy8970q0Xc&list=PLwJ2VKmefmxpUJEGB1ff6yUZ5Zd7Gegn2'

```

Alternatively, you can just use the playlist ID:

```
$ youtube-dl -x --audio-format mp3 PLwJ2VKmefmxpUJEGB1ff6yUZ5Zd7Gegn2

//Playlist extractor
$ youtube-dl -x --audio-format mp3 --yes-playlist https://www.youtube.com/watch?v=BX95eMQ5NIw&list=PLN2kbeB23nz7RmZ8UTeaZXkRfGBiERwLT

//Issue
Playlist download works if URL is a playlist page
eg:
$ ./youtube-dl https://www.youtube.com/playlist?list=SOME_PLAYLIST_ID

https://www.youtube.com/playlist?list=PLHLPYS4U6IXTuFWvffzRHYrfS9s5ALPas
```
