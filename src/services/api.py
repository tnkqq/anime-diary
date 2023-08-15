from config import Config 
from fake_useragent import UserAgent
import httpx


class AnimeApi():
    def __init__(self,title):
        self.title = title 
        self.url = Config.url_api
        self.headers = {"User-Agent" : UserAgent().chrome}
    #ANime Title !!!
    async def fetch_anime_data(self):
        query = query ="""{
        animes(search: "{self.title}", limit: 1, kind: "!special") {
            id
            name
            score
            russian
            japanese
            status
            episodes
            releasedOn { year month day date }
            poster{ id originalUrl mainUrl }
            genres { id name russian kind }
            studios { id name imageUrl }
        }
        }"""
        async  with  httpx.AsyncClient() as client:
            params = {"Title" : self.title}
            responese = await client.post(self.url,json ={"query" : query},headers=self.headers)
        print(responese.status_code)
        print(responese.json())

