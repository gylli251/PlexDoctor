import subprocess
import json
import os
from os import path
from plexapi.myplex import MyPlexAccount
from utils.logger import log

CONFIG_FILE = "plex_doctor_config.json"
DOCKER = "docker"
WINDOWS = "windows"
LINUX = "linux"

# Get config variables
def set_config():
    if path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as json_file:
            try:
                log.info("Setting config from config file...")
                config = json.load(json_file)
            except Exception:
                log.error("Config file not formatted correctly")
    else:
        log.error(f"[{CONFIG_FILE}] not found")
        exit()
    return config
 

def restart_docker():
    log.info("Restarting container...")
    subprocess.run("docker", "restart", "plex", shell=True)


def restart_windows(plex_path):  # Not implemented fully need test cases.
    log.info("Killing Plex...")
    os.system("taskkill /f /im  \"Plex Media Server.exe\" >nul 2>&1")
    log.info("Starting Plex...")
    os.chdir(plex_path)
    subprocess.Popen(["Plex Media Server.exe"])


def restart_linux(plex_path):  # Not implemented fully need test cases.
    log.info("Rebooting Plex...")
    subprocess.run(plex_path, "plexmediaserver", "restart", shell=True)


def test_health_plex_and_reboot(servername, os):
    try:
        log.info("Connecting to Plex...")
        plex = account.resource(servername).connect(timeout=10)
        plex.library.section('TV - Trending')
        log.info("Plex is up!")
    except Exception:
        log.error("Plex is down!")
        if os == DOCKER:
            restart_docker()
        if os == WINDOWS:
            restart_windows(config["plex_path"])
        if os == LINUX:
            restart_linux(config["plex_path"])


config = set_config()
account = MyPlexAccount(config["username"], config["password"])
test_health_plex_and_reboot(config["servername"], config["os"])
