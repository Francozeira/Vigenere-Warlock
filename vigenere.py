import re
from colorama import init
init()

from colorama import Fore, Back, Style

# DECIPHERING FUNCTIONS
class Cipher(object):
        
    def decipher(self,string):
        return string
        
    def a2i(self,ch):
        ch = ch.upper()
        arr = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
           'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
           'V':21,'W':22,'X':23,'Y':24,'Z':25,}
        return arr[ch]

    def i2a(self,i):
        i = i%26
        arr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        return arr[i]
        
    def remove_punctuation(self,text,filter='[^A-Z]'):
        return re.sub(filter,'',text.upper())

class Vigenere(Cipher):
    def __init__(self,key='fortification'):
        self.key = [k.upper() for k in key]

    def decipher(self,string):             
        string = self.remove_punctuation(string)
        ret = ''
        for (i,c) in enumerate(string):
            i = i%len(self.key)
            ret += self.i2a(self.a2i(c) - self.a2i(self.key[i]))
        return ret  

# GENERAL VARIABLES
ciphered4 = 'Th tscs hirv qe cyvtmie uno zocgawfy dnuos tsy nznizh oq jrzry nlyanorlaaby. Thtfcttpews, vllizos alois ffhcecoym awfoh nwz wozjecutthg aureced Z (tsy “FMC”) ayx P (ebe “alois”) tz xuafinutp nhp zuywttinlfies aguiwubwy tz nhp nhtld aures U (ebe “fmec”), qiebofn bpcnr ubwy tz jeczocg tscs qonnnizhawctj in ebetl ohh (wtnhzot nioayrlnizh). Tsy czhcpjt tm cwispfy cyllneo no ebe yittin zz tsledbowx ccspeigcupss, eiwean wp xelf wtnh zhlj nwz jacnipm P lhd Q, uno jllwe gyrj mtccce lednrtwttind in ebe huy ebe zjecuttind urp jeczocgeo (qhtwh tm dzhe qir ebe dukp if pzftwiphcj, oslviwctj uno mclfamcltny). Qir praxjlp, zoc xenlyanizh (rpmp. dcgyutfle) A (Z) sphdd u sthgwy mpmslae ei F (A), ufeyr hbinb tsy llntpl clh dpwrjjt (dcgy) nhp gedmary. Ofl fzlmlf mzxewcnr if alois ccspeigcupss stantzinunefy rynplawczpm, stgpwcftys lhd dcmfftlhezosws cwurtzipm tsy mzxew if “lnoxcc alois” sfagpmtpx bj Vllte lhd Dnrlosd [4]. Cn aureccffac, qe oyfthe mcdtlennizhaw uno ontxicycecoyul gurtunem oq iuc gooyl1, lhd dboh yxelexylj mixjlp aeyyrtw szfuecoym fzl pcixj mirhaeorp uno ynnlyanizh iy nhpme xidpfs. Hy awmo rcvp gocy eqzinceyn szfuecoym fzl sppecul djencftw snbexys. Hy czhcwodp nhln pcixj wrjjtzarljhj cs l lewuttpews stgpwy czhcpjt ei slnidzy hbey fozeeo zrzg tsy czlrpwt lhd qirxul dnayxpzcne'
ciphered3 = 'Vly eyltihv mhhsloenksh esgoyhkguvmip luu klqah dvichfa. Gioqopmwcxcqr ih mhhsloenksh ylyvlyt mh vly hslo sz gbwjehimhi qyuwuiim, vvupwuexcqrm vs nji yzgbcrag sz eshhmxgrnkef krzqvgcxcqr bcw vgih wwcpk nji wqqjwxyt xyelhqpiic uph ansvcp hgxqqve kw qkhy crx esgrpyz. Xbg flgexvl ih mhhsloenksh esgoyhkguvmip ynkpcbmhi kfqfun giotovil crx pinyslmmhi xyelhqpiimyu em vlya elg xifes nix vs nji yoiliihei ih tutxcgw qjs qcrngh nq wngef vly krzqvgcxcqr. Nq ihuylg xbg wyeylkxs crx krngklkxs qj u hmfg, eh grwqhcpk jtswgwm kw lguokvyf. Ihevsrxcqr cu hipi qjih vly hmfg mm uihv. Xbkw jtswgwm ymfn gipzytx hc slkkcp jcni cpxi c wyevyv jcni njen eeh psn di lgex. Oiupabkpy, vly fiwtcjvmip tlqgyuw cu hipi va xbg vyemjkihv sz vly uihv jcni. Nji lggykzyf wyevyv jcnim ymfn fy elupkyf fueo nq slkkcpef hmfg. Fs yes qj ypgifmhi, xbg slkkcpef hmfg acnp hqx vg vych va yhcynjslkdyf tutxcgw, vwx ipps dc nji lggcrmypx qjs bcw nji xgglatnksh mis. Qry qj nji unkitmnjqm wwyf xi rilhslo huve mggotmna mm vly Psymiip efislkxbo. Rigoyqr\'m cpaqvcvlg eeh di urtfkix kr ypglatnksh crx fiwtcjvmip sz oimueagw nq fy uiwwvyf fs fmpkhcpk nji wjelcgngvm krnq rigoyqr vnswmw.'
ciphered2 = 'Mifxekcit PntcygeifyTD ts ry acroittyx wytcy saj mevy dvgeczpvo tf detfrvwy ctnb lnu cekcivge r oixttrw kvj ujtnx ehv tnkprrntzzn fq a stodptitc zxaxp, slnh rd a wtnxprgciee, wzeh r detfrv mlfnk fq drea, byony aj l BzzstcygeTD. Ehv vep nae me ldeu, qoi pxrxpcp, aj ln vycijpktoe/oetcygeify kvj. Typ BzzstcygeTD nodarzdej l fzwtvc flycktoe, hhznh zd crwclwakpd ldier ae tmrre gcotpsjtnx llxzrzehd, lnu ztypr zyffcmreify wytcy ts ipqltrvo tf qiidt iptitemp, aeo typn mprzqy kse mllzoikj ow, ehv vep. Ehv vep ts iptitempd ldier ieqoixaktoe qrfx ae zukauk aakeeiy ffcmvo vzl typ ieeeilcktoe zf kse stodptitc zxaxp wzeh kse wtlkpr wfnteify. Typrvqoip, typ fzwtvc flycktoe xuje bv oejtgepd jz tylt ze pizdlnej l cfyszdtvyt fftgft gltkpre (lnu ehld, kvj). Typ fzwtvc flycktoe xuje acdo sp dvdixyeu eo sp svnuip (i.v. tnwzrdltzzn rmole typ fzygvcpitnk naeyok me iptitempd wcod ehv qiceei quentzzn). Kse tznjtskpntj ow ehv zukauk aakeeiy aeo typ svnuittp zf kse wtlkpr wfnteify aip typ tnz tfaitd dzdcldsvo ie ehzd praei.'
ciphered1 = 'Vvv roggf ugdzehj vvv fwcgadcg icwjgr sa hyg wdrzvosevokkce qt kjs Stoqkzzcb ukuzvoc esivwwkqrvsj’ umjvsd (Dfrbwc’u DBK) oef hyg diqqvug fh wehciookknrvwfp cw khj eclthj. Vvv Dfrbwc’u DBK kru sjvosnwjjsu dm kjs Echzqbrn Weuhzvikg cw Kbwqfdchzqb Kgqypccqup  (“Kbjvwkwhf Potkcecz ug Hvebfncxko uc Wehciooçãf”, czjq yeqk sa wku ottceaa “ZVW”) rocei o tqbkglk qt gqzzvwtcz kwfdqwc czfpu nkhy c zfv cw efzvwtkgd. Vvv Hsugfrn Qfwbtkz fh hyg Prt Ojuctkokkce (“Eceuscjc Wgrvtoc fo Ftrvo rfu Ouxcxcrfu rf Dfruwc”) ooug sjrstkocnm ycfjj qikhzeg riozpgk vvv umjvsd. Vvrv kru rlg hf khj kbkgfvuh zp hyg rvhseus fp gfos tqfgqfrvwmg digffiokkjvu, zzms kjs vowjuwfp cw nonasiu WUu. Ocuc, zv vrf pvgb gnoepwei hf nolpqy khj qke fwxkhrn qvthzhwtchvu’ gpuhvo. Hyg qfptckqk ifvy we ooea otvwfpg, zpqcwrzpu tqbjvwkwhzqbrn oef cifwecfp nonuizvg, nkhyqik cbp xwjkpcg gfnikkce. Vvv roggf uggttwsgg kjs Stoqkz GMW jagkga’j kagnsdgbkchzqb gtctggj, cbu vvv oozp qfpqvrhj qt kjs kgqypccqup. Vvvp wk cbrnmjgg kjs cgurn ticavycim oef hyg qikhzeg ugzzxsigr lrce kh. Kjs gcdvt kru plkzu hffo o iggvcftj arfs nkhy kbkgfmksnu oef o jwfmgm zpelkfp cpfwh kjs dqrvng fh arpoxkbx fwxkhrn qvthzhwtchvu’ gpuhvog. Kjsigtfts, zv qfpqcwrvu hych sqhy vvv vstjbzeoc cbu vvv nsxcz ugprvs jjcn c gfewrn rzudlvs, njwtj vru hf ds rugvugvf tiqa kjs tqagtsygbjkce qt kjs kgqypccqup’u gfewrn ijg. Vvtsrhhvt, hyg zrey fh rzhtluwfp cw c uvpsicz lus kgqypccqup vc xwoicbkgs uchr kbkgftjoeisj qpmkcluzp fsccmj vvv liukqzcz jagkga zptftarvwqchzqb.'
possibleKeys = ['ceu','dar','lua','ler','mar']
extendedPossibleKeys = [ 'ceu','dar','lua','ler','mar','sob', 'fel', 'vil', 'paz', 'mal', 'ver', 'ser', 'ego', 'ter', 'bem', 'vir', 'dar', 'bom', 'mas', 'rol', 'elo', 'era', 'tal', 'vis', 'ora', 'dia', 'luz', 'tez', 'com', 'ato', 'dor', 'eis', 'dou', 'hum', 'mim', 'ler', 'fiz', 'dom', 'pro', 'voo', 'sem', 'num', 'mau', 'uma', 'rua', 'sol', 'lei', 'que', 'ajo', 'foi', 'rio', 'pau', 'nau', 'seu', 'ode', 'eco', 'voz', 'fim', 'fez', 'nem', 'ido', 'meu', 'sim', 'vez', 'aia', 'via', 'boi', 'rei', 'jus', 'pai', 'sub', 'asa', 'jaz', 'som', 'tem', 'uns', 'azo', 'ali', 'for', 'rir', 'ata', 'agi', 'por', 'lhe', 'boa', 'uso', 'toa', 'sal', 'amo', 'ufa', 'sua', 'van', 'pra', 'cor', 'cia', 'cal', 'ovo', 'nos', 'par', 'tom', 'kit', 'fio', 'ira', 'mar', 'mui', 'giz', 'loa', 'lar', 'neo', 'mor', 'uau', 'ais', 'rim', 'uno', 'ano', 'pus', 'noz', 'top', 'gay', 'pez', 'mel', 'ele', 'cem', 'pal', 'aio', 'pia', 'cio', 'hem', 'oba', 'foz', 'tio', 'ela', 'uni', 'ida', 'ave', 'gia', 'jia', 'imo', 'tua', 'duo', 'uva', 'dum', 'teu', 'sic', 'cru', 'aro', 'vau', 'gol', 'dez', 'evo', 'ama', 'tia', 'exu', 'das', 'leu', 'deu', 'pio', 'aos', 'box', 'rap', 'dio', 'zen', 'nas', 'val', 'tai', 'oco', 'gaz', 'bio', 'ala', 'dei', 'mil', 'per', 'bis', 'tri', 'rum', 'opa', 'lia', 'aba', 'nua', 'sul', 'bar', 'oca', 'eia', 'pua', 'ado', 'ria', 'sus', 'bel', 'moa', 'oro', 'pan', 'ema', 'ipu', 'sai', 'sor', 'til', 'pum', 'vei', 'iso', 'spa', 'gel', 'min', 'qui', 'nom', 'mol', 'zoo', 'noa', 'aff', 'ero', 'ate', 'pop', 'ror', 'uru', 'itu', 'ola', 'zum', 'aca', 'lio', 'uai', 'ova', 'are', 'coa', 'eta', 'gir', 'gim', 'iru', 'bau', 'fot', 'upa', 'ono', 'ura', 'oma', 'xis', 'osa', 'sio', 'lis', 'bei', 'ulo', 'nha', 'mua', 'raz', 'feo', 'chi', 'var', 'mia', 'ati', 'obi', 'del', 'odo', 'rer', 'net', 'bit', 'ram', 'mio', 'gnu', 'ume', 'idi', 'IDH', 'tau', 'rau', 'ara', 'uca', 'pru', 'ose', 'aga', 'ade', 'dal', 'avo', 'ava', 'ota', 'ilu', 'afe', 'rep', 'omo', 'elu', 'qid', 'eva', 'ogo', 'reo', 'yin', 'cau', 'sen', 'Eva', 'abu', 'ago', 'emu', 'gio', 'psi', 'anu', 'apa', 'ril', 'fum', 'apo', 'ufo', 'gil', 'pul', 'far', 'heu', 'mir', 'out', 'ten', 'meo', 'axe', 'bos', 'uro', 'axi', 'aru', 'uga', 'ula', 'Gal', 'zio', 'adu', 'gau', 'sax', 'opo', 'hic', 'iva', 'Rem', 'ani', 'DDA', 'nit', 'dag', 'efi', 'ujo', 'rus', 'maz', 'uri', 'ren', 'nai', 'edu', 'iri', 'efe', 'oja', 'aal', 'tuo', 'ruz', 'nim', 'log', 'jau', 'bid', 'ppd', 'ozo', 'poa', 'ipo', 'joa', 'iba', 'upo', 'ovi', 'efo', 'udo', 'iei', 'uxi', 'ubi', 'oci', 'uja', 'rem', 'lev', 'bug', 'ici', 'ulu', 'uje', 'saa', 'udu']
commonWords = ['DECRYPTION','SECURITY','SAFETY','TECHNOLOGY','SYSTEM','PAPER','INFORMAT','PROCESS', 'THIS']

teste1 = 'Xn ztcmct gtazh, tpt cppoa qaatd kgyxioogaxwik plodrqihuh hike ajgotsbtd admm cee pnl tfnxcqtnb lagh tw sedtlwe smruzt iupgm tnkgyxiiwc tmrhvxqcts. Qc tpxs kdmujnqrabxov, le xgoxdsm p nml axerwpcp uoz xmive mccznpbxov qaatd wc cppobxc tdgqhtqr mies qc ozsez io uteb ihm geyjiztmmcta df bwe atccge qbaot tzpnauez. Xn bwe xgoxdsms iupgm tnkgyxiiwc skweut, av txbtrvpl atcztt sty wu 80-bqi avs ted cppobxc tdgqhtqr mies ige mbptdyms. Tpt ivxtqpl kdnlxtqdna uoz ihm qobw lwviaiik baxh azt dmgidtd chivv tpt efiezcat hekgeb zeg qy xgodxdqcg lxfntrmct etiowtive bd ata ibh bqis. Njrbwez, xn bwe xgoxdsms evrrgetqdn xgoktsa, tiowt lxfntrmct bnpmh on dpmgabxovh azt uatd bd evrrget bwe xxxmas wu av xmive icd ewikw ovt on ihmb wqal jt uatd ndr i eaziikjlig pqmet xs ltcqsel qy bwe wjtkdmm df bwe tdgqhtqr mie. Tw bast tpt cqehmg mwge zdbcht ivaqcsb png ptbpcs, ihm hekgeb zeg xs uddquims aniez tnkgyxiivv eirh jaokz on hifiemc pqmeth on ihm xmive. Bwe ztscata df atvmgat txxtrqbeviat, htiiiaiikpl icatnsqh avs kmn smcsqiidxtg ieais awoe ihii tpt pzdpwhel xmive mccznpbxov hcptmm erwkilts ic enuikxevi avs smruzt win fwg rmpl-bxmm xmive mccznpbxov pnl iricsuxsaxov.'
teste2 = '“Nokuscduyrire” rclepy tm oljteqy, alj hmsoqkxsglgzy fgd june hect evilsjeb lrms tfk lgyt ml dgyeyyeq. “Nokuscduyrire” iq ufrkn syeb hy pklgmimas ru ipxirgtc mawy, a lkgyzitklw vrmboione gtrotsje rnar ksagpcy Gmj\'s nxikurboaj rau - rotk. Ipunw os jonikd ru syxcyym ytd kucikrw, chgih mvpmye rne yhijotw zo juvc unc\'y ncogfhop. Napjlw, xapklw, gnb chw tor yaw, ot gy ikvoqyizre, ru tfos bgy, ru hcgr / pkab g nccsjktrkr unepk tfk hcgdjonc xeyjs: “Y nerkrmyevaaj iosvlc nab hect bcgtct, kgrlcj, bcgtct op ycmlfcj fmx sfuwgtg ylfcitgun gt pshlgi” alj / op "G srxagmhr sal roqz hgy lgle zkcyasc ne ugs qnouone ufd niq nerkrmyevaaj ihyxaazeposrocq."'
teste3 = ''

# FIRST TASK, TRANSLATE AND STORE DECYPHERS
i = 0
deciphered = []
while i < len(extendedPossibleKeys):
    deciphered.append(Vigenere(extendedPossibleKeys[i]).decipher(teste2))
    i += 1

# SECOND TASK, PRINTING ALL DECIPHERS
# j = 0
# while j < len(deciphered):
#     print(
#         'Verificação nº: ', j , '\n' ,
#         'Chave: ', extendedPossibleKeys[j] , '\n' ,
#         deciphered[j] , '\n'
#         '______________________________________________________________________________________________________________________________________________________________________________________','\n')
#     j += 1

# THIRD TASK, SEARCHING AND PRINTING DECIPHERS WITH COMMON ENGLISH WORDS
j = 0
while j < len(deciphered):
    k = 0
    hasWord = -1
    while (k < len(commonWords) and hasWord == -1):
        hasWord = deciphered[j].find(commonWords[k])
        if hasWord != -1:
            print( Fore.GREEN + 
                'Verificação nº: ', j , '\n' ,
                'Chave: ', extendedPossibleKeys[j] , '\n' ,
                deciphered[j] , '\n' + Style.RESET_ALL +
                '______________________________________________________________________________________________________________________________________________________________________________________','\n')
        k += 1
    j += 1

# FOURTH TASK, ADDING SPACE ON CORRECT DECHIPERED
j = 0
dictio = {}
thisIsCorrect = 'init'
while j < len(deciphered):
    k = 0
    hasWord = -1
    while (k < len(commonWords) and hasWord == -1):
        hasWord = deciphered[j].find(commonWords[k])
        if hasWord != -1:
            thisIsCorrect = deciphered[j]
        k += 1
    j += 1

# def find_all(a_str, sub):
#     start = 0
#     while True:
#         start = a_str.find(sub, start)
#         if start == -1: return
#         yield start
#         start += len(sub) # use start += 1 to find overlapping matches

# spacesArray = list(find_all(ciphered4, ' '))
# print (spacesArray)

dicio = list(thisIsCorrect)

dicio = { i : dicio[i] for i in range(0, len(dicio) ) }
# print (dicio)

i = 0
for c in ciphered4:
    if c == " ":
        dicio.update({i : " "})
    i += 1
print(dicio)

# CREATING FILE
# file = open("choupana.txt","w")
# 
