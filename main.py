from fastapi import FastAPI, File, UploadFile, HTTPException
from services import static_analysis, ssl_testing

app = FastAPI()

@app.post("/analyze_apk/")
async def analyze_apk(file: UploadFile = File(...)):
    if not file.filename.endswith(".apk"):
        raise HTTPException(status_code=400, detail="Only APK files are supported.")

    # Save the uploaded APK file temporarily
    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(await file.read())

    # Step 2: Perform static analysis using Androguard
    static_result = static_analysis.perform_static_analysis(temp_file_path)
    
    # Step 3: Conduct SSL/TLS testing if URLs are found in static analysis
    urls = static_result.get("urls", [])
    ssl_result = ssl_testing.check_ssl_urls(urls)

    # Return combined results
    return {
        "static_analysis": static_result,
        "ssl_testing": ssl_result
    }
