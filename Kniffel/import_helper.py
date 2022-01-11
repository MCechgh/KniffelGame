import base64

def get_dice_pictures():
    with open('dices_as_Base64.txt', 'w') as f:
        for i in range(1, 7):
            imagine = open(f'media/Wuerfelauge_{i}.png', 'rb')
            encoded = base64.b64encode(imagine.read())
            f.write(f"wuerfelauge_{i}={str(encoded)}\n")
        """imagine = open("media/logo/logo_128.png", "rb")
        encoded = base64.b64encode(imagine.read())
        f.write(f"KniffelIco={str(encoded)}\n")"""

get_dice_pictures()