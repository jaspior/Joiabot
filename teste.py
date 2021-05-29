import os
import json
import requests
import tweepy
from datetime import datetime, timezone, timedelta

#get the time with timezone
fuso_horario = timezone(timedelta(hours=-3))
data_e_hora_atuais = datetime.now()
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data = data_e_hora_sao_paulo.strftime('%H:%M')

mystring = f""" joinha {data}"""



def main(message: str, filename: str='temp') -> None:
    auth = tweepy.OAuthHandler(
        os.environ.get("CONSUMER_KEY"), 
        os.environ.get("CONSUMER_SECRET")
    )

    auth.set_access_token(
        os.environ.get("ACCESS_TOKEN"), 
        os.environ.get("ACCESS_TOKEN_SECRET")
    )

    api = tweepy.API(auth)
    try:

        api.verify_credentials()
        print("Twitter Authentication Succeeded")

 
        try:
            api.update_status(message)
            print('Tweet successfully sent!')


        except Exception as e:
            print('Error sending tweet \n %s' % e)

    except:
        print("Twitter Authentication Failed")



if __name__ == '__main__':

    main(mystring)
