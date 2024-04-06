
# -*- coding: utf-8 -*-
from requests import get
import util.file as file

FabricURL = "http://meta.fabricmc.net/v2/versions/loader/{version}/{FabricLoaderVersion}/{InstallerVersion}/server/jar"

def Download(version="1.20.4",FabricLoaderVersion="0.15.9",InstallerVersion="1.0.0"):
    url = FabricURL.replace("{version}",version).replace("{FabricLoaderVersion}",FabricLoaderVersion).replace("{InstallerVersion}",InstallerVersion)
    response = get(url=url)
    if response.status_code == 200:
        with open(f"{file.getFolder()}\\jar\\{version}-{FabricLoaderVersion}-{InstallerVersion}.jar", "wb") as fichier_local:
            fichier_local.write(response.content)
        print("Download Done.")
    else:
        print("Download Failed. Status code :", response.status_code)
        

if __name__ == "__main__":
    Download()