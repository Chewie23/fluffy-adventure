import webbrowser

def loop_youtube_vid(VIDEO_ID):
    """
    This opens up a browswer to Youtube, and loops a video by creating a playlist, and looping it ad nauseum
    Need the Video ID of video for parameter.
    FYI: Some videos don't allow playback.
    General Format to loop: 
    'https://www.youtube.com/v/VIDEO_ID?version=1&autoplay=1&loop=1&playlist=VIDEO_ID'
    """

    BASE = 'https://www.youtube.com/v/'
    LOOP = '?version=3&autoplay=1&loop=1&playlist='
    URL  = BASE + VIDEO_ID + LOOP + VIDEO_ID

    webbrowser.open_new(URL)

VIDEO_ID = '_gxLms9eBKk' #Av.i - Bluebird
loop_youtube_vid(VIDEO_ID)