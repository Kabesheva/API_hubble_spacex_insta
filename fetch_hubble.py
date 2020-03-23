import argparse
from pathlib import Path

import requests
from PIL import Image


def hubble_image(image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url)
    response.raise_for_status()
    hubble_image_file = response.json()['image_files'][-1]['file_url']
    full_file_url = f'https:{hubble_image_file}'
    file_extension = full_file_url.split('.')[-1]
    image_name = (f'hubble_{image_id}.' + file_extension)
    save_dir = Path('images')
    save_dir.mkdir(parents=True, exist_ok=True)
    file_path = save_dir / image_name
    response = requests.get(full_file_url, verify=False)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
    crop_image = square_image(file_path)
    crop_image.save(f'{save_dir}/hubble_{image_id}_crop.jpg', 'JPEG')
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


def hubble_collection(collection_name):
    url = f"http://hubblesite.org/api/v3/images/{collection_name}"
    response = requests.get(url)
    response.raise_for_status()
    collection_images = response.json()
    for i in collection_images:
        image_id = i['id']
        hubble_image(image_id)


def main():
    collection = argparse.ArgumentParser(description="фото с телескопа Hubble")
    collection.add_argument("collection", help="Введите название коллекции")
    args = collection.parse_args()
    collection = args.collection
    hubble_collection(collection)


if __name__ == '__main__':
    main()
