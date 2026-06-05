import allure
import re
from pathlib import Path


def take_screenshot(page, name):
    safe_name = re.sub(r'[<>:"/\\|?*]', '_', name).replace(' ', '_')
    path = Path("screenshots") / f"{safe_name}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    allure.attach(
        body=page.screenshot(path=str(path), full_page=True),
        name=safe_name,
        attachment_type=allure.attachment_type.PNG
    )

    # Capture a full-page screenshot, save it locally using a unique filename,
    # and attach the image to the Allure report with the provided name.
    # safe_name is used to create a valid filename by replacing invalid characters with underscores and replacing spaces with underscores as well.
