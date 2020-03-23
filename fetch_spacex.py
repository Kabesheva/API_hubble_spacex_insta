from pathlib import Path

import requests
from PIL import Image


def fetch_spacex_last_launch():
    save_dir = Path('images')
    save_dir.mkdir(parents=True, exist_ok=True)
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.post(url)
    response.raise_for_status()
    images_links = response.json()['links']['flickr_images']
    if len(images_links) == 0:
        print('в данный момент в API SpaceX нет фотографий с последнего запуска')
    for image in images_links:
        image_url = Path(image)
        file_path = save_dir / f'spacex_{image_url.parts[-2]}_{image_url.name}'
        response = requests.get(image)
        response.raise_for_status()
        with open(file_path, 'wb') as file:
            file.write(response.content)
        crop_image = square_image(file_path)
        crop_image.save(f'{save_dir}/{file_path.stem}_crop.jpg', 'JPEG')
        file_path.unlink()


def square_image(image):
    image = Image.open(image)
    if not image.mode == 'RGB':
        image = image.convert('RGB')
    xcenter = image.width / 2
    ycenter = image.height / 2
    x1 = xcenter - ycenter
    y1 = ycenter - ycenter
    x2 = xcenter + ycenter
    y2 = ycenter + ycenter
    cropped_image = image.crop((x1, y1, x2, y2))
    cropped_image_resized = cropped_image.resize((1080, 1080))
    return cropped_image_resized


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
