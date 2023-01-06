from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap, requests
import disnake

from io import BytesIO

def megamind(text):
    text = text.upper()
    canvas = Image.open("assets/MemeTemplates/megamind.png")

    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("assets/fonts/impact.ttf", size=70)
    
    canvas_width = canvas.width

    wrapped = textwrap.wrap(text, 20, break_long_words=True, max_lines=2, placeholder="")

    for (index, line) in enumerate(wrapped):
        textW, textH = draw.textsize(line, font=font)

        draw.text(
            ( (canvas_width-textW)/2, 10+(textH+2)*index ),
            line.strip(),
            fill="white",
            stroke_fill="black",
            stroke_width=2,
            font=font
        )


    img = BytesIO()
    canvas.save(img, 'PNG')
    img.seek(0)

    return disnake.File(img, filename="megamind.png")

def worldwide(name, avatar):
    name = name[:8]

    canvas = Image.new('RGB', (210, 232), (255,255,255))

    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("assets/fonts/Poppins.ttf", size=13)

    avatar = Image.open(BytesIO(requests.get(avatar).content))
    
    normal = ImageOps.fit(avatar, (103, 103), centering=(.5, .5))

    stretch = 3

    avatar_width, avatar_height = avatar.size
    left_margin = 100

    #wide = avatar.resize((avatar.width+STRENGTH, avatar.height-STRENGTH))
    wide = avatar.resize((round(avatar_width*stretch), avatar_height))
    wide = ImageOps.fit(wide, (103, 103), centering=(.5,.5))

    canvas.paste(normal, (100, 9))
    canvas.paste(wide, (100, 120))

    normal_width = draw.textsize(name, font=font)[0]

    draw.text(
        ( (left_margin-normal_width)/2, 50 ),
        name,
        font=font,
        fill="black"
    )

    wide_width = draw.textsize(f"{name} Wide", font=font)[0]

    draw.text(
        ( (left_margin-wide_width)/2, 150 ),
        f"{name} Wide",
        font=font,
        fill="black"
    )

    img = BytesIO()
    canvas.save(img, 'PNG')
    img.seek(0)

    return disnake.File(img, filename="worldwide.png")

def fate(string, scissors, other):

    canvas = Image.open("assets/MemeTemplates/fate.png")

    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("assets/fonts/impact.ttf", size=40)

    X_MARGIN, Y_MARGIN = 310, 230

    string_lines = textwrap.wrap(string, 20, break_long_words=True, break_on_hyphens=True, max_lines=3, placeholder="")

    for (index, line) in enumerate(string_lines):
        line_size = draw.textsize(line, font=font)
        draw.text(
        ((X_MARGIN-line_size[0])/2+X_MARGIN, (Y_MARGIN-line_size[1])/2+Y_MARGIN+40*index),
        line,
        font=font
    )

    X_MARGIN, Y_MARGIN = 500, 400

    scissor_lines = textwrap.wrap(scissors, 20, break_long_words=True, break_on_hyphens=True, max_lines=3, placeholder="")

    for (index, line) in enumerate(scissor_lines):
        line_size = draw.textsize(line, font=font)
        draw.text(
        ((X_MARGIN-line_size[0])/2+X_MARGIN, (Y_MARGIN-line_size[1])/2+Y_MARGIN+40*index),
        line,
        font=font
    )

    X_MARGIN, Y_MARGIN = 640, 100

    other_lines = textwrap.wrap(other, 20, break_long_words=True, break_on_hyphens=True, max_lines=3, placeholder="")

    for (index, line) in enumerate(other_lines):
        line_size = draw.textsize(line, font=font)
        draw.text(
        ((X_MARGIN-line_size[0])/2+X_MARGIN, (Y_MARGIN-line_size[1])/2+Y_MARGIN+40*index),
        line,
        font=font
    )

    img = BytesIO()
    canvas.save(img, 'PNG')
    img.seek(0)

    return disnake.File(img, filename="fate.png")

def wtfdidyoujustdo(image_url, AMOUNT, DURATION):
    canvas = Image.open(BytesIO(requests.get(image_url).content))

    question = Image.open("assets/MemeTemplates/lolWhat.png")

    DELAY = 5
    SPAN = 2

    images = [canvas for _ in range(DELAY)]

    MARGIN_X, MARGIN_Y = round((canvas.width-question.width)/2), round((canvas.height-question.height)/2)

    for _ in range(AMOUNT):
        canv = canvas.copy()
        VAL = 200
        OFFSET_X, OFFSET_Y = randint(-VAL,VAL), randint(-VAL,VAL)
        q_img = question.copy().rotate(randint(-80, 80))
        canvas.paste(q_img, (MARGIN_X+OFFSET_X, MARGIN_Y+OFFSET_Y), q_img)
        images += [canv for _ in range(SPAN)]

    img = BytesIO()
    canvas.save(img, format="GIF", save_all=True, append_images=images, loop=0, duration=DURATION)
    img.seek(0)

    file = disnake.File(img, filename="whatDidYouJustDo.gif")
    
    return file

def obama(receiver, giver):
    receiver = receiver[:30]
    giver = giver[:30]

    canvas = Image.open("assets/MemeTemplates/Obama.jpg")
    draw = ImageDraw.Draw(canvas)

    font = ImageFont.truetype("assets/fonts/DiscordBold.otf", size=40)

    canvas_width, canvas_height = 100, 100

    giver_width, giver_height = draw.textsize(giver, font, stroke_width=2)

    draw.text(
        (  770 + (canvas_width-giver_width)/2  ,  30 + (canvas_height-giver_height)/2  ),
        giver,
        font=font,
        stroke_fill="black",
        stroke_width=2
    )

    receiver_width, receiver_height = draw.textsize(receiver, font, stroke_width=2)

    draw.text(
        (  420 + (canvas_width-receiver_width)/2  ,  400 + (canvas_height-receiver_height)/2  ),
        receiver,
        font=font,
        stroke_fill="black",
        stroke_width=2
    )

    img = BytesIO()

    canvas.save(img, format="PNG")
    img.seek(0)

    return disnake.File(img, filename="obama.png")

def monke(ein, zwei, drei_name, drei_text):

    canvas = Image.open("assets/MemeTemplates/Monke.png")
    draw = ImageDraw.Draw(canvas)

    font = ImageFont.truetype("assets/fonts/DiscordBold.otf", size=40)

    canvas_width, canvas_height = 100, 100

    lines = textwrap.wrap(ein, 10, max_lines=3, placeholder="", break_long_words=True, break_on_hyphens=True)

    for (index, line) in enumerate(lines):
        text_width, text_height = draw.textsize(line, font, stroke_width=2)

        draw.text(
            ( 100 + (canvas_width-text_width)/2 , 250 + (canvas_height-text_height)/2 + (font.size+5)*index ),
            line,
            font=font,
            stroke_fill="black",
            stroke_width=2
        )

    lines = textwrap.wrap(zwei, 10, max_lines=3, placeholder="", break_long_words=True, break_on_hyphens=True)

    for (index, line) in enumerate(lines):
        text_width, text_height = draw.textsize(line, font, stroke_width=2)

        draw.text(
            ( 380 + (canvas_width-text_width)/2 , 220 + (canvas_height-text_height)/2 + (font.size+5)*index ),
            line,
            font=font,
            stroke_fill="black",
            stroke_width=2
        )

    lines = textwrap.wrap(drei_name, 20, max_lines=2, placeholder="", break_long_words=True, break_on_hyphens=True)

    for (index, line) in enumerate(lines):
        text_width, text_height = draw.textsize(line, font, stroke_width=2)

        draw.text(
            ( 760 + (canvas_width-text_width)/2 , 30 + (canvas_height-text_height)/2 + (font.size+5)*index ),
            line,
            font=font,
            stroke_fill="black",
            stroke_width=2
        )

    lines = textwrap.wrap(drei_text, 20, max_lines=3, placeholder="", break_long_words=True, break_on_hyphens=True)

    for (index, line) in enumerate(lines):
        text_width, text_height = draw.textsize(line, font, stroke_width=2)

        draw.text(
            ( 760 + (canvas_width-text_width)/2 , 220 + (canvas_height-text_height)/2 + (font.size+5)*index ),
            line,
            font=font,
            stroke_fill="black",
            stroke_width=2
        )

    img = BytesIO()

    canvas.save(img, format="PNG")
    img.seek(0)

    return disnake.File(img, filename="monke.png")

def stats(stat: str):
    stat = stat.upper()

    canvas = Image.open("assets/MemeTemplates/Stats.png")
    draw = ImageDraw.Draw(canvas)

    font = ImageFont.truetype("assets/fonts/DiscordText.otf", size=50)

    img = BytesIO()

    lines = textwrap.wrap(stat, 10, break_long_words=True, break_on_hyphens=True, placeholder="", max_lines=3)

    canvas_width, canvas_height = 70, 100

    for (index, line) in enumerate(lines):
        text_width, text_height = draw.textsize(line, font)

        draw.text(
            (120 + (canvas_width-text_width)/2, canvas.height-165-20*(len(lines)-1) + (canvas_height-text_height)/2 + (font.size+2)*index),
            line,
            fill="black",
            font=font
        )


    canvas.save(img, format="PNG")
    img.seek(0)

    return disnake.File(img, filename="monke.png")

def what(image, main:str, sub=""):
    canvas = Image.new('RGB', (800, 500), (0,0,0))
    draw = ImageDraw.Draw(canvas)

    image = Image.open(image)

    main = main.upper()[:30]
    sub = sub[:30]

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

    font = ImageFont.truetype("assets/fonts/Sharp.ttf", size=40)

    text_width = draw.textsize(sub, font=font)[0]

    draw.text(( round((canvas.width-text_width)/2) , image.height+130 ), sub, "white", font=font)

    img = BytesIO()

    canvas.save(img, format="PNG")
    img.seek(0)

    return disnake.File(img, filename="what.png")

def we_are_not_the_same(top_text, bottom_text):
    canvas = Image.open('assets/MemeTemplates/WeAreNotTheSame.jpg')

    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("assets/fonts/DiscordBold.otf", size=80)
    text_width, _ = draw.multiline_textsize(f"{top_text}\n\n\n{bottom_text}", font=font)

    draw.multiline_text(((canvas.width-text_width)/2, 600), f"{top_text}\n\n\n{bottom_text}", font=font, align="center")

    text_width, text_height = draw.textsize("We are not the same", font=font)
    draw.text(((canvas.width-text_width)/2 ,canvas.height-text_height-40), "We are not the same", font=font)

    img = BytesIO()
    canvas.save(img, "PNG")
    img.seek(0)

    return disnake.File(img, filename="we_are_not_the_same.png")

def stuff_admini(text: str):
    canvas = Image.open('assets/MemeTemplates/Stuff.png')
    text = text.upper()

    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("assets/fonts/impact.ttf", size=70)
    lines = textwrap.wrap(text, 7)
    text = '\n'.join(lines)
    text_width, text_height = draw.multiline_textsize(text, font=font)

    draw.multiline_text((270+(canvas.width-text_width)/2, 100), text, font=font, align="center", fill="black")

    img = BytesIO()
    canvas.save(img, "PNG")
    img.seek(0)

    return disnake.File(img, filename="admini.png")

def communist(image: BytesIO):
    overlay_image = Image.open("assets/MemeTemplates/Communist.jpg")
    canvas = Image.open(image).convert('RGBA').resize(overlay_image.size)

    overlay_image.putalpha(130)
    canvas.paste(overlay_image, (0,0), mask=overlay_image)

    img = BytesIO()
    canvas.save(img, "PNG")
    img.seek(0)

    return disnake.File(img, "our.png")

def insanity(image: BytesIO, text: str = "A common example of insanity."):
    canvas = Image.open("assets/MemeTemplates/Insanity.png")

    image = Image.open(image).resize((300, 265))
    canvas.paste(image, (407,307))

    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("assets/fonts/Arial.ttf", size=12)

    text = textwrap.wrap(text.strip(), 50)[:2]
    draw.multiline_text((410, 580), '\n'.join(text), "black", font=font)

    img = BytesIO()
    canvas.save(img, "PNG")
    img.seek(0)

    return disnake.File(img, "insanity.png")

def thing_at_home(image: BytesIO, thing: str = "BTB"):
    canvas = Image.new('RGB', (900, 900), (255,255,255))

    font = ImageFont.truetype("assets/fonts/Arial.ttf", size=40)

    thing = thing[:80]

    me_text = textwrap.wrap(f"me: can we stop and get some {thing}?", width=40)
    mom_text = textwrap.wrap(f"mom: we have {thing} at home.", width=40)
    at_home_text = textwrap.wrap(f"{thing} at home:", width=40)

    MOM_TOP_MARGIN = (font.size*len(me_text))-20
    AT_HOME_TOP_MARGIN = MOM_TOP_MARGIN+(font.size*len(mom_text))+20
    IMAGE_HEIGHT_MARGIN = font.size+(font.size*(len(mom_text)+len(me_text)+len(at_home_text)))+20

    draw = ImageDraw.Draw(canvas)

    draw.multiline_text((10, 10), '\n'.join(me_text), "black", font=font)
    draw.multiline_text((10, font.size+MOM_TOP_MARGIN), '\n'.join(mom_text), "black", font=font)

    draw.text((10, font.size+AT_HOME_TOP_MARGIN), '\n'.join(at_home_text), "black", font=font)

    image: Image.Image = Image.open(image).resize((canvas.width, canvas.height-IMAGE_HEIGHT_MARGIN))
    canvas.paste(image, (0, IMAGE_HEIGHT_MARGIN))

    img = BytesIO()
    canvas.save(img, "PNG")
    img.seek(0)

    return disnake.File(img, f"{thing.encode('utf-8')}-at-home.png")

def mass(text: str):
    canvas = Image.open("assets/MemeTemplates/Mass.png")
    text = text[:20]

    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("assets/fonts/DiscordBold.otf", size=20)
    text_width = draw.textsize(text, font=font)[0]


    LEFT_MARGIN = 410

    draw.text((LEFT_MARGIN+round((canvas.width-LEFT_MARGIN-text_width)/2), 15), text, "black", font=font, stroke_fill="black")
    
    img = BytesIO()
    canvas.save(img, "PNG")
    img.seek(0)

    return disnake.File(img, "humongus.png")

def jason(topic: str, description: str):
    canvas = Image.open("assets/MemeTemplates/Jason.png")

    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("assets/fonts/DiscordBold.otf", size=40)

    ROTATION = 15

    topic = textwrap.wrap(topic, 20, max_lines=3)
    description = textwrap.wrap(description, 30, max_lines=2, placeholder="    ")


    text_container = Image.new('RGBA', canvas.size, (0,0,0,0))
    text_draw = ImageDraw.Draw(text_container)
    text_draw.multiline_text((220, 750, 0), '\n'.join(topic), "black", font=font, align='center')

    canvas_over = canvas.rotate(ROTATION)
    canvas_over.paste(text_container, (0, 0), mask=text_container)
    canvas_over = canvas_over.rotate(-ROTATION)
    canvas.paste(canvas_over, (0, 0), mask=canvas_over)

    draw.text((600, 630), '\n'.join(description), "black", font=font)

    img = BytesIO()
    canvas.save(img, "PNG")
    img.seek(0)

    return disnake.File(img, "jason.png")