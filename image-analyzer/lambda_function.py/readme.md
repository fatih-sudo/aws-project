import json
import base64
import boto3

rekognition = boto3.client("rekognition")

def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method") or event.get("httpMethod")

    if method == "GET" or method is None:
        html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Analyzer | Muhammad Alfatih</title>
    <style>
        :root { --bg: #0a192f; --card: #112240; --green: #64ffda; --text: #ccd6f6; --slate: #8892b0; }
        body { background: var(--bg); color: var(--text); font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { background: var(--card); padding: 2rem; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); width: 100%; max-width: 420px; border: 1px solid #233554; text-align: center; }
        h1 { color: var(--green); margin: 0; font-size: 1.6rem; letter-spacing: 1px; }
        .dev { font-size: 0.85rem; color: var(--slate); margin-bottom: 1.5rem; }
        .dev b { color: var(--green); }
        #drop-area { border: 2px dashed var(--green); border-radius: 12px; padding: 30px 15px; cursor: pointer; background: rgba(100, 255, 218, 0.03); transition: 0.3s; }
        #drop-area:hover { background: rgba(100, 255, 218, 0.08); }
        #preview { width: 100%; border-radius: 8px; display: none; margin-top: 10px; border: 1px solid var(--green); }
        #result-box { margin-top: 1.5rem; text-align: left; background: var(--bg); padding: 15px; border-radius: 8px; border-left: 4px solid var(--green); display: none; }
        .item { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #1d2d50; font-size: 0.9rem; }
        .conf { color: var(--green); font-weight: bold; font-family: monospace; }
        .stack-title { margin-top: 2rem; font-size: 0.7rem; color: var(--green); font-weight: bold; letter-spacing: 2px; text-transform: uppercase; }
        .stack-list { display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-top: 10px; font-size: 0.7rem; color: var(--slate); }
        .stack-item { background: rgba(35, 53, 84, 0.5); padding: 5px; border-radius: 4px; border: 1px solid #233554; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Image Analyzer</h1>
        <div class="dev">Developed by <b>Muhammad Alfatih</b></div>
        <div id="drop-area" onclick="document.getElementById('fileInp').click()">
            <div id="label">
                <p style="margin:0">Drag & Drop Image</p>
                <small style="color:var(--slate)">or click to analyze</small>
            </div>
            <img id="preview">
            <input type="file" id="fileInp" accept="image/*" style="display:none">
        </div>
        <div id="result-box"></div>
        <div class="stack-title">Technology Stack</div>
        <div class="stack-list">
            <div class="stack-item">AWS Lambda</div>
            <div class="stack-item">Amazon Rekognition</div>
            <div class="stack-item">Python 3.x</div>
            <div class="stack-item">Boto3 SDK</div>
            <div class="stack-item">HTML5 / CSS3</div>
            <div class="stack-item">JavaScript (ES6)</div>
        </div>
    </div>
    <script>
        const fileInp = document.getElementById("fileInp");
        const resBox = document.getElementById("result-box");
        ['dragover', 'drop'].forEach(e => window.addEventListener(e, ev => ev.preventDefault()));
        fileInp.onchange = e => process(e.target.files[0]);
        window.ondrop = e => { e.preventDefault(); process(e.dataTransfer.files[0]); };
        async function process(file) {
            if(!file) return;
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = async function() {
                document.getElementById("preview").src = reader.result;
                document.getElementById("preview").style.display = "block";
                document.getElementById("label").style.display = "none";
                resBox.style.display = "block";
                resBox.innerHTML = "<span style='color:var(--green)'>Analyzing...</span>";
                try {
                    const res = await fetch(window.location.href, {
                        method: "POST",
                        body: JSON.stringify({ image: reader.result.split(",")[1] })
                    });
                    const data = await res.json();
                    if(data.error) {
                        resBox.innerHTML = "Error: " + data.error;
                    } else {
                        let html = "<b style='color:white; font-size:0.8rem;'>DETECTED OBJECTS:</b><br>";
                        data.results.forEach(item => {
                            html += "<div class='item'><span>• " + item.name + "</span><span class='conf'>" + item.conf + "%</span></div>";
                        });
                        resBox.innerHTML = html;
                    }
                } catch (err) {
                    resBox.innerHTML = "Connection Error";
                }
            };
        }
    </script>
</body>
</html>
"""
        return {"statusCode": 200, "headers": {"Content-Type": "text/html"}, "body": html}

    try:
        body = json.loads(event.get("body", "{}"))
        image_data = base64.b64decode(body["image"])
        response = rekognition.detect_labels(
            Image={"Bytes": image_data},
            MaxLabels=8,
            MinConfidence=70
        )
        result_list = [{"name": l["Name"], "conf": round(l["Confidence"], 1)} for l in response["Labels"]]
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps({"results": result_list})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
