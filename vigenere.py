from pycipher import Vigenere
from termcolor import colored

# DECIPHERING VARIABLES
toCipher = 'rickandmorty'
ciphered = 'CCCVUNOGOCNY'
key = 'lua'
possibleKeys = ['ceu','dar','lua','ler','mar']
ciphered2 = 'Th tscs hirv qe cyvtmie uno zocgawfy dnuos tsy nznizh oq jrzry nlyanorlaaby. Thtfcttpews, vllizos alois ffhcecoym awfoh nwz wozjecutthg aureced Z (tsy “FMC”) ayx P (ebe “alois”) tz xuafinutp nhp zuywttinlfies aguiwubwy tz nhp nhtld aures U (ebe “fmec”), qiebofn bpcnr ubwy tz jeczocg tscs qonnnizhawctj in ebetl ohh (wtnhzot nioayrlnizh). Tsy czhcpjt tm cwispfy cyllneo no ebe yittin zz tsledbowx ccspeigcupss, eiwean wp xelf wtnh zhlj nwz jacnipm P lhd Q, uno jllwe gyrj mtccce lednrtwttind in ebe huy ebe zjecuttind urp jeczocgeo (qhtwh tm dzhe qir ebe dukp if pzftwiphcj, oslviwctj uno mclfamcltny). Qir praxjlp, zoc xenlyanizh (rpmp. dcgyutfle) A (Z) sphdd u sthgwy mpmslae ei F (A), ufeyr hbinb tsy llntpl clh dpwrjjt (dcgy) nhp gedmary. Ofl fzlmlf mzxewcnr if alois ccspeigcupss stantzinunefy rynplawczpm, stgpwcftys lhd dcmfftlhezosws cwurtzipm tsy mzxew if “lnoxcc alois” sfagpmtpx bj Vllte lhd Dnrlosd [4]. Cn aureccffac, qe oyfthe mcdtlennizhaw uno ontxicycecoyul gurtunem oq iuc gooyl1, lhd dboh yxelexylj mixjlp aeyyrtw szfuecoym fzl pcixj mirhaeorp uno ynnlyanizh iy nhpme xidpfs. Hy awmo rcvp gocy eqzinceyn szfuecoym fzl sppecul djencftw snbexys. Hy czhcwodp nhln pcixj wrjjtzarljhj cs l lewuttpews stgpwy czhcpjt ei slnidzy hbey fozeeo zrzg tsy czlrpwt lhd qirxul dnayxpzcne'

# FUNCTION TO EXPAND KEY TO COVER WHOLE TOCIPHER STRING
def repeat_to_length(key, toCipher):
    return ((key * (int(len(toCipher)/len(key))+1))[:len(toCipher)])

# KEY TESTING
key = repeat_to_length(key, toCipher)
print('Chave implementada: ',key)

# x = Vigenere('rickandmorty').encipher(key)
# print(x)

# a = Vigenere(key).decipher(ciphered)
# print(a)

# for p in possibleKeys:
#     print(Vigenere(p).decipher(ciphered) , '\n')

i = 0
while i < len(possibleKeys):
    print(
        'Verificação nº: ', i , '\n' ,
        'Chave: ', possibleKeys[i] , '\n' ,
        Vigenere(possibleKeys[i]).decipher(ciphered2) , '\n')
    i += 1
