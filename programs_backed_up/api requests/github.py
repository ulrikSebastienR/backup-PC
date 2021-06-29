import pprint, json, requests
client_id = 'Iv1.0748a6c6d0bf55d5' # can be needed later
client_secret = '43313731db17088b961ed1bbc0eb47ae27e36379' #can be needed later

redirect_url = 'https://httpbin.org/anything'

def create_oauth_link():
    params = {
        'client_id' : client_id,
        'redirect_url' : redirect_url,
        'scope': 'user',
        'response_type': 'code'        
            }

    endpoint = 'https://github.com/login/oauth/authorize' 
    response = requests.get(endpoint, params=params)
    url = response.url
    return url

def exchange_code_for_access_token(code=None):
    params = {
        'client_id' : client_id,
        'redirect_url' : redirect_url,
        'client_secret' : client_secret,
        'code': code        
            }
    headers = {'Accept': 'application/json'}
    endpoint = 'https://github.com/login/oauth/access_token'
    response = requests.post(endpoint, params=params, headers=headers).json()
    return response['access_token']

def print_user_info(access_token=None):
    endpoint= 'https://api.github.com/user'
    headers= {'Authorization': f'token {access_token}'} # didn't understand it
    response = requests.get(endpoint, headers= headers).json()
    name = response['name']
    username = response['login']
    followers = response['followers']
    return print(f'user {name} or {username} has {followers} followers')

link = create_oauth_link()
print(f'the link of follow is {link}')
code = input('github code:')
access_token = exchange_code_for_access_token(code)
print(f'exchanged code {code} has access_token as: {access_token}')
print_user_info(access_token=access_token)

    



