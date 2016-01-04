#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = "xxxxxxxxxxxx"
csecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
atoken = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
asecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

malaga = [-4.559037,36.678891,-4.339496,36.757553] #Se obtiene de http://boundingbox.klokantech.com/

file =  open('tweets.txt', 'a') #la opcion a es para concatenar el nuevo contenido escrito con el anterior

class listener(StreamListener):

    def on_data(self, data):
        try:
            decoded = json.loads(data) #Twitter devuelve los datos en formato JSON
        except Exception as e:
            print (e) #Pintamos por pantalla el error
            return True #En caso de error, devolvemos True para que siga corriendo

        if decoded.get('geo') is not None: #Si existe geolocalizacion en el json obtenido anteriormente
            location = decoded.get('geo').get('coordinates') #coordenadas
            text = decoded['text'].replace('\n',' ').encode('utf-8') #tweet
            user = '@' + decoded.get('user').get('screen_name').encode('utf-8') #usuario
            created = decoded.get('created_at').encode('utf-8') #fecha
            tweet = '%s|%s|%s|%s\n' % (user,location,created,text) #componer los datos obtenidos

            file.write(tweet) #escribimos en el archivo

        return True

    def on_error(self, status):
        print(status) #Pintamos por pantalla el error

if __name__ == '__main__':
    print ('Comienza la captura')
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(locations=malaga)

