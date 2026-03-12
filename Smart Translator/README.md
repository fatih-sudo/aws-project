# Smart Translator
**By Muhammad Alfatih**

This project is a serverless web application that translates text between multiple languages using Amazon Translate. It features an "auto-detect" capability, so users don't need to specify the source language.

---

## Features
- **Language Auto-Detection:** Automatically identifies the input language.
- **Multiple Target Languages:** Supports translation to English, Indonesian, Arabic, Chinese, French, and Japanese.
- **Integrated UI:** The frontend is served directly from the Lambda function using Python f-strings to render HTML/CSS.
- **Dark Mode Design:** A modern, deep-blue theme for better readability.

## Tech Stack
- **Compute:** AWS Lambda
- **Service:** Amazon Translate
- **SDK:** Boto3
- **Language:** Python 3.12
- **Frontend:** HTML5 & CSS3 (Inter sans-serif font)

## How to Set Up
1. **AWS Lambda:** Create a new function and paste the `lambda_function.py` code.
2. **Function URL:** Enable the "Function URL" in AWS Lambda settings (Auth type: NONE) to get the public link.
3. **IAM Permissions:** Make sure the Lambda execution role has the `TranslateFullAccess` policy or specific `translate:TranslateText` permission.

## Data Flow
1. User enters text in the `textarea`.
2. The form sends a `GET` request to the Lambda Function URL with `text` and `lang` as query parameters.
3. Lambda processes the request using the Boto3 Translate client.
4. The result is returned and displayed in the result box.

---
*Developed as part of the AWS Project Collection.*
