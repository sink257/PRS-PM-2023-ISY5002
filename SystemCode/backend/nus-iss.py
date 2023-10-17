import logging
import ast
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from Main import *

app = FastAPI(title="nus-iss-API",)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post("/")
async def process_request(request: Request):
    logging.info('Processing a request.')
    data = await request.json()
    bytes_data = data['bytes_data']
    np_img = load_image(bytes_data)
    result = svm_classifier(np_img)
    return result
    

if __name__ == "__main__":
   uvicorn.run("nus-iss:app", host="0.0.0.0", port=8000, reload=True)
