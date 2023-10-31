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
with open('svm_classifier_updated_gridsearch.pkl', 'rb') as f:
    svm_loaded_classifier = pickle.load(f)

CNN_loaded_classifier = tf.keras.models.load_model('my_model_200_databal.keras')

resnet_loaded_classifier = tf.keras.models.load_model('my_model_resnet_databal.keras')

def get_majority_vote(results):
    counts = {}
    for result in results:
        if result in counts:
            counts[result] += 1
        else:
            counts[result] = 1
    
    majority_vote = max(counts, key=counts.get)
    return majority_vote

@app.post("/")
async def process_request(request: Request):
    logging.info('Processing a request.')
    data = await request.json()
    bytes_data = data['bytes_data']
    np_img_svm = load_image_svm(bytes_data)
    proba_svm, result_svm = svm_classifier(np_img_svm, svm_loaded_classifier)
    np_img_cnn = load_image_cnn(bytes_data)
    proba_cnn, result_cnn = cnn_classifier(np_img_cnn, CNN_loaded_classifier)
    proba_resnet, result_resnet = cnn_classifier(np_img_cnn, resnet_loaded_classifier)
    print({'proba_svm': type(proba_svm), 'result_svm': type(result_svm) , 'proba_cnn': type(proba_cnn), 'result_cnn': type(result_cnn)})
    majority_vote = get_majority_vote([result_svm, result_cnn, result_resnet])
    return {'proba_svm': proba_svm, 'result_svm': result_svm , 'proba_cnn': proba_cnn, 'result_cnn': result_cnn, 'proba_resnet': proba_resnet, 'result_resnet': result_resnet, 'final_vote': majority_vote}
    # return "done"

if __name__ == "__main__":
   uvicorn.run("nus-iss:app", host="0.0.0.0", port=8000, reload=False)
