
import urllib
import webbrowser
import oauth2 as oauth


class TwitterOauth:

    REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
    ACCESS_TOKEN_URL  = "https://api.twitter.com/oauth/access_token"
    AUTHENTICATE_URL  = "https://api.twitter.com/oauth/authenticate"

    def __init__(self, key, secret):
        self.consumer = oauth.Consumer(key=key, secret=secret)

    def get_authenticate_url(self):
        """
        �F�؃y�[�W��URL��Ԃ�
        """
        self._set_request_token_content()
        request_token = self.request_token_content["oauth_token"][0]
        query = urllib.parse.urlencode({"oauth_token": request_token})
        authenticate_url = self.AUTHENTICATE_URL + "?" + query
        return authenticate_url

    def get_access_token_content(self, pin):
        """
        Access Token �Ȃǂ̏�񂪓�����dict��Ԃ�
        """
        oauth_token = self.request_token_content["oauth_token"][0]
        oauth_token_secret = self.request_token_content["oauth_token_secret"][0]
        token = oauth.Token(oauth_token, oauth_token_secret)
        client = oauth.Client(self.consumer, token)
        body = urllib.parse.urlencode({"oauth_verifier": pin})
        resp, content = client.request(self.ACCESS_TOKEN_URL, "POST", body=body)
        return urllib.parse.parse_qs(content.decode())

    def _set_request_token_content(self):
        client = oauth.Client(self.consumer)
        resp, content = client.request(self.REQUEST_TOKEN_URL, "GET")
        self.request_token_content = urllib.parse.parse_qs(content.decode())


if __name__ == '__main__':

    ###############################################################################
    CONSUMER_KEY = "Il2tp4J43hWLNBV4iXRAJD8YN"            # ������ API key ��ݒ肷��
    CONSUMER_SECRET = "iPh5QIjdXruzVH9kKDy7WMvaFtKWuapO19Qd8yLkQssLgzSwWu"  # ������ API secret key ��ݒ肷��
    ###############################################################################

    t = TwitterOauth(CONSUMER_KEY, CONSUMER_SECRET)
    authenticate_url = t.get_authenticate_url()  # �F�؃y�[�W��URL���擾����
    webbrowser.open(authenticate_url)            # �u���E�U�ŔF�؃y�[�W���J��

    print("PIN? >> ", end="")
    pin = int(input())

    access_token_content = t.get_access_token_content(pin)
    access_token = access_token_content["oauth_token"][0]
    access_token_secret = access_token_content["oauth_token_secret"][0]
    s = "ACCESS TOKEN        = {}\nACCESS TOKEN SECRET = {}"
    s = s.format(access_token, access_token_secret)
    print(s)
