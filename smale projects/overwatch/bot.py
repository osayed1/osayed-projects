from time import sleep
import pyautogui as py

sleep(2)

def move_keys():
    # حركة دائرية مستمرة
    py.keyDown("s")
    sleep(0.3)
    py.keyUp("s")

    py.keyDown("a")
    sleep(0.3)
    py.keyUp("a")

    py.keyDown("d")
    sleep(0.3)
    py.keyUp("d")

    py.keyDown("w")
    sleep(0.3)
    py.keyUp("w")


def check_image(image):
    try:
        position = py.locateCenterOnScreen(image, confidence=0.3)
        if position is not None:
            py.press("esc")  # الحدث فقط عند ظهور الصورة
            print("✅ Image detected, pressed ESC!")
    except py.ImageNotFoundException:
        pass  # إذا ما لقى الصورة، تجاهل واستمر

# لوب لا نهائي
while True:
    move_keys()  # حركة مستمرة
    check_image(r"C:\idk\overwatch\dps.png")  # تحقق من الصورة
    sleep(0.1)  # تقليل الضغط على المعالج
