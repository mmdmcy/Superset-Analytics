import json
import requests

def deploy_dashboards(dashboard_file):
    with open(dashboard_file, 'r') as file:
        dashboards = json.load(file)

    for dashboard in dashboards:
        response = requests.post(
            'http://localhost:8088/api/v1/dashboard/',
            json=dashboard,
            headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
        )
        if response.status_code == 201:
            print(f"Dashboard '{dashboard['dashboard_title']}' deployed successfully.")
        else:
            print(f"Failed to deploy dashboard '{dashboard['dashboard_title']}': {response.content}")

if __name__ == "__main__":
    deploy_dashboards('../dashboards/exports/dashboard_exports.json')