import allure
from pathlib import Path


def take_screenshot(page, name):
    path = Path("screenshots") / f"{name.replace(' ', '_')}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    allure.attach(
        body=page.screenshot(path=str(path), full_page=True),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )

    # Capture a full-page screenshot, save it locally using a unique filename,
    # and attach the image to the Allure report with the provided name.
