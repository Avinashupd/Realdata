import requests

auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" \
             ".eyJzdWIiOjEwNzU4LCJpc3MiOiJodHRwczpcL1wvY3VzdG9tZXIuc2VydmV0ZWwuaW5cL3R" \
             "va2VuXC9nZW5lcmF0ZSIsImlhdCI6MTYwODQ2MDA2MiwiZXhwIjoxOTA4NDYwMDYyLCJuYmY" \
             "iOjE2MDg0NjAwNjIsImp0aSI6InE3aGtrZnB0aUFCRjBGSVUifQ.4PkHWMcs-R4HDCFGnjBLuMbf27yaW0Q1bNtisodrO8U "


def post_agent():
    addAgent = requests.post('https://api.servetel.in/v1/agent',
                             headers={"Content-Type": "application/json", "Accept": "application/json",
                                      "Authorization": auth_token},
                             json={"name": "Avinash", "follow_me_number": 9962792273})
    addAgent_response = addAgent.json()
    assert addAgent.status_code == 200
    assert addAgent_response["message"] == "Agent added successfully"
    agent_id = addAgent_response["agent_id"]
    return agent_id


def get_agent(agent_id):
    getAgent = requests.get('https://api.servetel.in/v1/agents', headers={"Accept": "application/json",
                                                                          "Authorization": auth_token})
    getAgent_response = getAgent.json()
    print(getAgent_response)
    assert getAgent.status_code == 200
    assert getAgent_response[0]["eid"] == agent_id

def update_agent(agent_id):
    get_url = "https://api.servetel.in/v1/agent/" + agent_id
    updateAgent = requests.put(get_url, headers={"Accept": "application/json", "Content-Type": "application/json",
                                                 "Authorization": auth_token},
                               json={"name": "Avinash_upd", "follow_me_number": 9962792273})
    assert updateAgent.status_code == 200
    updateAgent_response = updateAgent.json()
    print(updateAgent_response)


def delete_agent(agent_id):
    get_url = "https://api.servetel.in/v1/agent/" + agent_id
    deleteAgent = requests.delete(get_url, headers={"Accept": "application/json", "Authorization": auth_token})
    assert deleteAgent.status_code == 200
