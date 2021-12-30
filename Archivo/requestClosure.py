import requests


def requestsGet(url: str) -> requests.models.Request:
    def makeRequestGet(**kwargs):
        return requests.get(url.format_map(kwargs))
    return makeRequestGet


if __name__ == '__main__':
    getData = requestsGet("https://postman-echo.com/get?{key}={val}")
    result=getData(key="hellow", val="world")
    print(result)
