# Link Validator
**Developer: Muhammad Alfatih**

A cyber-security tool designed to scan URLs for potential threats like malware and phishing. It uses a serverless backend to interface with the VirusTotal V3 API.

---

## Features
- **Reputation Scanning:** Checks URLs against 70+ security vendors.
- **Base64 URL Identifier:** Implements the VirusTotal V3 standard for URL identification.
- **Cyber-Terminal UI:** A hacker-style retro interface for a unique user experience.
- **Real-time Results:** Instant feedback on malicious, suspicious, and harmless ratings.

## Tech Stack
- **Backend:** AWS Lambda (Python 3.12)
- **API Integration:** VirusTotal API V3
- **Frontend:** Vanilla HTML5, CSS3, and JavaScript (ES6 Fetch)
- **Libraries:** Urllib3, JSON, Base64

## How to Set Up
1. **API Key:** Obtain an API key from VirusTotal and place it in the `VT_API_KEY` variable.
2. **AWS Lambda:** Create a function and paste the code. Use the "Function URL" feature to access the app.
3. **Environment:** No external libraries required (uses standard Python libraries available in Lambda).

## Application Logic
1. The frontend encodes the user's URL input.
2. The Lambda function converts the URL into a URL-safe Base64 string (without padding).
3. A request is sent to the VirusTotal URL analysis endpoint.
4. The statistical data (malicious, suspicious, etc.) is parsed and displayed on the terminal UI.

---
*Part of the AWS Project Collection by Muhammad Alfatih.*
