from django.shortcuts import render
from  django.http import HttpResponse
import random
from . import models
# Create your views here.
PersionLetters = [
    'ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ز','ژ','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ی',' ',
]
#ქწერტყუიოპასდფგჯკლზხცვბნმჭღთჟჩშჵჶ
Numbers = {
    0:"ღ",
    1:"ნ",
    2:"ჯ",
    3:"ჩ",
    4:"ქ",
    5:"ყ",
    6:"ტ",
    7:"რ",
    8:"ე",
    9:"წ",
}
Numbers2 = {
    "ღ":0,
    "ნ" :1,
    "ჯ":2,
    "ჩ" :3,
    "ქ":4,
    "ყ":5,
    "ტ" :6,
    "რ":7,
    "ე":8,
    "წ":9,
}
#---------------------
StringOFLetters = "ქწერტყუიოპასდფგჯკლზხცვბნმჭღთჟჩშჵჶ "
ListOfLetters = []
for i in StringOFLetters:
    ListOfLetters.append(i)
#-------------------------
StringNoneLetters = "₾¢ჰতፅስሥዝግርቅውብኅን" 
ListNoneLetters = []
for i in StringNoneLetters:
        ListNoneLetters.append(i)
ChanceList = [1,1,1,1,0,0,0,0,0]
def First_Page(request):
    return(render(request, "Translator/Login.html"))


def Introduction(request):
    return render(request,"Translator/Introduction.html")

def Admin_Page_Show(request):
    return render(request, "Translator/Admin.html")

def Add_Language(request,Amount):
    for i in range(Amount):
        r = []
        y = 0
        for i in range(33) :
            a = random.choice(ListOfLetters)
            r.append(a)
            ListOfLetters.remove(a)
            y+=1

        x = models.LANGUAGE_CODE(None,r[0],r[1],r[2],r[3],r[4],r[5],r[6]
        ,r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16]
        ,r[17],r[18],r[19],r[20],r[21],r[22],r[23],r[24],r[25],r[26]
        ,r[27],r[28],r[29],r[30],r[31],r[32])

        x.save()
    return HttpResponse("Done Successfully!")

def Check_Login(request,Name,Password):
    Users = models.Users.objects.all()
    for user in Users:
        if user.Name==Name and user.Password==Password: 
            return render(request= request, template_name= "Translator/ChooseMode.html",context={"Name":Name} )
    else:
        return render(request= request, template_name= "Translator/LoginError.html",
                )
def GetP2C(request,Name):
    return render(request, "Translator/P2C.html",{"Name":Name})

def GetC2P(request,Name):
    return render(request, "Translator/C2P.html",{"Name":Name})
    
def GetResultC2P(request):
    try:
        r = request.POST['Response']
        First_r = ""
        for i in r:
            if not i in ListNoneLetters:
                First_r+=i
        #---------------------------
        NumberOFLanguage = First_r[0] + First_r[1] + First_r[2] + First_r[3] 
        NumberOFLanguage_Second=""
        for i in NumberOFLanguage:
            NumberOFLanguage_Second += str(Numbers2[i])
        NumberOFLanguage_Final = int(NumberOFLanguage_Second)
        #-----------------------------------
        index = -1
        Second_r = ""
        for i in First_r:
            index += 1
            if index<=3:
                continue
            else :
                Second_r += i
            #------------------------
        Language = models.LANGUAGE_CODE.objects.get(pk = NumberOFLanguage_Final)
            
        li = {
                Language.Letters_Alef : "ا",
                Language.Letters_Be : "ب",
                Language.Letters_Pe : "پ",
                Language.Letters_Te : "ت",
                Language.Letters_Se : "ث",
                Language.Letters_Jim : "ج",
                Language.Letters_Che : "چ",
                Language.Letters_Khe: "خ",
                Language.Letters_Dal : "د",
                Language.Letters_Zal : "ذ",
                Language.Letters_Re : "ر",
                Language.Letters_Ze : "ز",
                Language.Letters_Zhe : "ژ",
                Language.Letters_Sin : "س",
                Language.Letters_Shin : "ش",
                Language.Letters_Sad : "ص",
                Language.Letters_Zad : "ض",
                Language.Letters_Ta : "ط",
                Language.Letters_Za : "ظ",
                Language.Letters_Ain : "ع",
                Language.Letters_Ghain : "غ",
                Language.Letters_Fe: "ف",
                Language.Letters_Qaf : "ق",
                Language.Letters_Kaf : "ک",
                Language.Letters_Ghaf : "گ",
                Language.Letters_Lam : "ل",
                Language.Letters_MiM : "م",
                Language.Letters_Noon : "ن",
                Language.Letters_Vav : "و",
                Language.Letters_He : "ه",
                Language.Letters_Ye : "ی",
                Language.Letters_Hyphen : " ",

            }
        Final_r = ""
        for i in Second_r:
            if i in li:
                Final_r += li[i]
            else:
                Final_r += i
        context = {"output":Final_r}
        return render(request, "Translator/Result.html",context) 
    except:
        return render(request, "Translator/CodeError.html")       

def GetResultP2C(request):
    rr = request.POST['Response']
    Name = request.POST['Name']
    user = models.Users.objects.get(Name=Name)
    note = models.Notes(None,rr,user.pk)
    note.save()

    r = ""
    NumberOfCode = random.randrange(2000)
    NumberOfCode += 1
    language = models.LANGUAGE_CODE.objects.get(pk = NumberOfCode)
    for i in rr:
        if i == "آ":
            r+="ا"
        else:
            r+=i
    l = {
        "ا":language.Letters_Alef,
        "ب":language.Letters_Be,
        "پ":language.Letters_Pe,
        "ت":language.Letters_Te,
        "ث":language.Letters_Se,
        "ج":language.Letters_Jim,
        "چ":language.Letters_Che,
        "ح":language.Letters_HeJimi,
        "خ":language.Letters_Khe,
        "د":language.Letters_Dal,
        "ذ":language.Letters_Zal,
        "ر":language.Letters_Re,
        "ز":language.Letters_Ze,
        "ژ":language.Letters_Zhe,
        "س":language.Letters_Sin,
        "ش":language.Letters_Shin,
        "ص":language.Letters_Sad,
        "ض":language.Letters_Zad,
        "ط":language.Letters_Ta,
        "ظ":language.Letters_Za,
        "ع":language.Letters_Ain,
        "غ":language.Letters_Ghain,
        "ف":language.Letters_Fe,
        "ق":language.Letters_Qaf,
        "ک":language.Letters_Kaf,
        "گ":language.Letters_Ghaf,
        "ل":language.Letters_Lam,
        "م":language.Letters_MiM,
        "ن":language.Letters_Noon,
        "و":language.Letters_Vav,
        "ه":language.Letters_He,
        "ی":language.Letters_Ye,
        " ":language.Letters_Hyphen,


    }
    #---------------------------
    x = str(NumberOfCode)
    zero = ""
    for i in range( 4 - len(x) ):
        zero +="0"
    x = zero + x
    y=""
    for i in x:
        y+= Numbers[int(i)]
        if random.choice(ChanceList):
            y+=random.choice(ListNoneLetters)
    #----------------------------
    output = ""
    for i in r:
        if i in PersionLetters:
            output+=l[i]
            if random.choice(ChanceList):
                output+=random.choice(ListNoneLetters)
        else:
            output+=i
            if random.choice(ChanceList):
                output+=random.choice(ListNoneLetters)
    #----------------------------
    output = y + output
    y = 0
    index=-1
    foutput = ""
    for i in output:
        index+=1
        foutput += i
        y+=1
        if y>20:
            y=0
            foutput += "\n"
    context = {"output":output , "P2C":True}
    return render(request, "Translator/Result.html",context)
