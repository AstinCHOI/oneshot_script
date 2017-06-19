#! /usr/bin/env python
# Reference URL: https://developer.akamai.com/api/luna/papi/resources.html#getaproperty
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
targetPropertyId = False
                                                                                                                        
                                                                                                                        
config = EdgeGridConfig({"verbose":debug}, section_name)
                                                                                                                        
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
                                                                                                                        
#Set Name of target property
targetProperty = "sa2017api_bangalore_47.edgesuite.net"
                                                                                                                        
                                                                                                                        
# ===============================================================================
# Our first API Call
# We need to know what groups exist in the account
# Reference: https://developer.akamai.com/api/luna/papi/resources.html#listgroups
# ===============================================================================

groupsResult = httpCaller.getResult("/papi/v0/groups/")
                                                                                                                        
# DEBUG
# print groupsResult
# quit()
                                                                                                                        
                                                                                                                        
# ===============================================================================
# The resulting JSON response is now stored in "groupsResult"
# We know the structure from the Developer Portal
# {"groups": { "items": [
# So let's loop through each Luna Group
# ===============================================================================
for each in groupsResult['groups']['items']:
        try:
                # DEBUG
                # print each['groupName'] + " : " + each['groupId'] + " : " + each['contractIds'][0]
                                                                                                                        
                                                                                                                        
                # ===============================================================================
                # We now need to call out and get the list of properties in each group we got
                # returned in the first call.
                # Reference: https://developer.akamai.com/api/luna/papi/resources.html#listproperties
                # First, we have to put the appropriate bits of information into the Req Params
                # ===============================================================================
                requestParams = {                                                                                       
                        "groupId": each['groupId'],
                        "contractId": each['contractIds'][0]
                }                                                                                                       
                                                                                                                        
                # ===============================================================================
                # Then issue the API call:
                # ===============================================================================
                propsResult = httpCaller.getResult("/papi/v0/properties/", requestParams)
                                                                                                                        
                # ===============================================================================
                # The resulting JSON response is now stored in "propsResult"
                # We know the structure from the Developer Portal too
                # {"properties": { "items": [
                # So let's loop through each property
                # ===============================================================================
                for each in propsResult['properties']['items']:
                        try:
                                                                                                                        
                                # DEBUG
                                print "\t" + each['propertyName'] + " : " + each['propertyId']
                                                                                                                        
                                # ===============================================================================
                                # We need to see if the property matches our target (.upper() to normalise)
                                # ===============================================================================
                                if each['propertyName'].upper() == targetProperty.upper():
                                                                                                                        
                                        # ===============================================================================
                                        # Set the targetPropertyId to the current property if it matches and stop looping
                                        # ===============================================================================
                                        targetPropertyId = each['propertyId']
                                        targetGroupId = each['groupId']
                                        targetContractId = each['contractId']
                        except:
                                continue
        except:
                continue
                                                                                                                        
                                                                                                                        
                                                                                                                        
if targetPropertyId:
        print "FOUND!\n" + targetProperty + " is " + targetPropertyId + " in " + targetGroupId + " on " + targetContractId                                                                                                                      
else:
        print "NOT FOUND :("  