from torpy.http.requests import TorRequests
with TorRequests() as tor_requests:
    with tor_requests.get_session() as sess:
        print(sess.get("http://httpbin.org/ip").json())
    with tor_requests.get_session() as sess:
        print(sess.get("http://httpbin.org/ip").json())

