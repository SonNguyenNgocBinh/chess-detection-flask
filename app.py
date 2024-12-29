from flask import Flask, render_template, request, jsonify
import torch
from torchvision.models import vgg16  #  model architecture
from torchvision import transforms  # Import transforms for image preprocessing
from PIL import Image

app = Flask(__name__)

class_names = ['Black Bishop', 'Black King', 'Black Knight', 'Black Pawn', 'Black Queen', 'Black Rook', 'White Bishop', 'White King', 'White Knight', 'White Pawn', 'White Queen', 'White Rook']
# Load model and classes
model_path = "final_model_v3.pth"  

# Define the model architecture (this needs to match the one you used when training)
model = vgg16(pretrained=False)  # Adjust according to your architecture
model.classifier[6] = torch.nn.Linear(4096, len(class_names))  # Adjust output layer size
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load state dict (weights)
model.load_state_dict(torch.load(model_path, map_location=device))
model.eval()  



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        img = Image.open(file).convert('RGB')
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        img_tensor = transform(img).unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model(img_tensor)
            _, predicted_idx = torch.max(outputs, 1)
            predicted_class = class_names[predicted_idx.item()]

        return jsonify({'prediction': predicted_class})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)