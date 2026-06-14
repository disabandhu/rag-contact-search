from fastapi import FastAPI, UploadFile, File
import pandas as pd
import numpy as np
import traceback
from pipeline import process_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running 🚀"}


@app.post("/process/")
async def process_file(file: UploadFile = File(...)):
    try:
        # Save uploaded file
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())

        # Run pipeline
        df = process_pipeline(file_location)

        # 🔥 FIX: make dataframe JSON-safe
        df = df.replace([np.inf, -np.inf], None)
        df = df.astype(object).where(pd.notnull(df), None)

        # Return only sample
        return df.head(10).to_dict(orient="records")

    except Exception as e:
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }