import os

def create_folder():
    static_folder = 'static'
    images_folder = '/images/'
    full_path = static_folder + images_folder
    
    if not os.path.exists(full_path):
        return os.makedirs(static_folder + images_folder)
