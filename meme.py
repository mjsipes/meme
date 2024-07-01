from instagramy import InstagramUser
import requests
import os

# Function to download images
def download_image(url, folder_path, image_name):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(folder_path, image_name), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    else:
        print(f"Failed to download image: {image_name}")

# Function to get user images
def get_instagram_images(username):
    user = InstagramUser(username)
    folder_path = username
    os.makedirs(folder_path, exist_ok=True)
    
    images = user.posts
    for index, image in enumerate(images):
        image_url = image['display_url']
        download_image(image_url, folder_path, f'image_{index}.jpg')
        print(f'Downloaded image {index + 1}/{len(images)}')

if __name__ == "__main__":
    username = "instagram_username_here"  # Replace with the desired username
    get_instagram_images(username)
