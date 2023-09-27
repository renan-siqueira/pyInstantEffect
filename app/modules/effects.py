import cv2
import numpy as np



def prompt_help(frame):
    # Styling and positioning
    x, y = 10, 30
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    color = (255, 255, 255)
    thickness = 1

    message = "Press 'H' for help menu."
    
    # Calculate text width and height to draw the background rectangle
    (w, h), _ = cv2.getTextSize(message, font, font_scale, thickness)
    overlay = frame.copy()
    cv2.rectangle(overlay, (x - 5, y - 30), (x + w + 5, y + 5), (0, 0, 0), -1)
    
    # Blend original frame with the overlay
    alpha = 0.7
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    cv2.putText(frame, message, (x, y), font, font_scale, color, thickness, lineType=cv2.LINE_AA)

    return frame


def display_help_menu(frame):
    commands = [
        ("p", "Pause/Play"),
        ("y/u", "Rotate +10/-10"),
        ("i/o", "Zoom Out/In"),
        ("k", "Toggle Flip Horizontal"),
        ("l", "Toggle Flip Vertical"),
        ("a", "Toggle Grayscale"),
        ("s", "Toggle Blur"),
        ("d", "Toggle Canny"),
        ("f", "Toggle Invert"),
        ("g", "Toggle Posterize"),
        ("z/x", "Decrease/Increase Brightness"),
        ("c", "Toggle Sketch"),
        ("v", "Toggle Contours"),
        ("b", "Toggle Pixelize"),
        ("e", "Toggle Cartoon"),
        ("r", "Toggle Pixel Art"),
        ("2", "Toggle Sepia"),
        ("3/4", "Decrease/Increase Contrast"),
        ("5", "Toggle Sobel Edge Detection"),
        ("6", "Toggle Histogram Equalization"),
        ("7", "Toggle Log Scale"),
        ("q", "Quit"),
    ]

    # Positioning, styling, and font details
    x, y_start = frame.shape[1] - 300, 25
    y_step = 25
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    color = (255, 255, 255)
    thickness = 1

    # Draw a transparent background rectangle for the entire help menu
    # Assume there are 20 commands for now; adjust if you add more
    height = len(commands) * y_step + 20
    overlay = frame.copy()
    cv2.rectangle(overlay, (x - 5, y_start - 25), (x + 250, y_start + height), (0, 0, 0), -1)

    # Blend original frame with the overlay
    alpha = 0.7
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    for key, description in commands:
        text = f"{key}: {description}"
        cv2.putText(frame, text, (x, y_start), font, font_scale, color, thickness, lineType=cv2.LINE_AA)
        y_start += y_step

    return frame


def resize_frame(frame, width=None, height=None):
    if width is None and height is None:
        return frame

    h, w, _ = frame.shape
    if width is None:
        ratio = height / float(h)
        dim = (int(w * ratio), height)
    elif height is None:
        ratio = width / float(w)
        dim = (width, int(h * ratio))
    else:
        dim = (width, height)

    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

def apply_grayscale(frame, grayscale=False):
    if grayscale:
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        return frame
    
def apply_blur(frame, blur=False, ksize=(15, 15)):
    if blur:
        return cv2.GaussianBlur(frame, ksize, 0)
    else:
        return frame
    
def apply_canny(frame, canny=False, low_threshold=50, high_threshold=150):
    if canny:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray_frame, low_threshold, high_threshold)
    else:
        return frame

def apply_invert(frame, invert=False):
    if invert:
        return cv2.bitwise_not(frame)
    else:
        return frame

def apply_posterize(frame, posterize=False, num_levels=4):
    if posterize:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        interval = 256 // num_levels
        return ((gray_frame // interval) * interval).astype('uint8')
    else:
        return frame

def apply_brightness(frame, brightness=0):
    if len(frame.shape) == 2:
        return frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - brightness
    v = v.astype('int32')
    v[v > lim] = 255
    v[v <= lim] += brightness
    v = v.clip(0, 255).astype('uint8')
    hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def apply_sketch(frame, sketch=False):
    if sketch:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur_frame = cv2.GaussianBlur(gray_frame, (25, 25), 0)
        canny_frame = cv2.Canny(blur_frame, 30, 60)
        return cv2.cvtColor(canny_frame, cv2.COLOR_GRAY2BGR)
    else:
        return frame
    
def apply_contours(frame, contours=False):
    if contours:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    else:
        return frame

def apply_pixelize(frame, pixelize=False, block_size=16):
    if pixelize:
        h, w, _ = frame.shape
        return cv2.resize(cv2.resize(frame, (w // block_size, h // block_size), interpolation=cv2.INTER_LINEAR),
                          (w, h), interpolation=cv2.INTER_NEAREST)
    else:
        return frame

def apply_cartoon(frame, cartoon=False, num_down=2, num_bilateral=7):
    if cartoon:
        img_color = frame
        for _ in range(num_down):
            img_color = cv2.pyrDown(img_color)
        for _ in range(num_bilateral):
            img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)
        for _ in range(num_down):
            img_color = cv2.pyrUp(img_color)
        img_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.medianBlur(img_gray, 7)
        img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
        return cv2.bitwise_and(img_color, img_edge)
    else:
        return frame

def apply_pixel_art(frame, pixel_art=False, pixel_size=10):
    if pixel_art:
        h, w, _ = frame.shape
        return cv2.resize(cv2.resize(frame, (w // pixel_size, h // pixel_size), interpolation=cv2.INTER_LINEAR),
                        (w, h), interpolation=cv2.INTER_NEAREST)
    else:
        return frame

def apply_rotation(frame, angle=0):
    if angle != 0:
        (height, width) = frame.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(frame, rotation_matrix, (width, height))
    else:
        return frame

def apply_zoom(frame, factor=1.0):
    if factor != 1.0:
        (height, width) = frame.shape[:2]
        new_width, new_height = int(width * factor), int(height * factor)
        return cv2.resize(frame, (new_width, new_height))
    else:
        return frame

def apply_flip(frame, horizontal=True, vertical=False):
    flip_code = 1 if horizontal and vertical else 0 if horizontal else -1 if vertical else None
    if flip_code is not None:
        return cv2.flip(frame, flip_code)
    else:
        return frame

def apply_sepia(frame, enable=True):
    if enable:
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        return cv2.transform(frame, sepia_filter)
    else:
        return frame

def adjust_contrast(frame, contrast=1.0):
    if contrast != 1.0:
        return cv2.addWeighted(frame, contrast, frame, 0, 0)
    else:
        return frame

def apply_sobel_edge_detection(frame, enable=True):
    if enable:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sobel_x = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(gray_frame, cv2.CV_64F, 0, 1, ksize=3)
        abs_sobel_x = cv2.convertScaleAbs(sobel_x)
        abs_sobel_y = cv2.convertScaleAbs(sobel_y)
        return cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
    else:
        return frame

def apply_histogram_equalization(frame, enable=True):
    if enable:
        ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        ycrcb[:,:,0] = cv2.equalizeHist(ycrcb[:,:,0])
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
    else:
        return frame

def apply_log_scale(frame, enable=True):
    if enable:
        c = 255 / np.log(1 + np.max(frame))
        return (c * np.log(1 + frame)).clip(0, 255).astype(np.uint8)
    else:
        return frame
