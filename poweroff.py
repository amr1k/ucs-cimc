import secrets
import requests
import sys

#   The follow power states are allowed
#       "On",
#       "ForceOff",
#       "GracefulShutdown",
#       "ForceRestart",
#       "Nmi"
#
def power(server, state, auth):
    url = "https://"+server+"/redfish/v1/Systems/FCH1706V07G/Actions/ComputerSystem.Reset"

    payload = "{\"ResetType\": \""+state+"\"}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic "+auth,
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    print response.status_code
    if response.status_code == 200:
        return "sucess"
    else:
        return "fail"

if len(sys.argv) == 1:
    print   "\n\n\nplease use the following as the furst argument: \n\n\
                - On\n\
                - ForceOff\n\
                - GracefulShutdown\n\
                - ForceRestart\n\
                - Nmi\n\n\n"
    exit()

print power(secrets.server, sys.argv[1], secrets.auth)