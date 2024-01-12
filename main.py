from PIL import Image, ImageDraw
import qrcode
import argparse
 
def generate_qr_code(data, image, label, output):
    qr = qrcode.QRCode(version=3,
                       box_size=20,
                       border=10,
                       error_correction=qrcode.constants.ERROR_CORRECT_H)
 
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=(30, 50, 70), back_color="white")
 
    if image:
        logo = Image.open(image).resize((250,250))
        qr_w, qr_h = qr_img.size
        logo_w, logo_h = logo.size
        pos = ((qr_w - logo_w) // 2, (qr_h - logo_h) // 2)
        qr_img.paste(logo, pos, logo)
    
    qr_img.save(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate QR code.')
    parser.add_argument('-d', '--data', type=str, help='the data to be encoded in the QR code', required=True)
    parser.add_argument('-i', '--image', type=str, help='the image to be used as logo', required=False)
    parser.add_argument('-l', '--label', type=str, help='the label to be added to the QR code', required=False)
    parser.add_argument('-o', '--output', type=str, help='the filename of the QR code output file', required=True)
    arguments = parser.parse_args()
 
    generate_qr_code(arguments.data, arguments.image, arguments.label, arguments.output)
