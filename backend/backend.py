from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser
import os
from openai import OpenAI
from io import BytesIO
import customtkinter 
import customtkinter as CTk
from PIL import Image, ImageTk
import requests 
from PIL import Image
import openai
import tkinter as tk
from PIL import Image, ImageTk
import requests
from openai import OpenAI
import os
import requests
import os

# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Like this video if this helped!",
        'people': ['Jack', 'Harry', 'Arpan']
    })

# def search_website(query):
#     # Example: Search a website (e.g., example.com) for a query
#     response = requests.get(f"https://example.com/search?q={query}")
#     soup = BeautifulSoup(response.content, 'html.parser')
#     # Process the soup to find search results
#     # This part depends on the structure of the website's HTML
#     results = []
#     for result in soup.findAll('div', class_='search-result'):
#         results.append(result.text)
#     return results

# @app.route('/search', methods=['GET'])
# def handle_search():
#     query = request.args.get('query')
#     if not query:
#         return jsonify({'error': 'Missing query parameter'}), 400
#     results = search_website(query)
#     return jsonify(results)

@app.route('/imagegen', methods=['GET'])
def image_generation():
    client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY2"))

    response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    # print(image_url)

    # Fetch the image from the URL
    image_data = requests.get(image_url).content

    # Convert the image data to a PIL Image object
    pil_image = Image.open(BytesIO(image_data))

    # Create a Tkinter window
    window = tk.Tk()
    window.title("Image Display")

    # Convert the PIL Image to a Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(pil_image)

    # Create a label to display the image
    image_label = tk.Label(window, image=tk_image)
    image_label.pack()
    


    # Run the Tkinter event loop
    window.mainloop()
    
    # Fetch image from URL

    image_data = requests.get(image_url).content

    # Specify the folder where you want to save the images
    folder_path = "image_folder"

    # Check if the folder exists, create it if it doesn't
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate a unique filename for the image
    image_name = "image5.jpg"  # You can generate a unique filename based on timestamp or other criteria

    # Save the image to the specified folder
    image_path = os.path.join(folder_path, image_name)
    with open(image_path, "wb") as image_file:
        image_file.write(image_data)

    print("Image saved successfully to:", image_path)
  




    



if __name__ == "__main__":
    app.run(debug=True, port=8080)
