
# -*- coding: utf-8 -*-
from requests import get
import util.file as file
import os

FabricURL = "http://meta.fabricmc.net/v2/versions/loader/{version}/{FabricLoaderVersion}/{InstallerVersion}/server/jar"
VanillaURL = "http://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar"


def DownloadFabricJAR(version="1.20.4",FabricLoaderVersion="0.15.9",InstallerVersion="1.0.0"):
    url = FabricURL.replace("{version}",version).replace("{FabricLoaderVersion}",FabricLoaderVersion).replace("{InstallerVersion}",InstallerVersion)
    dirPath = f"{file.getFolder()}\\jar\\fabric\\{version}"
    response = get(url=url)
    if response.status_code == 200:
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        with open(f"{file.getFolder()}\\jar\\fabric\\{version}\\server.jar", "wb") as fichier_local:
            fichier_local.write(response.content)
        print("Download Done.")
    else:
        print("Download Failed. Status code :", response.status_code)
        

def DownloadLastVanillaJAR():
    url = VanillaURL
    response = get(url=url)
    dirPath = f"{file.getFolder()}\\jar\\vanilla"
    if response.status_code == 200:
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        with open(f"{file.getFolder()}\\jar\\vanilla\\server.jar", "wb") as fichier_local:
            fichier_local.write(response.content)
        print("Download Done.")
    else:
        print("Download Failed. Status code :", response.status_code)
        

DownloadFabricJAR()
DownloadLastVanillaJAR()