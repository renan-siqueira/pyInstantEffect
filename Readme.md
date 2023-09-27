# PyInstantEffect

### Description:

PyInstantEffect is a real-time video manipulation tool that allows users to apply a variety of effects while playing a video. With a range of keyboard shortcuts, users can toggle effects like grayscale, blur, cartoon, pixel art, and many others on the fly as they view the video.

### Features:

- Apply multiple effects in real-time.
- Control via keyboard shortcuts.
- Resize video to specific dimensions.
- Integrated help menu for easy reference of shortcuts.

### Prerequisites:

- Python
- OpenCV
- numpy

---

## Installation:

1. Ensure you have Python installed on your machine.

2. Clone the repository:

```bash
git clone https://github.com/renan-siqueira/pyInstantEffect.git
```

3. Navigate to the repository directory and install the required libraries:

```bash
cd pyInstantEffect
```

4. Set up a virtual environment:

- __Windows:__

```bash
python -m venv venv
.\venv\Scripts\activate
```

- __macOS and Linux:__

```bash
python3 -m venv venv
source venv/bin/activate
```

5. Install the required libraries:

```bash
pip install -r requirements.txt
```

6. Edit the `app/config/settings.py` file to point to your desired input directory and video name.

7. Run the program:

```bash
python run.py
```
---

## Keyboard Shortcuts:

| Key | Function |
|:----:|:----------:|
| H	| Toggle Help Menu |
| P | Pause/Play Video |
| Y	| Increase Rotation Angle by 10 |
| U	| Decrease Rotation Angle by 10 |
| I	| Decrease Zoom Factor by 0.1 |
| O	| Increase Zoom Factor by 0.1 |
| K	| Toggle Flip Horizontal |
| L	| Toggle Flip Vertical |
| A | Toggle Grayscale |
| S | Toggle Blur |
| D | Toggle Canny |
| F | Toggle Invert |
| G | Toggle Posterize |
| Z | Decrease Brightness by 10 |
| X | Increase Brightness by 10 |
| C | Toggle Sketch |
| V | Toggle Contours |
| B | Toggle Pixelize |
| E | Toggle Cartoon |
| R | Toggle Pixel Art |
| 2 | Toggle Sepia |
| 3 | Decrease Contrast by 0.1 (Min: 0.1) |
| 4 | Increase Contrast by 0.1 (Max: 4.0) |
| 5 | Toggle Sobel Edge Detection |
| 6 | Toggle Histogram Equalization |
| 7 | Toggle Log Scale |
| Q | Quit Application |

---

## Contributions:

Contributions are welcome! Please fork the repository and create a pull request with your changes.
