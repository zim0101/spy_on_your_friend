import pyscreenshot as ImageGrab
from settings import project_root_dir


def upload_path() -> str:
    return project_root_dir + '/assets/'


def take_screenshot() -> dict:
    try:
        full_image_path = upload_path() + 'fullscreen.png'
        print(full_image_path)
        image = ImageGrab.grab()
        image.save(full_image_path)

        return dict(success=True, path=full_image_path)
    except Exception as error:
        print(error)

        return dict(success=False)
