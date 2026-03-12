# AWS PROJECT
### Developed by **MUHAMMAD ALFATIH**

Welcome to my AWS exploration hub! This repository contains a collection of serverless micro-services built using **AWS Lambda** and **Python**. Each project demonstrates the power of integrating cloud-native AI services to solve real-world challenges.

---

## Project Showcase

### 1. LINK VALIDATOR (Cyber Security)
A high-performance URL reputation scanner designed to detect phishing and malicious links before they cause harm.
* **Engine:** VirusTotal API V3.
* **Core Logic:** Encodes target URLs into Base64 (V3 Standard) and retrieves security verdicts from 70+ antivirus vendors.
* **Stack:** Python 3.12, AWS Lambda, REST API.

### 2. IMAGE ANALYZER (Computer Vision)
An automated image recognition tool that extracts meaningful data from visual content.
* **Engine:** Amazon Rekognition.
* **Feature:** Detects objects, scenes, and labels with high-confidence scoring.
* **Stack:** AWS Lambda, Boto3 SDK, Amazon S3.

### 3. SMART TRANSLATOR (Natural Language Processing)
A seamless translation engine with intelligent source language identification.
* **Engine:** Amazon Translate.
* **Feature:** Supports 75+ languages with "Auto-Detect" capability.
* **Stack:** AWS Lambda, Boto3, HTML5 Interaction.

---
---

## Live Demos
Experience the power of these tools in real-time:
* [Link Validator](https://djjpfdukwxg5gtzk2j6atrrm2i0huhgj.lambda-url.us-east-1.on.aws/)
* [Image Analyzer](https://kzxt3gh4a2pxzlwn4tm5xyenea0yujfx.lambda-url.us-east-2.on.aws/)
* [Smart Translator](https://chifauwy4cf442nabzvtg7lb4y0akolg.lambda-url.us-east-2.on.aws/)

---

## Architecture Philosophy
All projects in this repository follow the **Serverless First** principle:
- **Zero Management:** No servers to provision or manage.
- **Pay-as-you-go:** Cost-efficient execution (Free Tier Friendly).
- **Global Reach:** Leveraging AWS global infrastructure for low-latency responses.



---

## How to Use
1.  Navigate to the specific project folder (e.g., `/link-validator`).
2.  Copy the `lambda_function.py` code to your AWS Lambda Console.
3.  Ensure your Lambda Execution Role has the necessary permissions (e.g., `AmazonRekognitionFullAccess`, `TranslateFullAccess`).
4.  For the **Link Validator**, make sure to add your own VirusTotal API Key.

---

## About the Author
**Muhammad Alfatih**
A Cloud Computing enthusiast focused on building secure, scalable, and intelligent applications on AWS. 

> "Building the future, one function at a time."
