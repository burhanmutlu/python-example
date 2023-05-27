from xml.etree.ElementTree import tostring


liste = []
k=0
with open ('data.txt', 'r+') as dosya: 
    for i in dosya:
        liste.append(i)
        listem = liste[k][0]+liste[k][1]+liste[k][2]+liste[k][3]
        print(listem)
        k = k+1
        fin = open("data.txt", "rt")
        data = fin.read()
        data = data.replace(listem, listem +"-")
        fin.close()
        fin = open("data.txt", "wt")
        fin.write(data)
        fin.close()

        fin = open("data.txt", "rt")
        data = fin.read()
        data = data.replace('-', '</td><td>')
        fin.close()
        fin = open("data.txt", "wt")
        fin.write(data)
        fin.close()

    dosya.close()    