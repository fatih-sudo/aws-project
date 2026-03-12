# Image Analyzer
**Developer: Muhammad Alfatih**

A serverless computer vision application that identifies objects and scenes within images using deep learning. This project integrates AWS Lambda with Amazon Rekognition to provide high-accuracy image tagging.

---

## Features
- **Object Detection:** Identifies multiple labels in a single image.
- **Confidence Scoring:** Displays the mathematical probability (percentage) for each detected object.
- **Drag-and-Drop Interface:** Clean web UI for easy image uploading and instant analysis.
- **Base64 Processing:** Efficiently handles image data transmission from frontend to backend.

## Tech Stack
- **Compute:** AWS Lambda
- **Computer Vision:** Amazon Rekognition
- **SDK:** Boto3
- **Languages:** Python 3.12, JavaScript (ES6), HTML5/CSS3

## How it Works
1. User uploads an image via the web interface.
2. The image is converted to a Base64 string and sent to the Lambda function.
3. Lambda decodes the image and passes the bytes to the `detect_labels` API in Amazon Rekognition.
4. The API returns a list of labels and confidence scores, which are rendered back to the UI.

## Configuration & Permissions
To run this project, the Lambda Execution Role requires the following permission:
- `AmazonRekognitionFullAccess` (or a custom policy allowing `rekognition:DetectLabels`).

---
*Part of the AWS Project Collection by Muhammad Alfatih.*
