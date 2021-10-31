from PIL import Image, ImageDraw, ImageFont
import textwrap
import wikipedia

img_size = (2048, 2048)

img = Image.new('RGBA', img_size, (230,230,230,255))
draw = ImageDraw.Draw(img)

wikipedia.set_lang("en")
res = wikipedia.search("Car")[0]
text = wikipedia.page(res).title
desc_raw = wikipedia.summary(res, sentences=1)

# desc_raw = desc_raw[:desc_raw.find("։") + 1]
text_position = (80, 550)

line_position1 = (80, 800)
line_position2 = (img_size[1] - line_position1[0], line_position1[1])
line_position = line_position1 + line_position2

desc_position = (line_position1[0], line_position1[1] + 50)

desc_raw = textwrap.fill(text=desc_raw, width=35)
desc = desc_raw.split('\n')

text_font = ImageFont.truetype("Mardoto-Bold.ttf", size=210)
desc_font = ImageFont.truetype("Mardoto-Thin.ttf", size=100)

draw.text(text_position, text, font=text_font, fill=(0,0,0,255))
draw.line(line_position, fill=(0,0,0), width=1)
for i in range(len(desc)):
	position = (line_position1[0], line_position1[1] + 50)
	draw.text((80, line_position1[1] + 50 + i*120), desc[i], font=desc_font, fill=(0,0,0,255))



img.save('out.png')