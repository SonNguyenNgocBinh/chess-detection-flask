# Chess Piece Classifier Application

This project is a web application for classifying chess pieces from uploaded images using a pre-trained VGG16 deep learning model. The application uses Flask as the backend framework and supports drag-and-drop functionality for an intuitive user experience.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Setup and Installation](#setup-and-installation)
4. [Application Structure](#application-structure)
5. [Usage](#usage)
6. [Model Details](#model-details)
7. [Frontend Functionality](#frontend-functionality)
8. [Limitations and Future Improvements](#limitations-and-future-improvements)

---

## Features

- **Image Upload**: Users can upload images or drag and drop them onto the webpage.
- **Deep Learning Model**: A pre-trained VGG16 model classifies chess pieces into 12 classes (Black and White chess pieces).
- **User-Friendly Interface**: Designed with responsive design principles using modern HTML and JavaScript.
- **Real-Time Feedback**: Displays prediction results immediately after processing the image.

## Requirements

### Python Packages
- Flask
- Torch
- torchvision
- Pillow

### Additional Requirements
- Pre-trained VGG16 model file (e.g., `final_model_v3.pth`)
- Modern web browser for the frontend.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Python Dependencies**:
   Make sure Python is installed on your system. Then, install the required packages:
   ```bash
   pip install flask torch torchvision pillow
   ```

3. **Place the Pre-trained Model**:
   Place the pre-trained model file (`final_model_v3.pth`) in the root directory of the project.

4. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```

5. **Access the Application**:
   Open a browser and navigate to `http://127.0.0.1:5000`.

## Application Structure

### Backend
- **`app.py`**: Contains the Flask server logic, including routes for rendering the main page and handling image classification.
- **Deep Learning Model**: Loads a VGG16 architecture and predicts the class of the uploaded chess piece image.

### Frontend
- **HTML (index.html)**: A simple webpage allowing users to upload or drag-and-drop images.
- **JavaScript**: Handles form submissions, drag-and-drop behavior, and image previews.
- **CSS**: Adds styling and responsiveness for better user experience.

## Usage

1. Open the application in a browser.
2. Drag and drop an image of a chess piece onto the designated area or use the file upload button.
3. Click the "Check" button.
4. View the prediction result displayed on the page.

## Model Details

- **Architecture**: VGG16 with a modified classifier output layer to match the 12 chess piece classes.
- **Classes**:
  - Black Pieces: Bishop, King, Knight, Pawn, Queen, Rook
  - White Pieces: Bishop, King, Knight, Pawn, Queen, Rook
- **Preprocessing**:
  - Image resizing to 224x224 pixels
  - Normalization with ImageNet statistics ([0.485, 0.456, 0.406] mean and [0.229, 0.224, 0.225] std)

## Frontend Functionality

1. **Drag-and-Drop Support**:
   - Allows users to drag and drop an image file onto the upload form.
   - Provides immediate feedback if a non-image file is uploaded.

2. **Image Preview**:
   - Displays a preview of the uploaded image before submission.

3. **Real-Time Prediction**:
   - Fetches the prediction from the server via an AJAX request.

## Limitations and Future Improvements

### Current Limitations
- **Model Generalization**: The model's performance depends on the training data and may not generalize to unseen chess piece styles.
- **Error Handling**: Limited error handling for invalid or corrupt images.

### Future Improvements
- **Model Enhancements**: Train with a larger dataset covering various chess piece designs.
- **Multi-Language Support**: Add translations for the frontend interface.
- **Batch Processing**: Allow users to upload multiple images simultaneously.

---

## License
This project is released under the MIT License. Feel free to use and modify the code as needed.

---

For any issues or feature requests, please contact [Your Email/Repository Maintainer].

