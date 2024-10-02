import pandas as pd
from PIL import Image, ImageDraw, ImageFont

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

csv_path = r'C:\Users\Rishabh Prashar\Desktop\cert gen\book1.csv'
template_path = r'C:\Users\Rishabh Prashar\Desktop\cert gen\template_certificate.jpg'
output_dir = r'C:\Users\Rishabh Prashar\Desktop\cert gen\output'
font = r'C:\Users\Rishabh Prashar\Desktop\cert gen\Poppins-MediumItalic.ttf'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

data = pd.read_csv(csv_path)
certificate_template = Image.open(template_path)
font_name = ImageFont.truetype(font, 64)
color_name = "#475dff"

W, H = certificate_template.size

for _, row in data.iterrows():
    name = row['Name']
    fn = name.replace(' ', '_')
    filename = f"{fn}_certificate.png"
    
    certificate = certificate_template.copy()
    draw = ImageDraw.Draw(certificate)

    w, h = draw.textbbox((0, 0), name, font=font_name)[2:]
    draw.text(((W - w) / 2, 620), name, font=font_name, fill=color_name)

    certificate.save(os.path.join(output_dir, filename))

print("Certificates generated successfully.")


data = pd.read_csv(csv_path)
certificate_template = Image.open(template_path)
font_name = ImageFont.truetype(font, 64)
color_name = "#475dff"
for _, row in data.iterrows():
	name = row['Name']
	namelen = len(name)	

	W, H = (2000,1414)

	fn = name.replace(' ', '_')
	print(fn)
	filename = f"{fn}_certificate.png"
	
	certificate = certificate_template.copy()
	draw = ImageDraw.Draw(certificate)
	w, h = draw.textsize(name)
	_, _, w, h = draw.textbbox((0, 0), name, font=font_name)
	draw.text(((W-w)/2, 620), name, font=font_name, fill=color_name)

	certificate.save(f'{output_dir}/{fn}_certificate.png')
