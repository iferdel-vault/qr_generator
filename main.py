from PIL import Image, ImageDraw, ImageFont
import qrcode
import argparse

from utils import wrap_text, calculate_text_height

def generate_qr_code(data, image, label, output):
    qr = qrcode.QRCode(
        version=3,
        box_size=20,
        border=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=(30, 50, 70), back_color="white").convert("RGB")

    if image:
        logo = Image.open(image).resize((225, 225))
        qr_w, qr_h = qr_img.size
        logo_w, logo_h = logo.size
        pos = ((qr_w - logo_w) // 2, (qr_h - logo_h) // 2)
        qr_img.paste(logo, pos, logo)

    if label:
        font = ImageFont.truetype("arial.ttf", 44)
        max_text_width = qr_img.width

        # Create a dummy draw object for measuring text
        dummy_draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
        text_height = calculate_text_height(label, font, dummy_draw, max_text_width)

        new_img_height = qr_img.height + text_height + 20
        new_img = Image.new("RGB", (qr_img.width, new_img_height), "white")

        new_img.paste(qr_img, (0, 0))

        draw = ImageDraw.Draw(new_img)
        wrapped_label = wrap_text(label, font, dummy_draw, max_text_width)  # Pass dummy_draw here
        text_x = 0
        text_y = qr_img.height + 10

        # Center each line of text
        for line in wrapped_label.split('\n'):
            # Calculate the bounding box of the line
            text_bbox = draw.textbbox((0, 0), line, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            line_height = text_bbox[3] - text_bbox[1]

            # Calculate the starting x-coordinate to center the text
            text_x = (qr_img.width - text_width) // 2
            draw.text((text_x, text_y), line, fill="black", font=font)

            # Increment y-coordinate for the next line
            text_y += line_height

        new_img.save(output)
        
    else:
        qr_img.save(output)

def main():
    parser = argparse.ArgumentParser(description='Generate QR code.')
    parser.add_argument('-d', '--data', type=str, help='the data to be encoded in the QR code', required=True)
    parser.add_argument('-i', '--image', type=str, help='the image to be used as logo', required=False)
    parser.add_argument('-l', '--label', type=str, help='the label to be added to the QR code', required=False)
    parser.add_argument('-o', '--output', type=str, help='the filename of the QR code output file', required=True)
    arguments = parser.parse_args()

    generate_qr_code(arguments.data, arguments.image, arguments.label, arguments.output)

if __name__ == "__main__":
    main()
