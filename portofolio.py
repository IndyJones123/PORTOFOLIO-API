from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ListenExperience.ListenExperience import ListenExperience
import psycopg2

# MY MAIN MODULE
import logging
import mainhttp
# from MainModuleADM.Utils.validate import i
from MainModuleADM.Encryption.aes import i_decrypt, i_encrypt
from MainModuleADM.Logging.logging_config import i_conf_logging, i_write_log
from MainModuleADM.Utils.validate import i_val as getJsonVal

import uvicorn

app = FastAPI()

dbUser = mainhttp.dbUser
dbPassword = mainhttp.dbPassword
dbUrl = mainhttp.dbUrl
dbName = mainhttp.dbName
port = mainhttp.port

loggers = logging.getLogger(__name__)



# CORS configuration
origins = [
    "http://localhost:5173",  # Allow your Vue app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger()

if not logger.handlers:
    logger.addHandler(i_conf_logging(nama_log='logging'))
    
mainhttp.loadXml()

@app.post('/api')
async def hello(request: Request):
    
    cnn = psycopg2.connect(
        user=dbUser,
        password=dbPassword,
        host=dbUrl,
        port=port,
        dbname=dbName
    )
    
    json_req = await request.json()
    # json_req['Authorization'] = request.headers.get('Authorization')

    try:
        ls_kd = getJsonVal(json_req, 'kdID')
        ls_appid = getJsonVal(json_req, 'appid')
    except Exception as ex:
        raise HTTPException(status_code=400, detail="Invalid format")

    if ls_appid == 'portofolio':
        listen_experience = ListenExperience(cnn, logger)
        rtr = listen_experience.handler(ls_kd, json_req)
    
    else:
        raise HTTPException(status_code=404, detail="Endpoint not found")

    cnn.close()
    
    return rtr

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")