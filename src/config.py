from dataclasses import dataclass

@dataclass
class Config:
    BOT_TOKEN : str = "5762079476:AAGG_TK7mhRMR7yKiGkSv9KRXxvC6-qU1pc"
    admin_ids: int = 1
    url_api : str = "https://shikimori.me/api/graphql/"