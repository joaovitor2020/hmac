import hashlib
MD5l = hashlib.md5().block_size

def preencheString(s):
        t = 0
        m = MD5l - len(s)
        while(t < m):
                t+= 1
                s+= chr(0)
        return s
	     
def criaIpad():	     
        ipad = ''
        w=0
        while(w < MD5l):
                w+= 1		
                ipad += chr(0x36)
        return ipad

def keyXorIpad(key,ipad):
        j=0
        x = 0
        result1 = []
        while(j < len(ipad)):
                x = ord(key[j])^ord(ipad[j])    #transforma cada caractere da string em inteire e faz um xor
                result1.append(x)
                j+=1
        return result1                          #vetor com o resultado do key xor ipad


def transformaIntChar(v):
        l=0
        result = ""
        while(l < len(v)):
                caractere = chr(v[l])
                result += caractere
                l+=1
        return result

def criaOpad():
        o=0
        opad=""
        while(o < MD5l):
                o+= 1		
                opad += chr(0x5C)
        #print(opad)
        #print(len(opad))
        return opad

def hmacMd5(key,text):
        if(len(key) < MD5l):
           key =  preencheString(key)
        ipad = criaIpad()
        result1 = transformaIntChar(keyXorIpad(key,ipad))
        result2 = result1 + text
        #print(result2)
        chave1 = hashlib.md5(result2.encode("utf-8"))
        opad = criaOpad()
        result3 = transformaIntChar(keyXorIpad(key,opad))
        chave2 = hashlib.md5(result3.encode("utf-8") + chave1.digest())
        return chave2

def verificaHmac(key,text,hash_esperada):
        g = hmacMd5(key,text).hexdigest()
        if(g == hash_esperada):
                return 1
        elif(g != hash_esperada):
                return 0
        

b = hmacMd5("key1","test1").hexdigest()
print(b)
print(verificaHmac("key1","test1",b))
#print(comparaHmac(a,b))
#print(hmacMd5(str1,str2).hexdigest())

