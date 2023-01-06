import numpy as np, disnake, os
from PIL import Image, ImageDraw, ImageOps, ImageFont
from datetime import datetime
from moviepy.editor import ImageClip, AudioFileClip, CompositeAudioClip

def out_of_context(image, main:str):
    canvas = Image.new('RGB', (800, 500), (0,0,0))
    draw = ImageDraw.Draw(canvas)

    image = Image.open(image)

    main = main.upper()[:30]

    aspect_ratio = image.width / image.height # > 1
    SIZE = 300

    image = image.resize((round(aspect_ratio*SIZE), SIZE))
    image = ImageOps.fit(image, (min(canvas.width-40, image.width), SIZE), centering=(.5,.5))

    X, Y = round((canvas.width - image.width) / 2), 50

    draw.rectangle(
        (X-10, Y-10, X+image.width+10, Y+image.height+10),
        (255,255,255)
    )

    draw.rectangle(
        (X-5, Y-5, X+image.width+5, Y+image.height+5),
        (0,0,0)
    )
    
    canvas.paste(
        image,
        ( X, Y )
    )

    font = ImageFont.truetype("assets/fonts/Sharp.ttf", size=50)

    text_width = draw.textsize(main, font=font)[0]

    draw.text(( round((canvas.width-text_width)/2) , image.height+70 ), main, "white", font=font)

    audio = CompositeAudioClip([ AudioFileClip("assets/media/BeCum.mp3") ])
    video: ImageClip = ImageClip(np.array(canvas))
    video = video.set_duration(audio.duration)
    video = video.set_fps(10)
    video.audio = audio

    OUT_FILENAME = f"temp/out-{datetime.now().timestamp()}.mp4"

    if not os.path.exists("temp/"):
        os.makedirs("temp/")
    
    video.write_videofile(OUT_FILENAME, logger=None)

    file = disnake.File(OUT_FILENAME, "out-of-context.mp4")
    
    def clear():
        try:
            os.remove(OUT_FILENAME)
        except: pass

    return file, clear