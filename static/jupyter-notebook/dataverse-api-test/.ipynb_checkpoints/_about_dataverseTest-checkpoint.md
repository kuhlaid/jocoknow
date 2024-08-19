# About

This notebook will be run against the demo server of the Dataverse at https://demo-dataverse.rdmc.unc.edu/dataverse/root.

## Configure a local Jupyter Server

`cd "/mnt/c/Users/pgale/University of North Carolina at Chapel Hill/TarcStudyDataRepository - Files/DataPull/364-dp/Note3/jocoknow/docs/jupyter-notebook/dataverse-api-test"`

`docker run -it --name 364-dp-DataverseApiTest --mount type=bind,source="$(pwd)",target="/home/jovyan/work" --add-host=host.docker.internal:host-gateway -p 10000:8888 quay.io/jupyter/scipy-notebook:latest`

## Notebook configuration

We will split our notebook configuration into several files (installer.py, _config.json, and worker.py). 

- The `installer.py` script installs Python modules our notebook may need. 

- The `_config.json` file(s) are used to define any configuration settings/variables so we can use the notebook code against multiple environments (demo, test, or production for example), thus making the notebook reusable by others. 

- The `worker.py` file contains our Python scripts since a notebook can become unweildy to use when all of the Python code is embeddd directly within the notebook. Although the main reason we use this external Python file is so our Python code can be placed within a Python object (or objects), making it much easier for the functions to interact with each other.o

## Packaging the Dataverse API handlers

At this point we want to setup a package/module that we can load from GitHub and use in our notebook since all of our dataset notebooks will be using the same code. Have the core code in an imported module will allow for ease of use by other users without the need to add the core functions into their notebook code. It simply makes things cleaner. At the moment we are simply using a locally stored file named `DvApiMod.py` to achieve this but having it moved to a plugin format will make it more extensible.

### Package files

This is an example of packaging on GitHub (which is what I want).
https://github.com/ceddlyburge/python_world/tree/master

https://packaging.python.org/en/latest/tutorials/packaging-projects/

### Using imported packages

https://github.com/wax911/plugin-architecture/blob/master/plugins/advanced-plugin/main.py#L14

## Issues

- We had originally placed our image files within .zip archives to minimize storage space and simplify the organizing of images, however the Dataverse code would not allow zip files to be replaced within a dataset without a duplicate file being created with a different filename (as of March 2024). Due to this problem we switched to simply organizing images by folder without archiving them into zip files.

## Old notebook worker code

```
import pandas as pd         # Import the data analysis libraries
from pandas import DataFrame
from tqdm import tqdm # progress bar
import numpy as np
import requests
import json
import time
import io
import hashlib
import os
from os.path import exists
import zipfile
from sqlalchemy import create_engine
import pymysql
# we use this to make sure our variable values are not printed to the notebook
from IPython.display import HTML, display, clear_output

# ===================================== include the functions we will use within the notebook
# @title Run this after any blocks of code you do not want to output printed
def ClearOutput():
    clear_output(wait=True) # we do not want any credentials saved as output in the notebook so we clear it (processed on the next line)
    print('')
    
# set up environment variables to be used by our notebook
notebookConfigurationJson=input("Paste the copied notebook configuration here:")
_CONFIG_ = json.loads(notebookConfigurationJson)    # convert the text JSON to a JSON object
ClearOutput() # ***WE DO NOT WANT THE CONFIGURATION PRINTED AS OUTPUT SO WE CLEAR THE OUTPUT AT THIS POINT***


# @title We need to convert some columns to be compatible with STATA, such as date fields (https://maxmasnick.com/kb/scipy/#tips-for-exporting-to-stata)
# We only need this if exporting to STATA
def StataDataPrep(df):
    type_pref = [int, float, str]
    for colname in list(df.select_dtypes(include=['object']).columns):
        for t in type_pref:
            try:
                df[colname] = df[colname].astype(t)
            except (ValueError, TypeError) as e:
                pass

# @title This function will initiate a Qualtrics API request for survey responses from a specified survey (see https://api.qualtrics.com/6b00592b9c013-start-response-export for related Qualtrics API documentation)
# @param strSurveyId=[Qualtrics Survey ID], strApiToken=[Qualtrics API token], strFilterId=[Qualtrics response filter ID to only pull the data we need from the survey]
def StartResponseExport(strSurveyId, strApiToken, strFilterId):
    # create request for the CSV data
    url = _CONFIG_["QAPI_ROOTSURVEYURL"]+strSurveyId+"/export-responses"
    payload = {"format": "csv", "filterId": strFilterId}
    headers = {
        "Content-Type": "application/json",
        "X-API-TOKEN": strApiToken
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    jsonResponse = json.loads(response.text)    # convert the text JSON to a JSON object
    print(jsonResponse)                         # only used for debugging
    print(jsonResponse["meta"]["httpStatus"])   # only used for debugging
    return jsonResponse

# @title This function checks the progress of the `StartResponseExport` function
# @param strSurveyId=[Qualtrics Survey ID], strApiToken=[Qualtrics API token], strExportProgressId=[the `progressId` returned from the `StartResponseExport` function]
def GetResponseExportProgress(strSurveyId, strApiToken, strExportProgressId):
    url = _CONFIG_["QAPI_ROOTSURVEYURL"]+strSurveyId+"/export-responses/"+strExportProgressId
    headers = {
        "Content-Type": "application/json",
        "X-API-TOKEN": strApiToken
    }
    response = requests.request("GET", url, headers=headers)
    jsonResponse = json.loads(response.text)    # convert the text JSON to a JSON object
    print(response.text)
    return jsonResponse

# @title This function retrieved the file once it is ready from the `GetResponseExportProgress` function
# @param strSurveyId=[Qualtrics Survey ID], strApiToken=[Qualtrics API token], strFileId=[the `fileId` returned from the `GetResponseExportProgress` function], strFileName=[a filename we will use to describe the data being returned from the Qualtrics AP]
def GetResponseExportFile(strSurveyId, strApiToken, strFileId, strFileName):
    url = _CONFIG_["QAPI_ROOTSURVEYURL"]+strSurveyId+"/export-responses/"+strFileId+"/file"
    headers = {
        "Content-Type": "application/json",
        "X-API-TOKEN": strApiToken
    }
    response = requests.request("GET", url, headers=headers)
    # the data is returned from Qualtrics as a zip file so we write it to a file in the Docker container
    with open(_CONFIG_["DOCKER_WORKING_DIR"]+"/"+strFileName, "wb") as f:
        f.write(response.content)
    return 'file retrieved'

# @title Add a column for image type (coded)
# @param Dataframe series
def imageType(series):
    if dictImgRef[series] != "":
        return dictImgRef[series]
    else:
        return series

# @title Add a column for file size (bytes)
# @param Dataframe series
def imageSize(series):
    return os.path.getsize(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/unprocessed/' + series.replace('.jpg','.png'))

# @title Give the image files new names and archive to the appropriate zip archive; this might take several minutes initially but subsequent runs are much faster since the code ignores files existing in the archives currently
# @param Dataframe row
def imageFilename(row):
    newFN = row['PublicId']+'_'+row['E03USIMGT']+'_00.png'  # create new filename recoded (based on the side and body part with a __00 suffix on the end to represent the archive number for that body part in the event we need to split them into multiple archives); we should not need to add additional archives for each bodypart due to the small file size of each archive
    isExisting = os.path.isfile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/unprocessed/'+row['filename'].replace('.jpg','.png'))  # check if old image filename exists
    if (isExisting):    # rename the image file if needed
        os.rename(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/unprocessed/'+row['filename'].replace('.jpg','.png'), _CONFIG_["DOCKER_WORKING_DIR"]+'/images/unprocessed/'+newFN)

    archive_name = row['E03USIMGT']+'.zip'
    # print('checking for '+row['E03USIMGT']+'.zip and newFN=',newFN)
    isExistingArchive = os.path.isfile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/'+row['E03USIMGT']+'.zip')
    if not isExistingArchive: # if the archive file needs to be created try to create it
        # print(isExistingArchive)
        # print('need to create zip for '+row['E03USIMGT'])
        with zipfile.PyZipFile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/'+row['E03USIMGT']+'.zip', 'x') as myzip:   # this does not work for 21.zip so 21.zip needed to be manually added 
            pass
    
    blnNewFNExists = False
    # check that the file does not already exist in the archive
    with zipfile.ZipFile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/'+row['E03USIMGT']+'.zip') as zf:
        if newFN in zf.namelist():
            blnNewFNExists=True

    if blnNewFNExists == False:
        # try to zip archive the file if it does not exist
        with zipfile.PyZipFile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/'+row['E03USIMGT']+'.zip', 'a') as myzip:
            myzip.write(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/unprocessed/'+newFN,newFN)
            print('adding ',newFN)

    return newFN

# @title Add a column for image side
# @param Dataframe series
def imageSide(series):
    return dictImageSideRef[series[:1]]

# @title Recode our ages to a range value instead
# @param Dataframe series
def ageRecode(series):
    if series >= 35 and series <= 39:
        return 1
    elif series >= 40 and series <= 44:
        return 2
    elif series >= 45 and series <= 49:
        return 3
    elif series >= 50 and series <= 54:
        return 4
    elif series >= 55 and series <= 59:
        return 5
    elif series >= 60 and series <= 64:
        return 6
    elif series >= 65 and series <= 70:
        return 7
    else:
        return series

# @title Generates an MD5 hash for a given file (used to check against files being uploaded to prevent duplicate file uploads)
# @argument File path
def md5(fileToCheck):
    hash_md5 = hashlib.md5()
    with open(fileToCheck, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# @title Upload a zip file to the Dataverse
# @param Archive name, a description we will use to describe the file in the Dataverse
def uploadZip(zipNumber,zipDescription):
    
    removeTempArchive(zipNumber)
    # create a placeholder temporary file first
    with zipfile.PyZipFile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/tmp/'+zipNumber+'c.zip', 'w') as myzip1:
        pass

    # double zip the file into a temporary zip
    with zipfile.PyZipFile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/tmp/'+zipNumber+'c.zip', 'w') as myzip:
        myzip.write(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/'+zipNumber+'.zip',zipNumber+'.zip')
        time.sleep(0.5) # try to ensure the archive is created before moving on
        pass
    
    # with zipfile.PyZipFile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/tmp/'+zipNumber+'c.zip', 'a') as myzip:
    #     myzip.write(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/'+zipNumber+'.zip', zipNumber+'.zip')

    fileobj = open(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/tmp/'+zipNumber+'c.zip', 'rb')  # read the double zipped file
    files = {'file': (zipNumber+'.zip', fileobj)}   # we have the new zip file object to save to the Dataverse

    # --------------------------------------------------
    # Using a "jsonData" parameter, add optional description + file tags
    # --------------------------------------------------
    params = dict(description=zipDescription,
                directoryLabel="data/image/ultrasound",
                fileName=zipNumber+'.zip',
                forceReplace="true",
                categories=['data', 'images', 'ultrasound'])
    print("uploadZip:",zipNumber,params)
    params_as_json_string = json.dumps(params)
    payload = dict(jsonData=params_as_json_string)

    # --------------------------------------------------
    # Add file using the Dataset's persistentId
    # --------------------------------------------------
    url_persistent_id = '%s/api/datasets/:persistentId/add?persistentId=%s&key=%s' % (DATAVERSE_SERVER, DATAVERSE_DATASET_DOI, DATAVERSE_API_KEY)

    # -------------------
    # Make the request
    # -------------------
    print('-' * 40)
    print('making request: %s' % url_persistent_id)
    r = requests.post(url_persistent_id, data=payload, files=files)

    # -------------------
    # Print the response
    # -------------------
    print('-' * 40)
    print(r.json())
    print(r.status_code)

    # removeTempArchive(zipNumber)

def removeTempArchive(zipNumber):
    isExisting = os.path.isfile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/tmp/'+zipNumber+'c.zip')  # check if image archive exists
    if (isExisting):
        print("removing archive",zipNumber+'c.zip')
        os.remove(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/tmp/'+zipNumber+'c.zip')    # remove temp archive
        time.sleep(0.5) # try to ensure the archive is removed before moving on
        
# @title Request the dataset contents from the Dataverse so we can compare with what we have locally
def getDVDatasetContents():
    # use the requests module from Python to make a simple request to the Dataverse to check the contents
    url = DATAVERSE_SERVER+"/api/datasets/:persistentId/versions/:latest?persistentId="+DATAVERSE_DATASET_DOI
    headers = {
        "Content-Type": "application/json",
        "X-Dataverse-Key": DATAVERSE_API_KEY
    }
    r = requests.request("GET", url, headers=headers)
    return r.json()    # convert the response to a dict

# @title Check that we have changes to a zip file before we try uploading to the Dataverse
# @param Archive name, a description we will use to describe the file in the Dataverse
def checkZipForUpload(zipNumber,zipDescription):
    # check for an existing file in the Dataverse
    strNewFileToUpload = zipNumber+'.zip'
    blnFileExists=False
    blnUpload=True
    strExistingMd5=''
    rJson = getDVDatasetContents()
    # print(rJson['data']['files'])   # loop through the files in the dataset to find the one we want to replace
    for item in rJson['data']['files']:
        if (item['label']==strNewFileToUpload):
            blnFileExists=True
            strExistingMd5 = item['dataFile']['md5']

    if (blnFileExists): # if the new file, we plan to upload, currently exists in the the Dataverse dataset, we check the MD5 checksum of the new file
        newFileMd5 = md5(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/'+strNewFileToUpload)
        if (newFileMd5==strExistingMd5):
            print("MD5 hashes match on "+strNewFileToUpload+", so do not upload new file")
            blnUpload=False
        else:
            print("Something has changed with the file so we can upload a new version of the file to the Dataverse",newFileMd5,"==",strExistingMd5)
            
    
    if (blnUpload):  # we will upload the file as long as it does not exist currently or the existing file is different from the newer file
        uploadZip(zipNumber,zipDescription)
        dictNewFile={str(zipNumber): {"filename": zipNumber+".zip", "fileCount":dictImageArchiveStats[zipNumber]['fileCount'],"directoryLabel": "data/image/ultrasound", "description": "This file contains an archive of "+dictImgTypeRef[zipNumber]+", ultrasound image files. There should only be one image per subject in this archive. Images are saved in lossless .png format.","updatedOnDataverse": str(datetime.now().astimezone())} }   # create the metadata for each zip archive
        zipMetaUpdate(zipNumber,dictNewFile)      # save the zip archive metadata to the main DatasetMetadata.json file


# @title Check that we have changes to a zip file before we try uploading to the Dataverse
# @param Archive name, a description we will use to describe the file in the Dataverse
def checkZipForUpload_test(zipNumber,zipPath,zipDescription):
     # create a placeholder temporary file first
    with zipfile.PyZipFile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/zipFileReplace/replacementFile/tmp/'+zipNumber+'c.zip', 'w') as myzip1:
        pass

    # double zip the file into a temporary zip
    with zipfile.PyZipFile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/zipFileReplace/replacementFile/tmp/'+zipNumber+'c.zip', 'w') as myzip:
        myzip.write(_CONFIG_["DOCKER_WORKING_DIR"]+zipPath+zipNumber+'.zip',zipNumber+'.zip')
        time.sleep(0.5) # try to ensure the archive is created before moving on
        pass
    
    # with zipfile.PyZipFile(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/tmp/'+zipNumber+'c.zip', 'a') as myzip:
    #     myzip.write(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/'+zipNumber+'.zip', zipNumber+'.zip')

    fileobj = open(_CONFIG_["DOCKER_WORKING_DIR"]+'/images/archive/zipFileReplace/replacementFile/tmp/'+zipNumber+'c.zip', 'rb')  # read the double zipped file
    files = {'file': (zipNumber+'.zip', fileobj)}   # we have the new zip file object to save to the Dataverse

    # --------------------------------------------------
    # Using a "jsonData" parameter, add optional description + file tags
    # --------------------------------------------------
    params = dict(description=zipDescription,
                directoryLabel="data/image/ultrasound",
                fileName=zipNumber+'.zip',
                forceReplace="true",
                categories=['data', 'images', 'ultrasound'])
    print("uploadZip:",zipNumber,params)
    params_as_json_string = json.dumps(params)
    payload = dict(jsonData=params_as_json_string)

    # --------------------------------------------------
    # Add file using the Dataset's persistentId
    # --------------------------------------------------
    url_persistent_id = '%s/api/datasets/:persistentId/add?persistentId=%s&key=%s' % (DATAVERSE_SERVER, DATAVERSE_DATASET_DOI, DATAVERSE_API_KEY)

    # -------------------
    # Make the request
    # -------------------
    print('-' * 40)
    print('making request: %s' % url_persistent_id)
    r = requests.post(url_persistent_id, data=payload, files=files)

    # -------------------
    # Print the response
    # -------------------
    print('-' * 40)
    print(r.json())
    print(r.status_code)

# @title Update the DatasetMetadata.json with new information on zip archives files to be sent to the Dataverse
# @param Name of the zip achive, the dictionary object describing the archive
def zipMetaUpdate(fileName,dictNewFile):
    jsonDatasetMetadata=getDatasetMetadata()
    # jsonDatasetMetadata={}
    # with open(_CONFIG_["DOCKER_WORKING_DIR"]+"/DatasetMetadata.json", mode='r') as jsonFile:   # read a copy of the metadata
    #     jsonDatasetMetadata = json.load(jsonFile)
    
    file_index = next((index for (index, obj) in enumerate(jsonDatasetMetadata['files']) if fileName in obj), "None")   # get the index of the file descriptions in the metadata
    
    if file_index=="None":
        jsonDatasetMetadata['files'].append(dictNewFile)    # add data not yet in the metadata file
    else:
        jsonDatasetMetadata['files'][file_index] = dictNewFile  # update existing metadata
        
    # save the JSON data
    with open(_CONFIG_["DOCKER_WORKING_DIR"]+"/DatasetMetadata.json", mode='w') as jsonFile:
        jsonFile.write(json.dumps(jsonDatasetMetadata, indent=2))

# @title Read the metadata file and return the contents
def getDatasetMetadata():
    with open(_CONFIG_["DOCKER_WORKING_DIR"]+"/DatasetMetadata.json", mode='r') as jsonFile:   # read a copy of the metadata
        return json.load(jsonFile)

# @title Retrieve the metadata for a file in the dataset
def getFileMetadata(fileName):
    jsonDatasetMetadata=getDatasetMetadata()
    # with open(_CONFIG_["DOCKER_WORKING_DIR"]+"/DatasetMetadata.json", mode='r') as jsonFile:   # read a copy of the metadata
    #     jsonDatasetMetadata = getDatasetMetadata()
    
    file_index = next((index for (index, obj) in enumerate(jsonDatasetMetadata['files']) if fileName in obj), "None")   # get the index of the file descriptions in the metadata
    
    if file_index!="None":
        return jsonDatasetMetadata['files'][file_index][fileName]
    
    return False
        

# give each image side and body part a numeric value which will be used in the renaming and partitioning of the images
dictImageSide = {
"1":"R",
"2":"L"
}
dictImageSideFull = {
"1":"Right",
"2":"Left"
}
dictImageBodyPart = {
"1":"SUPRAPAT LONG",
"2":"SUPRAPAT LONG CPD",
"3":"SUPRAPAT TRANS 30",
"4":"MED LONG",
"5":"LAT LONG",
"6":"SUPRAPAT TRANS FLEX",
"7":"POST TRANS"
}
dictImgRef = {} # create a reverse image type reference so we can create codes for the image types
for intImgSide in dictImageSide:
    for intBodyPart in dictImageBodyPart:
        dictImgRef[dictImageSide[intImgSide] + " " + dictImageBodyPart[intBodyPart]] = intImgSide+intBodyPart
dictImageSideRef = {}   # create a reverse image side reference so we can create a new column in the data for specifying the image side
for intImgSideRef in dictImageSide:
    dictImageSideRef[dictImageSide[intImgSideRef]] = intImgSideRef

genderVL = {1: "Male", 2: "Female"}
kl_gradeVL = {"00":"No OA",
                "1":"Questionable OA",
                "2":"Mild OA",
                "3":"Moderate OA",
                "4":"Severe OA",
                "9":"Non OA",
                "99":"Total joint replacement"}
ageVL = {"1":"35-39",
"2":"40-44",
"3":"45-49",
"4":"50-54",
"5":"55-59",
"6":"60-64",
"7":"65-70"}
paskVL = {"0":"None",
"1":"Mild",
"2":"Moderate",
"3":"Severe",
"888":"No response"}

dictImgTypeRef = {} # create a reverse image type reference so we can create codes for the image types
for intImgSide in dictImageSideFull:
    for intBodyPart in dictImageBodyPart:
        dictImgTypeRef[intImgSide+intBodyPart] = dictImageSideFull[intImgSide] + " " + dictImageBodyPart[intBodyPart]
# print(dictImgTypeRef)
# create value labels to apply to the data
# labels to apply to the STATA dataset
F2_IMAGE_value_labels = {
    "E03USIMGT": dictImgTypeRef,
    "E03USIMGD": dictImageSideFull
}

F2_IMAGE_variable_labels = {
    "E03SUBJECTID":"Unique subject/case ID for public consumption",
    "E03USIMGT":"Ultrasound image type",
    "E03USIMGF":"Ultrasound image file name",
    "E03USIMGZ":"Ultrasound image file size in bytes",
    "E03USIMGD":"Ultrasound image side"
}
F2_IMAGE_data_label="Ultrasound image references/metadata"
DATAVERSE_SERVER = 'https://'+_CONFIG_["DATAVERSE_DOMAIN"] # no trailing slash
DATAVERSE_API_KEY = _CONFIG_["DATAVERSE_API_KEY"]
DATAVERSE_DATASET_DOI = _CONFIG_["DATAVERSE_DATASET_DOI"] # doi or hdl of the dataset

# we need to get a fresh connection to the database anytime we make a SQL request otherwise we can end up with stale, old, data
def freshDbConn(blnSilent=True):
    # if you forget the password to the MySQL root user in OpenShift, log into OpenShift, open the terminal of the MySQL pod and enter 
    # `printenv` to get the list of environment variables
    # we are using variables for the database connection so the values are not saved to source control
    db_connection_str = "mysql+pymysql://"+_strUser+ ":" +_strPassword +"@"+_strHost+"/"+ _strDatabase 
    db_engine = create_engine(db_connection_str, connect_args= dict(host=_strHost, port=_intPort))
    try:
        db_connection = db_engine.connect()
        if (not blnSilent):
            print("It looks like our MySQL connection is good")
        return db_connection
    except:
        print("BLAHHHHH! We probably forgot to start our database server or port forward to it.")
    return False
    
_strHost=_CONFIG_["MYSQL_HOST"]
_intPort=_CONFIG_["MYSQL_PORT"]
_strUser=_CONFIG_["MYSQL_USERNAME"]
_strPassword=_CONFIG_["MYSQL_PASSWORD"]
_strDatabase=_CONFIG_["MYSQL_DATABASE"]

print("Notebook configuration complete")
```