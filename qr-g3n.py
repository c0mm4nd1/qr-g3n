import requests
import qrcode
from PIL import Image
from colorama import init, Fore, Style

init(autoreset=True)

def show_banner():
    print(Fore.CYAN + Style.BRIGHT + """

                                                                            

 .88888.    888888ba                    d8888b.          
d8'   `8b   88    `8b                       `88          
88     88  a88aaaa8P'          .d8888b.  aaad8' 88d888b. 
88  db 88   88   `8b. 88888888 88'  `88     `88 88'  `88 
Y8.  Y88P   88     88          88.  .88     .88 88    88 
 `8888PY8b  dP     dP          `8888P88 d88888P dP    dP 
oooooooooooooooooooooooooooooooo~~~~.88~ooooooooooooooooo
                                d8888P                   
                       
                                       
""" + Fore.GREEN + Style.BRIGHT + "         For Red Teamers\n")

def shorten_url_with_bitly(long_url, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "long_url": long_url
    }
    try:
        response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=data, headers=headers)
        if response.status_code == 200:
            return response.json()["link"]
        else:
            print(Fore.RED + f"❌ Bitly error: {response.text}")
            return None
    except Exception as e:
        print(Fore.RED + f"❌ Bitly exception: {e}")
        return None

def generate_qr_with_logo(url, logo_path, output_file="qr-code.png"):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    try:
        logo = Image.open(logo_path)
    except FileNotFoundError:
        print(Fore.RED + f"Logo not found: {logo_path}")
        return

    qr_width, qr_height = qr_img.size
    logo_size = qr_width // 4
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
    qr_img.save(output_file)
    print(Fore.GREEN + f"\n✅ QR code saved as: {output_file}")

if __name__ == "__main__":
    show_banner()

    url = input(Fore.YELLOW + "🔗 Enter the original URL: ").strip()
    use_bitly = input(Fore.CYAN + "Do you want to shorten the URL using Bitly? (Y/n) [default: n]: ").strip().lower()

    if use_bitly == "y":
        bitly_token = input(Fore.YELLOW + "🔑 Enter your Bitly token: ").strip()
        shortened_url = shorten_url_with_bitly(url, bitly_token)
        if shortened_url:
            print(Fore.BLUE + f"🔗 Shortened URL: {shortened_url}")
            print(Fore.MAGENTA + f"📊 Stats: {shortened_url}+")
            url = shortened_url
        else:
            print(Fore.RED + "⚠️ Failed to shorten the URL. Using original.")

    logo_path = input(Fore.YELLOW + "🖼️ Logo path (PNG/JPG): ").strip()
    output_name = input(Fore.YELLOW + "💾 Output filename [default: qr-code.png]: ").strip()
    if not output_name:
        output_name = "qr-code.png"

    generate_qr_with_logo(url, logo_path, output_name)
