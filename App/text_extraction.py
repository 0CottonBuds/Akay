import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    return thresh

def detect_text_regions(image):
    # Find contours in the image
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter out small contours
    min_area = 100
    text_regions = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:
            x, y, w, h = cv2.boundingRect(contour)
            text_regions.append((x, y, w, h))
    
    return text_regions

def crop_text_regions(text_regions: list[tuple], image_path: str):
    # Load the original image
    original_image = cv2.imread(image_path)

    canvas = np.ones_like(original_image) * 255

    # Paste each text region onto the canvas
    for x, y, w, h in text_regions:
        text_region = original_image[y:y+h, x:x+w]
        canvas[y:y+h, x:x+w] = text_region
    
    # Save the combined image
    cv2.imwrite("./App/tmp/cropped_text_region.jpg", canvas)

def extract_text_from_img(image_path):
    image = preprocess_image(image_path)

    text = pytesseract.image_to_string(image)

    return text

if __name__ == "__main__":

    image_path = "./App/test.jpg" 

    preprocessed_image = preprocess_image(image_path)

    text_regions: list[tuple] = detect_text_regions(preprocessed_image)

    crop_text_regions(text_regions, image_path)
    
    text = extract_text_from_img("./App/tmp/cropped_text_region.jpg")
    print(text)
   