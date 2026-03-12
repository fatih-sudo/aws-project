# Smart Translator
**Develope by: Muhammad Alfatih**

A serverless web application that provides instant text translation across multiple languages. This project utilizes Amazon Translate's machine learning capabilities to handle language processing.

---

## Features
- **Automatic Language Detection:** Uses the `auto` source code to identify the input language without user selection.
- **Multi-language Support:** Pre-configured for English, Indonesian, Arabic, Chinese, French, and Japanese.
- **Responsive Web UI:** A dark-themed, modern interface built directly into the Lambda response for seamless user interaction.

## Tech Stack
- **Compute:** AWS Lambda
- **AI Service:** Amazon Translate (Boto3 SDK)
- **Runtime:** Python 3.12
- **Frontend:** Vanilla HTML5 / CSS3

## How it Works
1. The user inputs text and selects the target language on the web interface.
2. The browser sends a GET request to the Lambda Function URL with the text as a query parameter.
3. The Lambda function calls the `translate_text` API.
4. The translated result is rendered back into the HTML and displayed to the user.

## Configuration & Permissions
To deploy this project, ensure your Lambda Execution Role has the following IAM policy attached:
- `TranslateFullAccess` or a custom policy allowing `translate:TranslateText`.

---
*Part of the AWS Project Collection by Muhammad Alfatih.*
