import socket
import ssl
import re

class tls:
    def check(self,host,port,connexion):
        try:
            context=ssl.create_default_context()
            socket.setdefaulttimeout(5)
            with socket.create_connection((host, port )) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    cipher = ssock.cipher()
                    Zertf= ssock.getpeercert()
                    print(ssock.version())
                   # print("11111111")
                    print(cipher[0])
                    print(host)
                    #print("22222222")
                    print(Zertf)
                    #print("3333333333")
                    print(Zertf['version'])
                    #print("4444444444444444444444444444444444444444444444444")
                    #print(Zertf['issuer'][1][0][0])
                    #print("555555555")
                    #print(Zertf['issuer'][1][0][1])
                    #print("666666666")

                    if(Zertf['issuer'][1][0][0]=='organizationName'):
                        print(Zertf['issuer'][1][0][1])
                        print("777777777777")
                        Zert_O=Zertf['issuer'][1][0][1]
                    else:
                        print(Zertf['issuer'][3][0][1])
                        print("8888888888888")
                        Zert_O=Zertf['issuer'][3][0][1]


                    query = connexion.cursor()
                    data = (host, ssock.version(), cipher[0],Zert_O )
                    query.execute("INSERT INTO hosts VALUES( ? , ?, ?, ? )", data)
                    connexion.commit()
        except:
            query = connexion.cursor()
            data = (host)
            query.execute("INSERT INTO hosts('host') VALUES( ? )", [data])
            connexion.commit()
    def clear(self,connexion):
        query = connexion.cursor()
        query.execute("DELETE FROM hosts")

    def getbytls(self,connexion):
        query = connexion.cursor()
        res = query.execute("select tls , count(host)  from hosts group by tls")
        data = res.fetchall()
        return data

    def getbyorganisation(self,connexion):
        query = connexion.cursor()
        res = query.execute("select organisation , count(host)  from hosts where organisation NOT NULL  group by organisation")
        data = res.fetchall()
        return data

    def getbycyfer(self,connexion):
        query = connexion.cursor()
        res = query.execute("select Chiffriersuiten , count(host)  from hosts where Chiffriersuiten NOT NULL group by Chiffriersuiten")
        data = res.fetchall()
        return data


