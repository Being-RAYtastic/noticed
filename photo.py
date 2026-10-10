from PIL import Image, ImageOps

def save_clean_photo(file, destination):
    img = Image.open(file)
    img = ImageOps.exif_transpose(img).convert("RGB")

    img.thumbnail((2560, 2560))
    img.save(destination, "JPEG", quality=85)
    r, g, b = img.resize((1, 1)).getpixel((0, 0))

    return f"#{r:02x}{g:02x}{b:02x}"

if __name__ == "__main__":
    print(save_clean_photo("test.jpg", "clean.jpg"))