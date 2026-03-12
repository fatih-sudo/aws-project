import json
import boto3

def lambda_handler(event, context):
    translate = boto3.client('translate')
    
    query_params = event.get('queryStringParameters', {}) or {}
    text_input = query_params.get('text', '')
    target_lang = query_params.get('lang', 'en')

    translated_text = ""
    if text_input:
        try:
            response = translate.translate_text(
                Text=text_input,
                SourceLanguageCode="auto",
                TargetLanguageCode=target_lang
            )
            translated_text = response.get('TranslatedText')
        except Exception as e:
            translated_text = f"Error: {str(e)}"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Smart Translator | Muhammad Alfatih</title>
        <style>
            body {{ font-family: 'Inter', sans-serif; background: #0a192f; color: #e6f1ff; display: flex; justify-content: center; padding: 50px 20px; margin: 0; }}
            .container {{ background: #112240; padding: 40px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); width: 100%; max-width: 600px; border: 1px solid #233554; }}
            h1 {{ color: #ccd6f6; font-size: 28px; text-align: center; margin-bottom: 10px; }}
            .stack {{ color: #64ffda; font-size: 12px; font-family: monospace; text-align: center; margin-bottom: 30px; }}
            textarea {{ width: 100%; padding: 15px; background: #1d2d50; border: 1px solid #233554; border-radius: 8px; color: white; font-size: 16px; min-height: 120px; box-sizing: border-box; }}
            .controls {{ display: flex; gap: 10px; margin: 20px 0; }}
            select, button {{ padding: 12px; border-radius: 8px; border: none; font-weight: bold; }}
            select {{ background: #233554; color: white; flex: 2; }}
            button {{ background: #64ffda; color: #0a192f; flex: 1; cursor: pointer; }}
            .result-box {{ background: #0a192f; padding: 20px; border-radius: 8px; border-left: 4px solid #64ffda; min-height: 50px; margin-top: 20px; }}
            .footer {{ margin-top: 40px; font-size: 12px; color: #8892b0; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Smart Translator</h1>
            <div class="stack">STACK: AWS LAMBDA • AMAZON TRANSLATE • PYTHON</div>
            
            <form method="get">
                <textarea name="text" placeholder="Enter text in any language...">{text_input}</textarea>
                <div class="controls">
                    <select name="lang">
                        <option value="en" {"selected" if target_lang=="en" else ""}>English</option>
                        <option value="id" {"selected" if target_lang=="id" else ""}>Indonesian</option>
                        <option value="ar" {"selected" if target_lang=="ar" else ""}>Arabic</option>
                        <option value="zh" {"selected" if target_lang=="zh" else ""}>Chinese (Simplified)</option>
                        <option value="fr" {"selected" if target_lang=="fr" else ""}>French</option>
                        <option value="ja" {"selected" if target_lang=="ja" else ""}>Japanese</option>
                    </select>
                    <button type="submit">TRANSLATE</button>
                </div>
            </form>

            <div class="result-box">
                <small style="color: #64ffda">Translation Result:</small>
                <p style="margin-top: 10px; font-size: 18px;">{translated_text if translated_text else "Your translation will appear here..."}</p>
            </div>

            <div class="footer">
                Developed by: <b>Muhammad Alfatih</b><br>
                Cloud Computing Project
            </div>
        </div>
    </body>
    </html>
    """

    return {'statusCode': 200, 'headers': {'Content-Type': 'text/html'}, 'body': html_content}
