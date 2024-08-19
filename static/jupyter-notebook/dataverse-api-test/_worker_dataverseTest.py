from faker import Faker
from faker.providers import profile
import json
import os
# import shutil
from os.path import exists
from DvApiMod import ObjDvApi  # pull in the Dataverse API functions from our external file

# @title By placing all of our Python function within a class object, it makes it much easier for information to be used across functions without needing to explicitly passing them into each function (instead we pass the entire Worker object into the functions so each function can do what it needs with the object)
class Worker:
    # @param strEnvironment (ex. demo or prod, would represent the environment you wish for the notebook code to run against)
    def __init__(self,strConfigFile):
        f = open (strConfigFile, "r") # read the notebook configuration settings
        self._config = json.loads(f.read())
        f.close()
        self.ObjDvApi = ObjDvApi(self._config) # here we pass our notebook configuration to the ObjDvApi module and extend the functionality of this object with the ObjDvApi object
        self.strUploadPath = self._config["strDOCKER_WORKING_DIR"]+self._config["strLOCAL_UPLOAD_DIR"] # creating this because we will reuse it several places
        print("Finished installing and importing modules for the",strConfigFile,"environment") # it is a good idea to end your functions with a print statement so you can visually see when the function ends in the notebook output


    # @title Generate fake data for testing
    def createSampleData(self):
        fake = Faker('en_US')
        fake.add_provider(profile)
        lstProfiles = []
        for _ in range(5):  # create five fake profile records 
            lstProfiles.append(fake.profile(['name','username','address','mail']))
        # print(lstProfiles)
        return lstProfiles


    # @title Generate files for the dataset
    def createTestFiles(self):
        print("start createTestFiles")
        if not os.path.exists(self.strUploadPath):
            os.mkdir(self.strUploadPath)  # create file path if not exists for storing our sample data
        for obj in self._config["lstTEST_FILES"]:
            with open(os.path.join(self.strUploadPath,obj["strFileName"]), mode='w') as objFile:
                objFile.write(json.dumps(self.createSampleData(), indent=2))
                objFile.close() # *** WE MUST CLOSE THE FILE AFTER CREATING IT OTHERWISE WE WILL NOT BE ABLE TO OPEN THE FILE FOR UPLOAD ***
                # self.uploadFile(obj["name"], obj["type"]) # we will do this in a separate function
        print("end createTestFiles")


    # @title Upload files to the dataset
    def uploadTestFiles(self):
        print("start uploadTestFiles")
        for objFile in self._config["lstTEST_FILES"]:
            objFile["strUploadPath"] = self.strUploadPath # we add a few extra properties to the object before sending it to the addDatasetFile method
            objFile["strDvUrlPersistentId"] = 'asdf'
            self.ObjDvApi.addDatasetFile(objFile) # we simply pass the objFile so we can use the configuration file to determine the elements linked to the object (spare us from altering the arguments of the addDatasetFile method
        print("end uploadTestFiles")