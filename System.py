#OpenSeas - AssetVerification

#SystemImports
from asyncio import sleep
import json
from telnetlib import PRAGMA_HEARTBEAT
import requests
import time

#AssetTable
Asset_Names = [] # Insert Chosen Names Here for Display
Asset_Contract_Address = ("") # Insert Contract Address Here
Asset_Contract_IDs = [] # Insert All Contract IDs Here

#PreSetRequest
OpenSeas_StartURL = "https://api.opensea.io/api/v1/asset/"
OpenSeas_EndURL = "/owners?format=json&limit=50&order_by=created_date&order_direction=desc"

#Functions
def FindAssetOwners(User_Wallet):
    #FunctionVariables
    System_Counter = 0

    for Contract_ID in Asset_Contract_IDs:

        URL_Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        URL_Address = (OpenSeas_StartURL + Asset_Contract_Address + "/" + Contract_ID + OpenSeas_EndURL)

        URL_Response = requests.get(URL_Address, headers = URL_Header)
        JSON_Response = URL_Response.text

        JSON_Data = json.loads(JSON_Response)
        JSON_OwnerTable = JSON_Data["owners"]

        for Asset_Owners in JSON_OwnerTable:
            Asset_Owner = Asset_Owners["owner"]
            Asset_Owner_Address = Asset_Owner["address"]

            if Asset_Owner_Address == User_Wallet:
                print(Asset_Names[System_Counter])

        System_Counter = System_Counter + 1

def GetUserWallet():
    User_Wallet = input(str("Input Your Public Wallet Address: "))
    FindAssetOwners(User_Wallet)

GetUserWallet()
