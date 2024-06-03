import json 
import sys
import json
import os 
from typing import List

from tools import *


## Cache the old environment in case we need it 
__root_environ__ = os.environ

## Build an environment for use in this script 
script_environ = os.environ.copy()
os.environ = script_environ

ws = Workspace()


__PURGE_EXISTING__ = True
__LOGGING__ = False

if __name__ == "__main__": 

    ##
    ##
    ## Parse Args: 
    ## Keep it simple to just the JSON file
    ##
    if len(sys.argv) < 2: 
        print('Usage: json_file')
        sys.exit(1)

    input_json = sys.argv[1]
    with open(input_json, 'r') as of: 
        json_data = json.load(of)

    ##
    ##
    ## Build Basic Workspace Folder Structure
    ## Do this outside the workspace so that we can build 
    ## The custom environment to resolve links in later  
    ##
    for keyed_path in json_data['workspace_paths']:

        ep = EnvPath(keyed_path)
        script_environ[ep.env_key()] = ep.env_value()
        ws.AddToWorkspace(ep)

    if __PURGE_EXISTING__: 
        ws.PurgeExistingKeyPaths()

    ws.BuildFileStructure()
    if __LOGGING__: 
        print(ws)
        
    ##
    ##
    ## Build all the generated files required by the workspace  
    ##
    ws.BuildGeneratedEnvFile(json_data['generated']['env_var'])
    ws.BuildGeneratedAliases(json_data['generated']['aliases'])
    ws.BuildGeneratedFunctions(json_data['generated']['func'])
    # ws.BuildGeneratedJumpFile(json_data['generated']['summary']['name'])
    ws.BuildJumpFile(json_data['generated']['summary'])

    ##
    ##
    ## Finally, install the repo into the workspace so that we can 
    ## manage the links directly  
    ##
    ws_builder_root = os.path.dirname(os.path.abspath(__file__))
    ws_root = os.path.dirname(ws_builder_root)

    ws.CopyRepoToWorkspace(ws_root)
    ws.LinkRepoDirsInWorkspace()

    