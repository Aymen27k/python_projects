import pyautogui
import time
import numpy as np
import cv2
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "chest_templates")
THRESHOLD_VALUE = 50
LOWER_MOVEMENT_THRESHOLD = 400
HIGHER_MOVEMENT_THRESHOLD = 1200
LIKE_BUTTON_PATH = os.path.join(TEMPLATES_DIR, "like.jpg")
MAX_LIKES_PER_STREAM = 20
LIKE_COOLDOWN = 7



def item_location_clicking(image_path):
    # Initialize the mouse position
    x, y = pyautogui.position()
    try:
        window_pop_up = pyautogui.locateOnScreen(image_path, confidence=0.8, grayscale=True)
        if window_pop_up:
            center_x = window_pop_up.left + window_pop_up.width / 2
            center_y = window_pop_up.top + window_pop_up.height / 2
            pyautogui.click(center_x, center_y)
            pyautogui.moveTo(x, y)
            print(f"Clicked on '{image_path}' at ({int(center_x)}, {int(center_y)})")
            return True
        else:
            print(
                f"'{image_path}' found but not clickable (perhaps due to very low confidence returning None, "
                f"though unlikely with ImageNotFoundException).")
            return False
    except pyautogui.ImageNotFoundException:
        print(f"Image '{image_path} not found on screen. Skipping Click")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while processing '{image_path}': {e}")
        return False


CHEST_TEMPLATES = [
    os.path.join(TEMPLATES_DIR, "still_chest_player.jpg"),
    os.path.join(TEMPLATES_DIR, "chest_x10.jpg"),
    os.path.join(TEMPLATES_DIR, "small_chest.jpg"),
    os.path.join(TEMPLATES_DIR, "chest_x10_2.jpg"),
    os.path.join(TEMPLATES_DIR, "still_chest_x3.jpg"),
    os.path.join(TEMPLATES_DIR, "chest_x5.jpg"),
    os.path.join(TEMPLATES_DIR, "chest_regular.jpg"),
    os.path.join(TEMPLATES_DIR, "chest_x4.jpg"),
    os.path.join(TEMPLATES_DIR, "chest_x7.jpg"),
    os.path.join(TEMPLATES_DIR, "chest_50.jpg"),
]


def main():
    chest_found = False
    running = True
    chest_location = None
    chest_coords = None
    likes_given_current_stream = 0
    while not chest_found:
        # Searching for the chest image
        for template_path in CHEST_TEMPLATES:
            try:
                chest_location = pyautogui.locateOnScreen(template_path, confidence=0.9, grayscale=True)
                if chest_location:
                    chest_coords = (int(chest_location.left), int(chest_location.top), int(chest_location.width),
                                    int(chest_location.height))
                    print(f"Chest found using template: {template_path} at {chest_coords}")
                    chest_region_screenshot = pyautogui.screenshot(region=chest_coords)
                    previous_frame_array = np.array(chest_region_screenshot)
                    previous_frame_gray = cv2.cvtColor(previous_frame_array, cv2.COLOR_BGR2GRAY)
                    chest_found = True
                else:
                    print("Chest not found initially, trying again...")
                    time.sleep(1)
            except pyautogui.PyAutoGUIException as e:
                print(f"Error locating image {template_path}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
    while running:
        try:
            # Initialize the mouse position
            x, y = pyautogui.position()
            # Take the current screenshot of the defined region
            current_screenshot_pillow = pyautogui.screenshot(region=chest_coords)
            current_frame_array = np.array(current_screenshot_pillow)
            current_frame_gray = cv2.cvtColor(current_frame_array, cv2.COLOR_BGR2GRAY)
            # --- Comparing two images for motion detection ---
            difference = cv2.absdiff(previous_frame_gray, current_frame_gray)
            ret, thresh = cv2.threshold(difference, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
            movement_score = cv2.countNonZero(thresh)
            print(movement_score)
            # Comparing if movement is big enough to click
            if LOWER_MOVEMENT_THRESHOLD < movement_score < HIGHER_MOVEMENT_THRESHOLD:
                # Calculate the center x and y coordinates
                center_x = chest_location.left + chest_location.width / 2
                center_y = chest_location.top + chest_location.height / 2

                # Click the center of the chest
                pyautogui.click(center_x, center_y)
                pyautogui.moveTo(x, y)
                time.sleep(10)

            # Skip window pop Up
            clicked_window_pop = item_location_clicking(os.path.join(TEMPLATES_DIR, "window_pop.jpg"))

            clicked_got_it = item_location_clicking(os.path.join(TEMPLATES_DIR, "got_it.jpg"))

            clicked_woohoo = item_location_clicking(os.path.join(TEMPLATES_DIR, "woohoo.jpg"))

            if clicked_window_pop or clicked_got_it or clicked_woohoo:
                print("One or more pop-up buttons were found and clicked. Adding a short delay.")
                time.sleep(1)
            if likes_given_current_stream < MAX_LIKES_PER_STREAM:
                like_clicked_this_iteration = item_location_clicking(LIKE_BUTTON_PATH)
                if like_clicked_this_iteration:
                    likes_given_current_stream += 1
                    print(f"Given {likes_given_current_stream}/{MAX_LIKES_PER_STREAM} likes in this stream.")
                    time.sleep(LIKE_COOLDOWN)

            # Replacing the old frame with most recent one
            if previous_frame_gray is not None:
                previous_frame_gray = current_frame_gray

            # Small delay to avoid CPU overload
            time.sleep(0.05)
        except KeyboardInterrupt:
            print("\nCtrl+C detected! Initiating graceful shutdown...")
            running = False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            running = False
    print("Chest Hunter has stopped gracefully.")


if __name__ == "__main__":
    main()
