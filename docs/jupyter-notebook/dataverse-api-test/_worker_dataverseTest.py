# @title Here we create a main working object (Worker) so our configuration and database connections can more easily integrate. Also separating the code from the notebooks makes the notebook easier to read and manage.
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
import shutil
from os.path import exists
import zipfile
# we use this to make sure our variable values are not printed to the notebook
from IPython.display import HTML, display, clear_output
from datetime import datetime
# currentDateAndTime = datetime.now().astimezone()    # get the current date and time to show when this notebook was last run

# @title By placing all of our Python function within a class object, it makes it much easier for information to be used across functions without needing to explicitly passing them into each function (instead we pass the entire Worker object into the functions so each function can do what it needs with the object)
class Worker:
    # @param strEnvironment (ex. demo or prod, would represent the environment you wish for the notebook code to run against)
    def __init__(self,strEnvironment):
        f = open ("_config_"+strEnvironment+".json", "r") # read the notebook configuration settings
        self._config = json.loads(f.read())
        f.close()
        print("Finished installing and importing modules for the",strEnvironment,"environment")
        self.strDATAVERSE_PARENT_COLLECTION = self._config["DATAVERSE_PARENT_COLLECTION"]
        self.strDATAVERSE_DOMAIN = self._config["DATAVERSE_DOMAIN"]
        self.strDATAVERSE_API_TOKEN = self._config["DATAVERSE_API_TOKEN"]
        
    
    # @title Create a new Dataverse collection (which is the same thing as creating a new Dataverse)
    def DvCreateCollection(self):
        print("start DvCreateCollection")
        strApiEndpoint = '%s/api/dataverses/%s' % (self.strDATAVERSE_DOMAIN, self.strDATAVERSE_PARENT_COLLECTION)
        print('making request: %s' % strApiEndpoint)
        objHeaders = {
            "Content-Type": "application/json",
            "X-Dataverse-Key": self.strDATAVERSE_API_TOKEN
        }
        r = requests.request("POST", strApiEndpoint, json=self._config["DATAVERSE_COLLECTION_START"], headers=objHeaders) # it is nice I can simply send the JSON object without the need to create a separate JSON file
        self.printResponseInfo(r)
        print("end DvCreateCollection")
        

    # @title View a new Dataverse collection based on the collection alias
    def DvViewCollection(self):
        print("start DvViewCollection")
        strApiEndpoint = '%s/api/dataverses/%s' % (self.strDATAVERSE_DOMAIN, self._config["DATAVERSE_COLLECTION_START"]["alias"])
        print('making request: %s' % strApiEndpoint)
        objHeaders = {
            "Content-Type": "application/json",
            "X-Dataverse-Key": self.strDATAVERSE_API_TOKEN
        }
        r = requests.request("GET", strApiEndpoint, headers=objHeaders)
        self.printResponseInfo(r)
        print("end DvViewCollection")
        

    # @title Delete a new Dataverse collection based on the collection alias
    def DvDeleteCollection(self):
        print("start DvDeleteCollection")
        strApiEndpoint = '%s/api/dataverses/%s' % (self.strDATAVERSE_DOMAIN, self._config["DATAVERSE_COLLECTION_START"]["alias"])
        print('making request: %s' % strApiEndpoint)
        objHeaders = {
            "Content-Type": "application/json",
            "X-Dataverse-Key": self.strDATAVERSE_API_TOKEN
        }
        r = requests.request("DELETE", strApiEndpoint, headers=objHeaders)
        self.printResponseInfo(r)
        print("end DvDeleteCollection")
        

    # @title List Dataverse collection contents based on the collection alias
    def DvViewCollectionContents(self):
        print("start DvViewCollectionContents")
        strApiEndpoint = '%s/api/dataverses/%s/contents' % (self.strDATAVERSE_DOMAIN, self._config["DATAVERSE_COLLECTION_START"]["alias"])
        print('making request: %s' % strApiEndpoint)
        objHeaders = {
            "Content-Type": "application/json",
            "X-Dataverse-Key": self.strDATAVERSE_API_TOKEN
        }
        r = requests.request("GET", strApiEndpoint, headers=objHeaders)
        self.printResponseInfo(r)
        print("end DvViewCollectionContents")

    
    # @title Create a new dataset
    def DvCreateDataset(self):
        print("start DvCreateDataset")
        strApiEndpoint = '%s/api/dataverses/%s/datasets' % (self.strDATAVERSE_DOMAIN, self._config["DATAVERSE_COLLECTION_START"]["alias"])
        print('making request: %s' % strApiEndpoint)
        objHeaders = {
            "Content-Type": "application/json",
            "X-Dataverse-Key": self.strDATAVERSE_API_TOKEN
        }
        r = requests.request("POST", strApiEndpoint, json=self._config["DATAVERSE_DATASET_PART"], headers=objHeaders)  # this only creates a dataset placeholder with partial information
        # r = requests.request("POST", strApiEndpoint, json=self._config["DATAVERSE_DATASET_FULL"], headers=objHeaders)  # full dataset properties not working (8/17)
        self.printResponseInfo(r)
        print("end DvCreateDataset")


    # @title Upload a dataset file
    def DvAddDatasetFile(self):
        print("start DvAddDatasetFile")
        strApiEndpoint = '%s/api/dataverses/%s/datasets' % (self.strDATAVERSE_DOMAIN, self._config["DATAVERSE_COLLECTION_START"]["alias"])
        print('making request: %s' % strApiEndpoint)
        objHeaders = {
            "Content-Type": "application/json",
            "X-Dataverse-Key": self.strDATAVERSE_API_TOKEN
        }
        r = requests.request("POST", strApiEndpoint, json=self._config["DATAVERSE_DATASET_PART"], headers=objHeaders)  # this only creates a dataset placeholder with partial information
        self.printResponseInfo(r)
        print("end DvAddDatasetFile")

    
    # @title General purpose method for printing response properties for testing
    # @argument r=response object from a requests.request()
    def printResponseInfo(self,r):
        print('-' * 40) # simple delineation so we know when this method is called in our output 
        print("json=",r.json())
        print("headers=",r.headers)
        print("response status=",r.status_code)

    # @title Initialize a file upload bucket to deposit our files (think of this as a dataset)
    # def initNewDataset(self):
    #     print("initialize dataset placeholder")
    #     objHeaders = {"Content-Type": "application/json"}
    #     objParams = {"access_token": self._config["ZENODO_API_KEY"]}
    #     r = requests.post(self._config["ZENODO_DOMAIN"]+"deposit/depositions",
    #         params=objParams,
    #         json={},
    #         headers=objHeaders)
    #     self.bucket_url = r.json()["links"]["bucket"]
    #     self.files_url = r.json()["links"]["files"]
    #     self.deposition_id = r.json()["id"]
    #     print("end startUpload")

    
    # @title Generates an MD5 hash for a given file (used to check against files being uploaded to prevent duplicate file uploads)
    # @argument File path
    def md5(self, fileToCheck):
        hash_md5 = hashlib.md5()
        with open(fileToCheck, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


    # @title Request the dataset contents from the Dataverse so we can compare with what we have locally
    def getDvDatasetContents(self):
        # use the requests module from Python to make a simple request to the Dataverse to check the contents
        url = self._config["DATAVERSE_DOMAIN"]+"/api/datasets/:persistentId/versions/:latest?persistentId="+self._config["DATAVERSE_DATASET_DOI"]
        headers = {
            "Content-Type": "application/json",
            "X-Dataverse-Key": self._config["DATAVERSE_API_TOKEN"]
        }
        r = requests.request("GET", url, headers=headers)
        self.dictDatasetContents = r.json()    # convert the response to a dict


    # @title Check that we have changes to a file before we try uploading to the Dataverse
    # @param File name, a description we will use to describe the file in the Dataverse
    def checkFileForUpload(self, strFileName, strFilePath):
        # check for an existing file in the Dataverse
        blnFileExists=False
        self.blnUploadFile=True
        strExistingMd5=''
        # print(self.dictDatasetContents['data']['files'])   # loop through the files in the dataset to find the one we want to replace
        for item in self.dictDatasetContents['data']['files']:
            if (item['label']==strFileName):
                blnFileExists=True
                strExistingMd5 = item['dataFile']['md5']
    
        if (blnFileExists): # if the file we are wanting to upload currently exists in the the Dataverse dataset, we check the MD5 checksum of both files and only upload if the MD5 differs
            newFileMd5 = self.md5(strFilePath+strFileName)
            if (newFileMd5==strExistingMd5):
                print("MD5 hashes match on "+strFileName+", so do not upload new file")
                self.blnUploadFile=False
            else:
                print("Something has changed with the file so we can upload a new version of the file to the Dataverse",newFileMd5,"==",strExistingMd5)
                

    # @title Return the notebook configuration
    def objConfig(self):
        return self._config



    # @title Add a column for image type (coded)
    # @param Dataframe series
    def imageType(self, series):
        if self.dictImgRef[series] != "":
            return self.dictImgRef[series]
        else:
            return series


    # @title Read the metadata file and return the contents
    def getDatasetMetadata(self):
        with open(self._config["DOCKER_WORKING_DIR"]+"/DatasetMetadata.json", mode='r') as jsonFile:   # read a copy of the metadata
            return json.load(jsonFile)


    # @title Retrieve the metadata for a file in the dataset
    def getFileMetadata(self,fileName):
        jsonDatasetMetadata=self.getDatasetMetadata()
        file_index = next((index for (index, obj) in enumerate(jsonDatasetMetadata['files']) if fileName in obj), "None")   # get the index of the file descriptions in the metadata
        if file_index!="None":
            return jsonDatasetMetadata['files'][file_index][fileName]
        return False


    # @title Give the image files new names and archive to the appropriate zip archive; this might take several minutes initially but subsequent runs are much faster since the code ignores files existing in the archives currently
    # @param Dataframe row
    def createPublicFile(self,row):
        newFN = row['PublicId']+'_'+row['E03USIMGT']+'.png'  # create new filename recoded (based on the side and body part); we should not need to add additional archives for each bodypart due to the small file size of each archive
        strPublicImageTypePath = self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+row['E03USIMGT']+'/'
        strPrivateImagePath = self._config["DOCKER_WORKING_DIR"]+'/images/unprocessed/'
        if not os.path.exists(strPublicImageTypePath):
            os.mkdir(strPublicImageTypePath)  # create archive path if not exists 
        blnPublicImageExists = os.path.isfile(strPublicImageTypePath+newFN)  # check if public image filename exists
        if (not blnPublicImageExists):    # copy the private file name to the archive rename the image file to public
            shutil.copy(strPrivateImagePath+row['filename'].replace('.jpg','.png'), strPublicImageTypePath+newFN) # copy private file to public archive and rename
        return newFN



    # @title Update the DatasetMetadata.json with new information on zip archives files to be sent to the Dataverse
    # @param Name of the zip achive, the dictionary object describing the archive
    def zipMetaUpdate(self,fileName,dictNewFile):
        jsonDatasetMetadata=self.getDatasetMetadata()
        file_index = next((index for (index, obj) in enumerate(jsonDatasetMetadata['files']) if fileName in obj), "None")   # get the index of the file descriptions in the metadata
        if file_index=="None":
            jsonDatasetMetadata['files'].append(dictNewFile)    # add data not yet in the metadata file
        else:
            jsonDatasetMetadata['files'][file_index] = dictNewFile  # update existing metadata
        # save the JSON data
        with open(self._config["DOCKER_WORKING_DIR"]+"/DatasetMetadata.json", mode='w') as jsonFile:
            jsonFile.write(json.dumps(jsonDatasetMetadata, indent=2))

    

    # @title Add the working directory to the file path
    def getWorkDirForPath(self, strLocalFilePath):
        return self._config["DOCKER_WORKING_DIR"]+strLocalFilePath


    # @title Upload a file to the Dataverse
    def DvUploadFile(self, strFileName, strLocalFilePath, strDataDescription, strDvDirectoryLabel, lstCatgories):
        self.checkFileForUpload(strFileName,self.getWorkDirForPath(strLocalFilePath))  # check that we are ready for upload
        if (self.blnUploadFile):
            # --------------------------------------------------
            # Using a "jsonData" parameter, add optional description + file tags
            # --------------------------------------------------
            params = dict(description=strDataDescription,
                        directoryLabel=strDvDirectoryLabel,
                        fileName=strFileName,
                        forceReplace="true",
                        categories=lstCatgories)
            print("uploadFileToDv:",strFileName,params)
            params_as_json_string = json.dumps(params)
            payload = dict(jsonData=params_as_json_string)
    
            fileobj = open(self.getWorkDirForPath(strLocalFilePath)+strFileName, 'rb')  # read the file
            objFile = {'file': (strFileName, fileobj)}   # we have the new file object to save to the Dataverse
        
            # -------------------
            # Make the request
            # -------------------
            print('-' * 40)
            print('making request: %s' % self.strDvUrlPersistentId)
            r = requests.post(self.strDvUrlPersistentId, data=payload, files=objFile)
        
            # -------------------
            # Print the response
            # -------------------
            print('-' * 40)
            print(r.json())
            print(r.status_code)
        print("--end uploadFileToDv--")

    # @title Lets check our DatasetMetadata.json file and make sure our variables are listed for `F1_SUBJECT` and `F2_IMAGE` data
    def metadataMatch(self,fileName, filePath, objDtype):
        dfObj = pd.read_csv(self._config["DOCKER_WORKING_DIR"]+"/"+filePath, skiprows=[1], header=0, dtype=objDtype)  # read data file
        dictMetadata = self.getFileMetadata(fileName)    # retrieve the metadata we are checking
        listMdColumns = [d.get('name') for d in dictMetadata['variables']]     # use list comprehension to extract a list of variable names from our metadata file
        for colDf in dfObj.columns:   # checking the columns of the data file and throw an error if the variable is missing from the metadata
            if (colDf in listMdColumns):
                print(colDf+" in the "+fileName+" metadata")
            else:
                raise RuntimeError("***ERROR: Missing variable "+colDf+" in the "+fileName+" metadata***")
    
            file_index = next((index for (index, obj) in enumerate(dictMetadata['variables']) if colDf in obj['name']), "None")   # get the index of the variable in the metadata
            if file_index!="None" and dictMetadata['variables'][file_index]['value']['format']=="categorical":  # if the variable is a categorical format
                listVarCats = list([d for d in dictMetadata['variables'][file_index]['value']['category']])
                print(listVarCats)
                for catKey in dfObj[colDf].unique():
                    if (str(catKey) not in listVarCats):
                        print(str(catKey)+" is missing")
                # print("total number of distinct values for",colDf,": ",dfObj[colDf].unique())
                # if df_qKneePain["SubjectId"].count()!=df_qKneePain["SubjectId"].unique().size:
                #     raise RuntimeError("***ERROR: The df_qKneePain data contains a duplicate subject record needing to be resolved***")
            
        print("All variables in the "+fileName+" data file are accounted for in the metadata.")
        # once all variables are defined in the metadata we want to check our categorical variables to ensure the values found in the data match the metadata


    # @title Check that the variables are accounted for in the reference metadata
    def checkReferenceMetadata(self):
        print("check metadata")
        self.metadataMatch("F1_SUBJECT", "F1_SUBJECT.csv", {"E03PASKR":"Int64","E03PASKL":"Int64","E03RADRPAKKL":"Int64","E03RADLPAKKL":"Int64","E03AGE":"Int64"})
        self.metadataMatch("F2_IMAGE", "F2_IMAGE.csv", {"E03USIMGT":"Int64","E03USIMGD":"Int64"})
        print("--end checkMetaMatch")


    # @title Compare the image files and folders to the our metadata describing the images. The data should match. We will also update the image metadata in our metadata reference file as well as upload the images to the Dataverse if they have changed since last uploading.
    # ----- We are not using this function because pushing individual images to the dataset is extremely slow and inefficient
    # def publishUsImages(self):
    #     print("create public US image metadata")
    #     self.getDvDatasetContents()
    #     dfGetImageData = pd.read_csv(self._config["DOCKER_WORKING_DIR"]+"/dfGetImageData.csv",skiprows=[1], header=0) # read the raw image metadata
    #     # we can now drop the original columns we will be excluding from the dataset (DO NOT REMOVE THESE LINES)
    #     dfGetImageData.drop(columns=["PrivateId"], inplace = True)
    #     dfGetImageData.drop(columns=["SubjectId"], inplace = True)
    #     dfGetImageData.drop(columns=["filename"], inplace = True)
    #     dfGetImageData.drop(columns=["BodyPart"], inplace = True)
    #     # rename the original columns
    #     dfGetImageData.rename(columns={"PublicId": "E03SUBJECTID"}, inplace = True)
        
    #     # print ("processing for upload of folder",self.dictImgRef[key])
    #     for row in tqdm(dfGetImageData.itertuples()): # loop through the list of images in the metadata (and add progress bar)
    #         # print(self.dictImgTypeRef[str(row[2])])
    #         strFileName=row[3]
    #         strLocalFilePath='/images/archive/'+str(row[2])+"/"
    #         strDataDescription=self.dictImgTypeRef[str(row[2])]+" image"
    #         strDvDirectoryLabel="data/image/ultrasound/"+str(row[2])
    #         lstCatgories=['data', 'images', 'ultrasound']
    #         # print("information for image upload strFileName=",strFileName,"strLocalFilePath=",strLocalFilePath,"strDataDescription=",strDataDescription,"strDvDirectoryLabel=",strDvDirectoryLabel,"lstCatgories=",lstCatgories)
            
    #         self.uploadFileToDv(strFileName, strLocalFilePath, strDataDescription, strDvDirectoryLabel, lstCatgories)  # check that we are ready for upload
    #     # print(dictImageArchiveStats)
    #     # output main demographics data to STATA
    #     dfGetImageData.to_stata(self._config["DOCKER_WORKING_DIR"]+"/"+self._config["F2_IMAGE"], version=118, variable_labels=F2_IMAGE_variable_labels, 
    #     data_label=F2_IMAGE_data_label, value_labels=F2_IMAGE_value_labels) 
    #     # output main demographics data to CSV
    #     dfGetImageData.to_csv(self._config["DOCKER_WORKING_DIR"]+"/F2_IMAGE.csv", index=False, compression=None) # write the KL grades to a file
    #     print("--end compileUsImgMetadata--")


    # @title Upload image archives to the dataset (if they have changes needing to be published)
    def uploadImageArchives(self):
        print("validate archives")
        self.getDvDatasetContents()
        dfGetImageData = pd.read_csv(self._config["DOCKER_WORKING_DIR"]+"/dfGetImageData.csv",skiprows=[1], header=0) # read the raw image metadata
        # we can now drop the original columns we will be excluding from the dataset (DO NOT REMOVE THESE LINES)
        dfGetImageData.drop(columns=["PrivateId"], inplace = True)
        dfGetImageData.drop(columns=["SubjectId"], inplace = True)
        dfGetImageData.drop(columns=["filename"], inplace = True)
        dfGetImageData.drop(columns=["BodyPart"], inplace = True)
        # rename the original columns
        dfGetImageData.rename(columns={"PublicId": "E03SUBJECTID"}, inplace = True)
        intTotalImagesChecked=0
        dictImageArchiveStats={}
        # print(self.dictImgRef)
        # for each image archive we check the contents match the metadata and save the metadata to our main reference file
        # ***NOTE: since we are using `itertuples` for efficiency reasons, we need to know the column number of the row values we are comparing (instead of searching column names, which is easier but slower to process)
        for key in self.dictImgRef:
            print("looking for archive",self.dictImgRef[key])
            isExisting = os.path.isfile(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+self.dictImgRef[key]+'.zip')  # check if image archive exists
            if (not isExisting):
                print("create zip archive for",self.dictImgRef[key])
                # try to zip archive the folder of images if it does not exist
                shutil.make_archive(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+self.dictImgRef[key], 'zip', self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+self.dictImgRef[key])
                # with zipfile.PyZipFile(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+row['E03USIMGT']+'.zip', 'a') as myzip:
                #     myzip.write(self._config["DOCKER_WORKING_DIR"]+'/images/unprocessed/'+self.dictImgRef[key],newFN)

            dictImageArchiveStats[self.dictImgRef[key]] = {"fileCount":0}
            print ("processing for upload",self.dictImgRef[key]+'.zip')
            with zipfile.PyZipFile(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+self.dictImgRef[key]+'.zip', 'r') as myzip:
                for row in dfGetImageData.itertuples(): # loop through the list of images in the metadata
                    if str(row[2])==str(self.dictImgRef[key]) and row[3] not in myzip.namelist():        # check if a file exists within the zip archive
                        raise RuntimeError("***ERROR: Missing file "+row[3]+" in the "+self.dictImgRef[key]+".zip archive***")
                    if str(row[2])==str(self.dictImgRef[key]):
                        intTotalImagesChecked += 1
                        dictImageArchiveStats[self.dictImgRef[key]]['fileCount'] += 1
            self.checkZipForUpload(self.dictImgRef[key],self.dictImgTypeRef[self.dictImgRef[key]]+', ultrasound image files', dictImageArchiveStats[self.dictImgRef[key]]['fileCount'])   # we check a zip file to see if we can upload new content for it
        print(intTotalImagesChecked, "images checked in the archives with no missing")       # we made it this far so we can move on
        print(dictImageArchiveStats)
        # output main demographics data to STATA
        dfGetImageData.to_stata(self._config["DOCKER_WORKING_DIR"]+"/"+self._config["F2_IMAGE"], version=118, variable_labels=self.F2_IMAGE_variable_labels, 
        data_label=self.F2_IMAGE_data_label, value_labels=self.F2_IMAGE_value_labels) 
        # output main demographics data to CSV
        dfGetImageData.to_csv(self._config["DOCKER_WORKING_DIR"]+"/F2_IMAGE.csv", index=False, compression=None) # write the KL grades to a file
        # print(dfGetImageData)
        print("--end uploadImageArchives--")


    # @title Delete a file in a dataset
    def deleteDvFile(self,intDataFileId):
        strDvUrl = '%s/api/files/%s' % (self._config["DATAVERSE_DOMAIN"], intDataFileId)
        print('delete request: %s' % strDvUrl)
        r = requests.delete(strDvUrl, headers = {"X-Dataverse-key": self._config["DATAVERSE_API_TOKEN"]})
        # -------------------
        # Print the response
        # -------------------
        print('-' * 40)
        print(r.json())
        print("deleted file status:",r.status_code)
        if (r.status_code!=200):
            raise RuntimeError("***ERROR: The file deletion could not be completed***")
        # time.sleep(1) # try to ensure the file is removed before moving on


    
    # @title Upload a zip file to the Dataverse
    # @param Archive name, a description we will use to describe the file in the Dataverse
    def DvUploadZip(self,zipNumber,zipDescription):
        self.removeTempArchive(zipNumber)
        # create a placeholder temporary file first
        with zipfile.PyZipFile(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+zipNumber+'c.zip', 'w') as myzip1:
            pass
        # double zip the file into a temporary zip
        with zipfile.PyZipFile(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+zipNumber+'c.zip', 'w') as myzip:
            myzip.write(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+zipNumber+'.zip',zipNumber+'.zip')
            time.sleep(0.5) # try to ensure the archive is created before moving on
            pass
        fileobj = open(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+zipNumber+'c.zip', 'rb')  # read the double zipped file
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
        # -------------------
        # Make the request
        # -------------------
        print('-' * 40)
        print('making request: %s' % self.strDvUrlPersistentId)
        r = requests.post(self.strDvUrlPersistentId, data=payload, files=files)
        # -------------------
        # Print the response
        # -------------------
        print('-' * 40)
        print(r.json())
        print(r.status_code)


    # @title Remove the archive we create as a temporary placeholder
    def removeTempArchive(self,zipNumber):
        isExisting = os.path.isfile(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+zipNumber+'c.zip')  # check if image archive exists
        if (isExisting):
            print("removing temp archive",zipNumber+'c.zip')
            os.remove(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+zipNumber+'c.zip')    # remove temp archive
            time.sleep(0.5) # try to ensure the archive is removed before moving on

    
    # @title Check that we have changes to a zip file before we try uploading to the Dataverse
    # @param Archive name, a description we will use to describe the file in the Dataverse
    def checkZipForUpload(self, zipNumber,zipDescription,intFileCount):
        # check for an existing file in the Dataverse
        strNewFileToUpload = zipNumber+'.zip'
        blnFileExists=False
        blnUpload=True
        strExistingMd5=''
        for item in self.dictDatasetContents['data']['files']:
            intDataFileId=0
            if (item['label']==strNewFileToUpload):
                blnFileExists=True
                strExistingMd5 = item['dataFile']['md5']
                print(item)
                intDataFileId=item['dataFile']['id']
                
        if (blnFileExists): # if the new file, we plan to upload, currently exists in the the Dataverse dataset, we check the MD5 checksum of the new file
            newFileMd5 = self.md5(self._config["DOCKER_WORKING_DIR"]+'/images/archive/'+strNewFileToUpload)
            if (newFileMd5==strExistingMd5):
                print("MD5 hashes match on "+strNewFileToUpload+", so do not upload new file")
                blnUpload=False
            else:
                print("Something has changed with the file so we can upload a new version of the file to the Dataverse",newFileMd5,"==",strExistingMd5)
        if (blnUpload):  # we will upload the file as long as it does not exist currently or the existing file is different from the newer file
            if (blnFileExists and intDataFileId!=0):
                self.deleteDvFile(intDataFileId)
            self.uploadZip(zipNumber,zipDescription)
            dictNewFile={str(zipNumber): {"filename": zipNumber+".zip", "fileCount":intFileCount,"directoryLabel": "data/image/ultrasound", "description": "This file contains an archive of "+self.dictImgTypeRef[zipNumber]+", ultrasound image files. There should only be one image per subject in this archive. Images are saved in lossless .png format.","updatedOnDataverse": str(datetime.now().astimezone())} }   # create the metadata for each zip archive
            self.zipMetaUpdate(zipNumber,dictNewFile)      # save the zip archive metadata to the main DatasetMetadata.json file

    # @title Generate a simple table view of the dataset contents
    def viewDatasetContents(self):
        self.getDvDatasetContents()
        dfFileList = pd.DataFrame(self.dictDatasetContents['data']['files'])   # assign the file metadata to a dataframe for sorting and display
        display(HTML(dfFileList[['label','directoryLabel','categories','description']].sort_values(by=['directoryLabel', 'label']).to_html()))


    def DvUploadMetadata(self):
        self.getDvDatasetContents()
        print("for a list of files remaining to upload to the dataset, read the metadata from the DatasetMetadata.json file and upload the files to the Dataverse, and update date uploaded to dataset")
        listFilesToUpload = ['F1_SUBJECT', 'F2_IMAGE', 'DatasetMetadata','example.us.image']
        for strFileName in listFilesToUpload:
            dictMetadata = self.getFileMetadata(strFileName)
            strExistingMd5=''
            blnUpload=True
            blnFileExists=False
            intDataFileId=0
            print("checking "+strFileName)
            
            # ***************** we need to check the MD5 of these files before sending to the Dataverse to prevent duplicates
            for dvFile in self.dictDatasetContents['data']['files']:   # for each dataverse file
                if 'originalFileName' in dvFile['dataFile']:    # NOTE: STATA files are unique in the Dataverse in that they are not labeled the same way due to the original format switched to tab delimited format, so we need to check for an `originalFileName` element
                    print("originalFileName",dvFile)
                    if (dvFile['dataFile']['originalFileName']==dictMetadata['filename']):
                        intDataFileId = dvFile['dataFile']['id']
                        # print(dvFile['dataFile']['originalFileName']+"---"+dictMetadata['filename'])
                        blnFileExists=True
                        strExistingMd5 = dvFile['dataFile']['md5']
                        break
                else:
                    if (dvFile['label']==dictMetadata['filename']):     # check files other than STATA in the Dataverse
                        print("not originalFileName",dvFile)
                        intDataFileId = dvFile['dataFile']['id']
                        # print(dvFile['label']+" label---"+dictMetadata['filename'])
                        blnFileExists=True
                        strExistingMd5 = dvFile['dataFile']['md5']
                        break
        
            if (blnFileExists): # if the new file we are uploading currently exists in the the Dataverse dataset, we check the MD5 checksum of the new file
                newFileMd5 = self.md5(self._config["DOCKER_WORKING_DIR"]+"/"+dictMetadata['filename'])
                if (newFileMd5==strExistingMd5):
                    print("MD5 hashes match on "+dictMetadata['filename']+", so do not upload new file")
                    blnUpload=False
                else:
                    print(newFileMd5+"=="+strExistingMd5+" Something has changed with the "+dictMetadata['filename']+" file so we can upload a new version of the file to the Dataverse") # : ",newFileMd5,"==",strExistingMd5)
        
            if (blnUpload):
                # --------------------------------------------------
                # Using a "jsonData" parameter, add optional description + label
                # --------------------------------------------------
                params = dict(description=dictMetadata['description'],
                            directoryLabel=dictMetadata['directoryLabel'],
                            forceReplace="true",
                            categories=dictMetadata['categories'])
                # print(dictMetadata)  # testing
                fileData = open(self._config["DOCKER_WORKING_DIR"]+"/"+dictMetadata['filename'], 'rb')  # read file contents
                fileObj = {'file': (dictMetadata['filename'], fileData)}
                params_as_json_string = json.dumps(params)
                payload = dict(jsonData=params_as_json_string)
                # if (intDataFileId): # NOTE: if the file exists then we replace it using the existing file ID (this is important for STATA files otherwise the STATA files will not be replaced and duplicate STATA files will be added to the dataset)
                #     url_persistent_id = '%s/api/files/%s/replace?&key=%s' % (self._config["DATAVERSE_DOMAIN"], intDataFileId, self._config["DATAVERSE_API_TOKEN"])   # replace file by ID
                # else

                print("checking blnFileExists=",blnFileExists,"intDataFileId=",intDataFileId)
                if (blnFileExists and intDataFileId!=0): # delete the existing file first
                    self.deleteDvFile(intDataFileId)
                                    
                url_persistent_id = self.strDvUrlPersistentId   # Add file using the Dataset's persistentId
                
                print("updated using "+url_persistent_id)
                # Make the request
                print('-' * 40)
                print('making request: %s' % url_persistent_id)
                r = requests.post(url_persistent_id, data=payload, files=fileObj)
                # Print the response
                print('-' * 40)
                print(r.json())
                print(r.status_code)
        print("--end uploadMetadata--")