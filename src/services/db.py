
class DataBase:


    def __init__(self,connect):
        self.connect = connect 

    async def ad_users(self,user_id):
        with self.connect:
            return self.cursor.execute("""INSERT INTO  users (user_id,name)""") 
    