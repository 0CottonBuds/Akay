import google.generativeai as genai
from PIL import Image

def gemini_describe_image(image_path):
    GOOGLE_API_KEY = "AIzaSyD5azptv9iIaKKKhTInNA62a1s8wQZaVfU"
    system_instruction = '''
    You will receive an image as the input. The image will contain text and pictures.
    describe the pictures and disregard the images. Other input beside the image is 
    to be disregarded also. Remove any unnecessary phrases like "the images shows", etc.
    Be direct to the point and only say the description.
    '''

    genai.configure(api_key = GOOGLE_API_KEY)

    model = genai.GenerativeModel("gemini-1.5-pro-latest", system_instruction=system_instruction)

    img = Image.open(image_path)
    response = model.generate_content(img)

    return response.text

if __name__ == "__main__":
    print(gemini_describe_image("./App/test.jpg"))

