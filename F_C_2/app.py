from flask import Flask,request, jsonify
from pizza_class import FoodClassification
import os

app = Flask(__name__)


@app.route("/classify",methods=["POST"])

def classify_image():

    if "image" not in request.files:
        return "no image :("
    

    # Create a directory to save the images if it doesn't exist
    imag_directory ="./input_images"
    if not os.path.exists(imag_directory):
        os.makedirs(imag_directory)


    image_file=request.files["image"]
    img_path=imag_directory+image_file.filename
    image_file.save(img_path)


    #process food
    food=FoodClassification()
    pred=food.main(img_path)


    return jsonify({"Food": pred})
    

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)


