import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import qrcode
import os

csv_path = r'C:\Users\Rishabh Prashar\Desktop\cert gen\Book1.csv'
template_path = r'C:\Users\Rishabh Prashar\Desktop\cert gen\template_certificate.jpg'
output_dir = r'C:\Users\Rishabh Prashar\Desktop\cert gen\output'
droid_serif_path = r'C:\Users\Rishabh Prashar\Desktop\cert gen\DroidSerif-Regular.ttf'
great_vibes_path = r'C:\Users\Rishabh Prashar\Desktop\cert gen\GreatVibes-Regular.ttf'
poppins_italic_path = r'C:\Users\Rishabh Prashar\Desktop\cert gen\Poppins-MediumItalic.ttf'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

data = pd.read_csv(csv_path)
print("Column names in the CSV file:", data.columns.tolist())

certificate_template = Image.open(template_path)
font_type = ImageFont.truetype(droid_serif_path, 32)
font_name = ImageFont.truetype(great_vibes_path, 90)
font_achievement = ImageFont.truetype(poppins_italic_path, 16)

color_type = "#FFFFFF"
color_name = "#C5982C"
color_achievement = "#000000"

name_position = (750, 400)
event_position = (440, 600)
regno_position = (900, 510)
type_position = (750, 240)
achievement_text_position = (700, 550)
qr_code_position = (415, 630)

for _, row in data.iterrows():
    name = row['Name']
    event = row['Event']
    regno = row['Registration Number']
    cert_type = row['certification type']

    if cert_type.lower() in ['1st place', '2nd place', '3rd place']:
        certificate_type_text = "OF APPRECIATION"
        achievement_text = f"""       for securing {cert_type} in the {event}
        held by the AI Club of VIT Chennai held on xxxx."""
    else:
        certificate_type_text = "OF PARTICIPATION"
        achievement_text = f"""       for participating in the {event}
        held by the AI Club of VIT Chennai on xxxx."""

    fn = name.replace(' ', '_')
    print(f"Generating certificate for: {fn}")
    filename = f"{fn}_certificate.png"
    cert_url = f"https://aiclubvitc.in/certificates/{filename}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(cert_url)
    qr.make(fit=True)

    qr_code_image = qr.make_image(fill_color="black", back_color="white")
    qr_code_image = qr_code_image.resize((150, 150))

    certificate = certificate_template.copy()
    draw = ImageDraw.Draw(certificate)

    draw.text(name_position, name, fill=color_name, font=font_name)
    draw.text(regno_position, regno, fill=color_achievement, font=font_achievement)
    draw.text(type_position, certificate_type_text, fill=color_type, font=font_type)
    draw.text(achievement_text_position, achievement_text, fill=color_achievement, font=font_achievement)

    certificate.paste(qr_code_image, qr_code_position)
    certificate.save(os.path.join(output_dir, filename))

print("Certificates generated successfully.")
