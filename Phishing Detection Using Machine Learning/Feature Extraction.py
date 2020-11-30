import numpy as np
def URLhavingattherate(URL): #4th column
    if '@' in URL:
        return 0
    else:
        return 1
def Redirectusingdoubleslash(URL):#5th column
    p=0
    for i in range(len(URL)-1):
        if URL[i]=="/" and URL[i+1]=="/":
            p=i
    if p>7:
        return 0
    else:
        return 1
def prefixsuffix(URL): #6th column
    if '-' in URL:
         return 0
    else:
        return 1
def Length(URL): #2nd column
    if len(URL)<54:
         return 1
    else:
        return 0.
def TinyURL(URL): #3rd column
    if 'bit.ly' in url:
         return 1
    else:
        return 0
def IP(URL):#1st Column
    if URL.count('x')>6:
        return 0
    else:
        return 1
def Dot(URL):#7th column
    if URL.count('.')>3:
        return 0
    else:
        return 1
def HTTPS(URL):#8th column
    if 'https' in URL:
        return 1
    else:
        return 0
def valid(e):
    if e<=1:
        return 1
    else:
        return 0
def favicon(f):
    if f==1:
        return 1
    else:
        return 0

def nonstandardport(port): #11
   if port == True:return 0 
   else: return 1

def requestUrl(URL): #13 column
    if URL>=22 and URL<=61:
        return 1
    else:
        return 0
def anchor(URL): #14column
    if URL>=31 and URL<=67:
        return 1
    else:
        return 0
def SFH(sfh): #16column
    if sfh='':
        return 1
    else:
        return 0
def email(mail): #17column
    mail=0
    if mail==1:
        return 1
    else:
        return 0
def abnormal(URL): #18column
    hostname=''
    if URL==hostname:
        return 1
    else:
        return 0
def redirect(URL): #19column
    redirect=1
    if redirect>=2 and redirect<4:
        return 1
    else:
        return 0
def onmouseover(URL): #20colum
    if len(URL) >20:
        return 0
    else:
        return 1



    
def rightclick(URL): #21column
    if len(URL)>12:
        return 1
    else:
        return 0
def popup(txt): #22column
    if txt="":
        return 0
    else:
        return 1


def iframe(frame): #23
    frame=0
    if frame==1:
        return 1
    else:
        return 0
def ageofdomain(month): #24
     month = int(input('Enter the number to be converted: '))
    if month<6:
        return 1
    else:
        return 0
def dnsrecord(dns): #25
    if dns='':
        return 1
    else:
        return 0
def websitetraffic(rank): #26
    if rank>=100000:
        return 1
    else:
        return 0
def pagerank(prank): #27
    if prank<0.2:
        return 1
    else :
        return 0
def googleindex(index): #28
    if index == True:
        return 1
    else:
        return 0

def numboflinks(link): #29
    if link>=0 and link<=2:
        return 1
    else:
        return 0
def statisticalreports(host): #30
url = input()
exp = int(input())
L=[]
for i in range(30):
    L+=[0]
c9 = valid(exp)
L[8] = c9
c8 = Dot(url)
L[7] = c8
c7 = Dot(url)
L[6] = c7
c1 = IP(url)
L[0] = c1
c3 = TinyURL(url)
L[2]=c3
c2 = Length(url)
L[1] = c2
p = URLhavingattherate(url)
L[3]=p
k = Redirectusingdoubleslash(url)
L[4]=k
s = prefixsuffix(url)
L[5]=s
f = int(input())
c10 = favicon(f)
L[9] = c10
port = int(input('port'))
c11 = nonstandardport(port)
L[10]=c11
c12=requestUrl(url)
L[11]= c12
c13=anchor(url)
L[12]= c13
c14 = SFH(url)
L[13]= c14
mail = int(input('Mail'))
c15 = email(mail)
L[14] = c15
c16 = abnormal(url)
L[15] = c16
c17 = redirect(url)
L[16] = c17
c18 = onmouseover(url)
L[17] = c18
c19 = rightclick(url)
L[18] = c19
c20 = popup(url)
L[19] = c20
frame = int(input('frame'))
c21 = iframe(frame)
L[20] = c21
age = int(input('age'))
c22 = ageofdomain(age)
L[21] = c22
dns = int(input('dns'))
c23 = dnsrecord(dns)
L[22] = c23
rank = int(input('rank'))
c24 = websitetraffic(rank)
L[23] = c24
c25 = googleindex(rank)
L[24] = c25
links = int(input('Links'))
c26 = numboflinks(links)
L[25] = c26
for i in range(26,30):
    p = np.random.randn(1)
    if p>0.5:
        L[i] = 1
    else:
        L[i] = 0
print(*L)
