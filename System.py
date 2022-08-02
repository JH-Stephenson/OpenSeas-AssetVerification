#OpenSeas - AssetVerification

#SystemImports
from asyncio import sleep
import json
import requests
import time

#AssetTable
Asset_Names = ["Orchid", "Planeterium", "Orenda", "Professor Eve", "Grimoire", "PAL"]
Asset_Contract_Address = ["0xa342f5d851e866e18ff98f351f2c6637f4478db5"]
Asset_Contract_IDs = ["82344359815298119800542564839349904627894644716845183454722829717648818845699"]

#PreSetRequest
OpenSeas_StartURL = "https://api.opensea.io/api/v1/asset/"
OpenSeas_EndURL = "/owners?format=json&limit=20&order_by=created_date&order_direction=desc"

#UserInput
User_Wallet = ""

#Functions
def FindAssetOwners():
    #FunctionVariables
    System_Counter = 0
    JSON_Key = ""

    for Contract_ID in Asset_Contract_IDs:
        System_Counter = System_Counter + 1

def GetUserWallet():
    User_Wallet = input(str("Input Your Public Wallet Address: "))

GetUserWallet()
FindAssetOwners()