import json
# %load_ext autoreload
# %autoreload all
# we need the 'autoreload' above if we are actively making changes to the worker.py module and want to reload any changes to the module without restarting the notebook kernel
# NOTE: if we make changes to the worker script we need to rerun this code block for the notebook to use the new edits

from DvApiMod import ObjDvApi  # pull in the Dataverse API functions from our external file

# @title By placing all of our Python function within a class object, it makes it much easier for information to be used across functions without needing to explicitly passing them into each function (instead we pass the entire Worker object into the functions so each function can do what it needs with the object)
class Worker:
    # @param strEnvironment (ex. demo or prod, would represent the environment you wish for the notebook code to run against)
    def __init__(self,strConfigFile):
        f = open (strConfigFile, "r") # read the notebook configuration settings
        self._config = json.loads(f.read())
        f.close()
        self.ObjDvApi = ObjDvApi(self._config) # here we pass our notebook configuration to the ObjDvApi module
        print("Finished installing and importing modules for the",strConfigFile,"environment")
        