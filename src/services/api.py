from config import Config 
from fake_useragent import UserAgent
import httpx

class AnimeApi():
    def __init__(self,title):
        self.title = title 
        self.url = Config.url_api
        self.headers = {"User-Agent" : UserAgent().chrome}
    async def fetch_anime_data(self):
        query = f"""{{
        animes(search: "{self.title}", limit: 1, kind: "!special") {{
            id
            name
            score
            russian
            japanese
            status
            episodes
            releasedOn {{ year }}
            poster {{ originalUrl mainUrl }}
            genres {{ name russian kind }}
            studios {{  name  }}
        }}
        }}
        """

        async  with  httpx.AsyncClient() as client:

            params = {"Title" : self.title}
            responese = await client.post(self.url,json ={"query" : query},headers=self.headers)
        print(f"{self.title} : status code : {responese.status_code}")
        responese = responese.json()["data"]["animes"][0]
        
        anime_data = dict ()
        for key,value in responese.items():
            anime_data[key] = value

        return anime_data














