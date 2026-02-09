import api_client
import os
import dotenv
import json
import ast
from pathlib import Path

dotenv.load_dotenv()

apikey = os.getenv("APIKEYFORORION")

def getfleetsyay():

    response = api_client.get_v1_stations(apikey, include_config=False, include_deployments=True)



    p = Path("stations.json")
    data = response
    if not isinstance(data, (dict, list)):
        try:
            data = json.loads(response)
        except Exception:
            data = ast.literal_eval(response)

    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote pretty JSON to {p}")
    return "done"




def getstationid(deployment_name):
    """
    Search stations.json for a deployment with the given deployment_name.
    Returns the station_id of the station containing that deployment.
    """
    p = Path("stations.json")
    if not p.exists():
        return None
    
    try:
        data = json.loads(p.read_text())
    except Exception:
        return None
    
    items = data.get('items', [])
    for station in items:
        deployments = station.get('deployments', [])
        for deployment in deployments:
            if deployment.get('deployment_name') == deployment_name:
                return station.get('station_id')
    
    return None


def getdeploymentinfo(deployment_name):
    """
    Search stations.json for a deployment with the given deployment_name.
    Returns a dict with station_id, player_count, and other deployment info.
    """
    p = Path("stations.json")
    if not p.exists():
        return None
    
    try:
        data = json.loads(p.read_text())
    except Exception:
        return None
    
    items = data.get('items', [])
    for station in items:
        deployments = station.get('deployments', [])
        for deployment in deployments:
            if deployment.get('deployment_name') == deployment_name:
                return {
                    'station_id': station.get('station_id'),
                    'station_name': station.get('station_name'),
                    'deployment_id': deployment.get('deployment_id'),
                    'player_count': deployment.get('player_count'),
                    'deployment_cl': deployment.get('deployment_cl'),
                    'region': deployment.get('region'),
                    'online': deployment.get('online'),
                }
    
    return None





