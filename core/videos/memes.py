import numpy as np, disnake, os
from PIL import Image, ImageDraw, ImageOps, ImageFont
from datetime import datetime
from moviepy.editor import ImageClip, AudioFileClip, CompositeAudioClip, concatenate_videoclips, VideoFileClip
from typing import Union
from io import BytesIO

RESOLUTION = (800, 500)

def modify_last_frame(frame, main_text: str, bytes_io: bool = False):
    canvas = Image.new('RGB', RESOLUTION, (0,0,0))
    draw = ImageDraw.Draw(canvas)

    image = Image.fromarray(frame) if not bytes_io else Image.open(frame)

    main_text = main_text.upper()[:30]

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

    text_width = draw.textsize(main_text, font=font)[0]

    draw.text(( round((canvas.width-text_width)/2) , image.height+70 ), main_text, "white", font=font)

    return canvas

def out_of_context(video:Union[BytesIO, str], text:str, is_image:bool=False):
    audio = CompositeAudioClip([ AudioFileClip("assets/media/BeCum.mp3") ])

    if is_image:
        video_clip = ImageClip(np.array(modify_last_frame(video, text, True)))
        video_clip.audio = audio
        video_clip.duration = audio.duration
    
    else:
        filename = video
        video = VideoFileClip(video, target_resolution=(RESOLUTION[1], RESOLUTION[0]))

        frame = video.get_frame(video.duration-0.1)
            
        canvas = modify_last_frame(frame, text)

        video.size = canvas.width, canvas.height

        clip: ImageClip = ImageClip(np.array(canvas)).set_duration(audio.duration)
        clip.audio = audio

        video_clip = concatenate_videoclips([ video, clip ])

    OUT_FILENAME = f"temp/out-{datetime.now().timestamp()}.mp4"

    if not os.path.exists("temp/"):
        os.makedirs("temp/")
    
    video_clip.write_videofile(OUT_FILENAME, logger=None, fps=24)

    file = disnake.File(OUT_FILENAME, "out-of-context.mp4")
    
    def clear():
        try:
            os.remove(OUT_FILENAME)
            os.remove(filename)
        except: pass

    return file, clear

def how(video:Union[BytesIO, str], text:str, is_image:bool=False):
    audio = CompositeAudioClip([ AudioFileClip("assets/media/How.mp3") ])

    if is_image:
        video_clip = ImageClip(np.array(modify_last_frame(video, text, True)))
        video_clip.audio = audio
        video_clip.duration = audio.duration
    
    else:
        filename = video
        video = VideoFileClip(video, target_resolution=(RESOLUTION[1], RESOLUTION[0]))

        frame = video.get_frame(video.duration-0.1)
            
        canvas = modify_last_frame(frame, text)

        clip: ImageClip = ImageClip(np.array(canvas)).set_duration(audio.duration)
        clip.audio = audio

        video_clip = concatenate_videoclips([ video, clip ])

    OUT_FILENAME = f"temp/out-{datetime.now().timestamp()}.mp4"

    if not os.path.exists("temp/"):
        os.makedirs("temp/")
    
    video_clip.write_videofile(OUT_FILENAME, logger=None, fps=24)

    file = disnake.File(OUT_FILENAME, "How.mp4")
    
    def clear():
        try:
            os.remove(OUT_FILENAME)
            os.remove(filename)
        except: pass

    return file, clear