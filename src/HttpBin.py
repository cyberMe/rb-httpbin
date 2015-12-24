from robot.api.deco import keyword
from httplib import HTTPConnection


class HttpBin(object):
    """
    Robot framework test library for httpbin.org
    """
    def __init__(self):
        from collections import namedtuple
        self.result = namedtuple("Result", ['code', 'answer'])

    @keyword('Test Auth')
    def auth(self, user, password):
        """
        check httpbin.org basic auth
        :param user: username
        :param password: password
        :return:None
        """
        con = HTTPConnection("httpbin.org")
        path = "/basic-auth/{}/{}".format(str(user), str(password))
        from base64 import b64encode
        basic_auth = "Basic {}".format(b64encode(user + ":" + password))
        con.request("GET", path, None, {"Authorization": basic_auth})
        response = con.getresponse()
        result = self.result(response.status, response.reason)
        con.close()
        return result

    @keyword('Test Get')
    def get(self, header):
        """
        check get method
        :param header:
        :return:
        """
        con = HTTPConnection("httpbin.org")
        con.request("GET", "/get")
        response = con.getresponse()
        answer = ''
        if response.length > 0:
            data = response.read()
            from json import loads
            parsed = loads(data.__str__())
            con.close()
            answer = parsed["headers"][str(header)]
        result = self.result(response.status, answer)
        con.close()
        return result

    @keyword('Test Stream')
    def stream(self, count):
        """
        Check stream method
        :param count: request of count lines
        :return: returned count lines
        """
        con = HTTPConnection("httpbin.org")
        con.request("GET", "/stream/" + str(count))
        response = con.getresponse()
        data = response.read()
        result = self.result(response.status, len(data.splitlines()))
        con.close()
        return result

if __name__ == "__main__":
    b = HttpBin()
    print(b.auth("user", "name"))
    print(b.get("Host"))
    print(b.stream(10))
