import os

import cv2

import app.modules.effects as effects
from app.config.settings import INPUT_DIR, VIDEO_NAME


def main(video_path, display_width=1280, display_height=720):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print('fps:', fps)

    pause = False
    help_menu = False

    grayscale = False
    blur = False
    canny = False
    invert = False
    posterize = False

    brightness = 0
    sketch = False
    contours = False
    pixelize = False

    cartoon = False
    pixel_art = False

    rotation_angle = 0
    zoom_factor = 1.0
    flip_horizontal = False
    flip_vertical = False

    sepia = False
    contrast = 1.0
    sobel_edge_detection = False
    histogram_equalization = False
    log_scale = False

    while cap.isOpened():
        if not pause:
            ret, frame = cap.read()
            if not ret:
                break

            resized_frame = effects.resize_frame(frame, width=display_width, height=display_height)

            processed_frame = effects.apply_grayscale(resized_frame, grayscale)
            processed_frame = effects.apply_blur(processed_frame, blur)
            processed_frame = effects.apply_canny(processed_frame, canny)
            processed_frame = effects.apply_invert(processed_frame, invert)
            processed_frame = effects.apply_posterize(processed_frame, posterize)

            processed_frame = effects.apply_brightness(processed_frame, brightness)
            processed_frame = effects.apply_sketch(processed_frame, sketch)
            processed_frame = effects.apply_contours(processed_frame, contours)
            processed_frame = effects.apply_pixelize(processed_frame, pixelize)

            processed_frame = effects.apply_cartoon(processed_frame, cartoon)
            processed_frame = effects.apply_pixel_art(processed_frame, pixel_art)

            processed_frame = effects.apply_rotation(processed_frame, rotation_angle)
            processed_frame = effects.apply_zoom(processed_frame, zoom_factor)
            processed_frame = effects.apply_flip(processed_frame, flip_horizontal, flip_vertical)

            processed_frame = effects.apply_sepia(processed_frame, sepia)
            processed_frame = effects.adjust_contrast(processed_frame, contrast)
            processed_frame = effects.apply_sobel_edge_detection(processed_frame, sobel_edge_detection)
            processed_frame = effects.apply_histogram_equalization(processed_frame, histogram_equalization)
            processed_frame = effects.apply_log_scale(processed_frame, log_scale)

            if help_menu:
                processed_frame = effects.display_help_menu(processed_frame)
            else:
                processed_frame = effects.prompt_help(processed_frame)

            cv2.imshow('Player', processed_frame)


        key = cv2.waitKey(fps) & 0xFF
        if key == ord("p"):
            pause = not pause
        elif key == ord("h"):
            help_menu = not help_menu
        elif key == ord("y"):
            rotation_angle += 10
        elif key == ord("u"):
            rotation_angle -= 10
        elif key == ord("i"):
            zoom_factor -= 0.1
        elif key == ord("o"):
            zoom_factor += 0.1
        elif key == ord("k"):
            flip_horizontal = not flip_horizontal
        elif key == ord("l"):
            flip_vertical = not flip_vertical
        elif key == ord("a"):
            grayscale = not grayscale
        elif key == ord("s"):
            blur = not blur
        elif key == ord("d"):
            canny = not canny
        elif key == ord("f"):
            invert = not invert
        elif key == ord("g"):
            posterize = not posterize
        elif key == ord("z"):
            brightness -= 10
        elif key == ord("x"):
            brightness += 10
        elif key == ord("c"):
            sketch = not sketch
        elif key == ord("v"):
            contours = not contours
        elif key == ord("b"):
            pixelize = not pixelize
        elif key == ord("e"):
            cartoon = not cartoon
        elif key == ord("r"):
            pixel_art = not pixel_art
        elif key == ord("2"):
            sepia = not sepia
        elif key == ord("3"):
            contrast = max(contrast - 0.1, 0.1)
        elif key == ord("4"):
            contrast = min(contrast + 0.1, 4.0)
        elif key == ord("5"):
            sobel_edge_detection = not sobel_edge_detection
        elif key == ord("6"):
            histogram_equalization = not histogram_equalization
        elif key == ord("7"):
            log_scale = not log_scale
        elif key == ord("q") or key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':

    input_dir, video_name = INPUT_DIR, VIDEO_NAME
    video_path = os.path.join(input_dir, video_name)

    main(video_path)