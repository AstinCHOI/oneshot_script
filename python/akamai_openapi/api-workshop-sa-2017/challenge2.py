#! /usr/bin/env python
                                                                                                                         
import requests, logging, json, sys
from http_calls import EdgeGridHttpCaller
from random import randint
from akamai.edgegrid import EdgeGridAuth
from config import EdgeGridConfig
from urlparse import urljoin
import urllib

session = requests.Session()                                                                                             
debug = False
verbose = False
section_name = "default"
                                                                                                                         
config = EdgeGridConfig({"verbose": debug},section_name)
                                                                                                                         
if hasattr(config, "debug") and config.debug:
  debug = True
                                                                                                                         
if hasattr(config, "verbose") and config.verbose:
  verbose = True
                                                                                                                         
session.auth = EdgeGridAuth(                                                                                             
    client_token=config.client_token,                                                                                    
    client_secret=config.client_secret,                                                                                  
    access_token=config.access_token                                                                                     
)                                                                                                                        
baseurl = '%s://%s/' % ('https', config.host)
httpCaller = EdgeGridHttpCaller(session, debug, verbose, baseurl)                                                        
                                                                                                                         
# Set options
targetProperty = "sa2017api_bangalore_47.edgesuite.net"
newOrigin = "neworigin.domain.tld"
                                                                                                                         
# List Groups
groupsResult = httpCaller.getResult("/papi/v0/groups/")
                                                                                                                         
for each in groupsResult['groups']['items']:
    try:
            # For each group
            requestParams = {                                                                                        
                    "groupId": each['groupId'],
                    "contractId": each['contractIds'][0]
                    }                                                                                                
                                                                                                                     
            # List Properties
            propResult = httpCaller.getResult("/papi/v0/properties/", requestParams)
                                                                                                                     
            for each in propResult['properties']['items']:
                try:
                    if each['propertyName'].upper() == targetProperty.upper():
                            propertyDeets = {                                                                
                                "propertyId": each['propertyId'],
                                "groupId":each['groupId'],
                                "contractId":each['contractId'],
                                "productionVersion": each['productionVersion'],
                                "stagingVersion": each['stagingVersion']
                            }                                                                        
                except:
                        continue
    except:
            continue
                                                                                                                         
# Check we found the property details
try:
    print "FOUND!\n" + propertyDeets['propertyId'] + " in " + propertyDeets['groupId'] + " on " + propertyDeets['contractId']
except:
    print "Property not found."
    quit()                                                                                                           
                                                                                                                         
# Set the groupId & contractId we will need for future API Calls
requestParams = {                                                                                                        
    "groupId": propertyDeets['groupId'],
    "contractId": propertyDeets['contractId']
}                                                                                                                

# Get a rule tree for latest version on Production
ruleTree = httpCaller.getResult("/papi/v0/properties/"+ propertyDeets['propertyId'] + "/versions/" + str(propertyDeets['productionVersion']) + "/rules/", requestParams)
                                                                                                                         
                                                                                                                                                                                                                                                  
# Update Origin server in local rule tree
for behavior in ruleTree['rules']['behaviors']:
        if behavior['name'] == "origin":
                oldOrigin = behavior['options']['hostname']
                behavior['options']['hostname'] = newOrigin
                                                                                                                         
                                                                                                                         
# Create a new version
requestPayload = {                                                                                                       
    "createFromVersion": propertyDeets['productionVersion']
}                                                                                                                
createVersion = httpCaller.postResult("/papi/v0/properties/"+ propertyDeets['propertyId'] + "/versions/",json.dumps(requestPayload), requestParams)
                                                                                                                         
# List versions
propertyVersions = httpCaller.getResult("/papi/v0/properties/"+ propertyDeets['propertyId'] + "/versions/", requestParams)
                                                                                                                         
# find the most recent version in the list
newVersion = propertyVersions['versions']['items'][0]['propertyVersion']
                                                                                                                         
# PUT Rule tree
# path = "/papi/v0/properties/"+ propertyDeets['propertyId'] + "/versions/" + str(propertyDeets['productionVersion']) + "/rules/"
path = "/papi/v0/properties/"+ propertyDeets['propertyId'] + "/versions/" + str(newVersion) + "/rules/"
updateRules = httpCaller.putResult(path, json.dumps(ruleTree), requestParams)

# Debug
print(path)

# Check Origin server in rule tree
for behavior in updateRules['rules']['behaviors']:
    if behavior['name'] == "origin":
        updatedOrigin = behavior['options']['hostname']
try:
    for each in updateRules['errors']:
        print each['errorLocation']
        print each['type']
        print each['detail'] + "\n"
except:
    print "No Errors"
                                                                                                                         
try:
    for each in updateRules['warnings']:
        print each['errorLocation']
        print each['type']
        print each['detail'] + "\n"
except:
    print "No Warnings"
                                                                                                                         
print "Property Version " + str(updateRules['propertyVersion']) + " updated"
print "Origin changed from '" + oldOrigin + " to '" + updatedOrigin + "'"