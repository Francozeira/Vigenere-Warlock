#UNCOMMENT LINES BELOW TO IMPORT LIBRARIES

# from pycipher import Vigenere
# from termcolor import colored

# GENRAL VARIABLES
toCipher = 'rickandmorty'
ciphered = 'CCCVUNOGOCNY'
key = 'lua'
possibleKeys = ['ceu','dar','lua','ler','mar']
ciphered4 = 'Th tscs hirv qe cyvtmie uno zocgawfy dnuos tsy nznizh oq jrzry nlyanorlaaby. Thtfcttpews, vllizos alois ffhcecoym awfoh nwz wozjecutthg aureced Z (tsy “FMC”) ayx P (ebe “alois”) tz xuafinutp nhp zuywttinlfies aguiwubwy tz nhp nhtld aures U (ebe “fmec”), qiebofn bpcnr ubwy tz jeczocg tscs qonnnizhawctj in ebetl ohh (wtnhzot nioayrlnizh). Tsy czhcpjt tm cwispfy cyllneo no ebe yittin zz tsledbowx ccspeigcupss, eiwean wp xelf wtnh zhlj nwz jacnipm P lhd Q, uno jllwe gyrj mtccce lednrtwttind in ebe huy ebe zjecuttind urp jeczocgeo (qhtwh tm dzhe qir ebe dukp if pzftwiphcj, oslviwctj uno mclfamcltny). Qir praxjlp, zoc xenlyanizh (rpmp. dcgyutfle) A (Z) sphdd u sthgwy mpmslae ei F (A), ufeyr hbinb tsy llntpl clh dpwrjjt (dcgy) nhp gedmary. Ofl fzlmlf mzxewcnr if alois ccspeigcupss stantzinunefy rynplawczpm, stgpwcftys lhd dcmfftlhezosws cwurtzipm tsy mzxew if “lnoxcc alois” sfagpmtpx bj Vllte lhd Dnrlosd [4]. Cn aureccffac, qe oyfthe mcdtlennizhaw uno ontxicycecoyul gurtunem oq iuc gooyl1, lhd dboh yxelexylj mixjlp aeyyrtw szfuecoym fzl pcixj mirhaeorp uno ynnlyanizh iy nhpme xidpfs. Hy awmo rcvp gocy eqzinceyn szfuecoym fzl sppecul djencftw snbexys. Hy czhcwodp nhln pcixj wrjjtzarljhj cs l lewuttpews stgpwy czhcpjt ei slnidzy hbey fozeeo zrzg tsy czlrpwt lhd qirxul dnayxpzcne'
ciphered3 = 'Vly eyltihv mhhsloenksh esgoyhkguvmip luu klqah dvichfa. Gioqopmwcxcqr ih mhhsloenksh ylyvlyt mh vly hslo sz gbwjehimhi qyuwuiim, vvupwuexcqrm vs nji yzgbcrag sz eshhmxgrnkef krzqvgcxcqr bcw vgih wwcpk nji wqqjwxyt xyelhqpiic uph ansvcp hgxqqve kw qkhy crx esgrpyz. Xbg flgexvl ih mhhsloenksh esgoyhkguvmip ynkpcbmhi kfqfun giotovil crx pinyslmmhi xyelhqpiimyu em vlya elg xifes nix vs nji yoiliihei ih tutxcgw qjs qcrngh nq wngef vly krzqvgcxcqr. Nq ihuylg xbg wyeylkxs crx krngklkxs qj u hmfg, eh grwqhcpk jtswgwm kw lguokvyf. Ihevsrxcqr cu hipi qjih vly hmfg mm uihv. Xbkw jtswgwm ymfn gipzytx hc slkkcp jcni cpxi c wyevyv jcni njen eeh psn di lgex. Oiupabkpy, vly fiwtcjvmip tlqgyuw cu hipi va xbg vyemjkihv sz vly uihv jcni. Nji lggykzyf wyevyv jcnim ymfn fy elupkyf fueo nq slkkcpef hmfg. Fs yes qj ypgifmhi, xbg slkkcpef hmfg acnp hqx vg vych va yhcynjslkdyf tutxcgw, vwx ipps dc nji lggcrmypx qjs bcw nji xgglatnksh mis. Qry qj nji unkitmnjqm wwyf xi rilhslo huve mggotmna mm vly Psymiip efislkxbo. Rigoyqr\'m cpaqvcvlg eeh di urtfkix kr ypglatnksh crx fiwtcjvmip sz oimueagw nq fy uiwwvyf fs fmpkhcpk nji wjelcgngvm krnq rigoyqr vnswmw.'
ciphered2 = 'Mifxekcit PntcygeifyTD ts ry acroittyx wytcy saj mevy dvgeczpvo tf detfrvwy ctnb lnu cekcivge r oixttrw kvj ujtnx ehv tnkprrntzzn fq a stodptitc zxaxp, slnh rd a wtnxprgciee, wzeh r detfrv mlfnk fq drea, byony aj l BzzstcygeTD. Ehv vep nae me ldeu, qoi pxrxpcp, aj ln vycijpktoe/oetcygeify kvj. Typ BzzstcygeTD nodarzdej l fzwtvc flycktoe, hhznh zd crwclwakpd ldier ae tmrre gcotpsjtnx llxzrzehd, lnu ztypr zyffcmreify wytcy ts ipqltrvo tf qiidt iptitemp, aeo typn mprzqy kse mllzoikj ow, ehv vep. Ehv vep ts iptitempd ldier ieqoixaktoe qrfx ae zukauk aakeeiy ffcmvo vzl typ ieeeilcktoe zf kse stodptitc zxaxp wzeh kse wtlkpr wfnteify. Typrvqoip, typ fzwtvc flycktoe xuje bv oejtgepd jz tylt ze pizdlnej l cfyszdtvyt fftgft gltkpre (lnu ehld, kvj). Typ fzwtvc flycktoe xuje acdo sp dvdixyeu eo sp svnuip (i.v. tnwzrdltzzn rmole typ fzygvcpitnk naeyok me iptitempd wcod ehv qiceei quentzzn). Kse tznjtskpntj ow ehv zukauk aakeeiy aeo typ svnuittp zf kse wtlkpr wfnteify aip typ tnz tfaitd dzdcldsvo ie ehzd praei.'
ciphered1 = 'Vvv roggf ugdzehj vvv fwcgadcg icwjgr sa hyg wdrzvosevokkce qt kjs Stoqkzzcb ukuzvoc esivwwkqrvsj’ umjvsd (Dfrbwc’u DBK) oef hyg diqqvug fh wehciookknrvwfp cw khj eclthj. Vvv Dfrbwc’u DBK kru sjvosnwjjsu dm kjs Echzqbrn Weuhzvikg cw Kbwqfdchzqb Kgqypccqup  (“Kbjvwkwhf Potkcecz ug Hvebfncxko uc Wehciooçãf”, czjq yeqk sa wku ottceaa “ZVW”) rocei o tqbkglk qt gqzzvwtcz kwfdqwc czfpu nkhy c zfv cw efzvwtkgd. Vvv Hsugfrn Qfwbtkz fh hyg Prt Ojuctkokkce (“Eceuscjc Wgrvtoc fo Ftrvo rfu Ouxcxcrfu rf Dfruwc”) ooug sjrstkocnm ycfjj qikhzeg riozpgk vvv umjvsd. Vvrv kru rlg hf khj kbkgfvuh zp hyg rvhseus fp gfos tqfgqfrvwmg digffiokkjvu, zzms kjs vowjuwfp cw nonasiu WUu. Ocuc, zv vrf pvgb gnoepwei hf nolpqy khj qke fwxkhrn qvthzhwtchvu’ gpuhvo. Hyg qfptckqk ifvy we ooea otvwfpg, zpqcwrzpu tqbjvwkwhzqbrn oef cifwecfp nonuizvg, nkhyqik cbp xwjkpcg gfnikkce. Vvv roggf uggttwsgg kjs Stoqkz GMW jagkga’j kagnsdgbkchzqb gtctggj, cbu vvv oozp qfpqvrhj qt kjs kgqypccqup. Vvvp wk cbrnmjgg kjs cgurn ticavycim oef hyg qikhzeg ugzzxsigr lrce kh. Kjs gcdvt kru plkzu hffo o iggvcftj arfs nkhy kbkgfmksnu oef o jwfmgm zpelkfp cpfwh kjs dqrvng fh arpoxkbx fwxkhrn qvthzhwtchvu’ gpuhvog. Kjsigtfts, zv qfpqcwrvu hych sqhy vvv vstjbzeoc cbu vvv nsxcz ugprvs jjcn c gfewrn rzudlvs, njwtj vru hf ds rugvugvf tiqa kjs tqagtsygbjkce qt kjs kgqypccqup’u gfewrn ijg. Vvtsrhhvt, hyg zrey fh rzhtluwfp cw c uvpsicz lus kgqypccqup vc xwoicbkgs uchr kbkgftjoeisj qpmkcluzp fsccmj vvv liukqzcz jagkga zptftarvwqchzqb.'


# FUNCTION TO EXPAND KEY TO COVER WHOLE TOCIPHER STRING
def repeat_to_length(key, toCipher):
    return ((key * (int(len(toCipher)/len(key))+1))[:len(toCipher)])

# KEY TESTING
key = repeat_to_length(key, toCipher)
# print('Chave implementada: ',key)

# x = Vigenere('rickandmorty').encipher(key)
# print(x)

# a = Vigenere(key).decipher(ciphered)
# print(a)

# for p in possibleKeys:
#     print(Vigenere(p).decipher(ciphered) , '\n')


i = 0

# FIRST TASK, JUST PRINTING RESULTS
# while i < len(possibleKeys):
#     print(
#         'Verificação nº: ', i , '\n' ,
#         'Chave: ', possibleKeys[i] , '\n' ,
#         Vigenere(possibleKeys[i]).decipher(ciphered4) , '\n'
#         '______________________________________________________________________________________________________________________________________________________________________________________','\n')
#     i += 1

# SECOND TASK, STORING DECIPHERS
deciphered = []
while i < len(possibleKeys):
    deciphered.append(Vigenere(possibleKeys[i]).decipher(ciphered4))
    i += 1

# SECOND TASK, PRINTING DECIPHERS
# j = 0
# while j < len(deciphered):
#     print(
#         'Verificação nº: ', j , '\n' ,
#         'Chave: ', possibleKeys[j] , '\n' ,
#         deciphered[j] , '\n'
#         '______________________________________________________________________________________________________________________________________________________________________________________','\n')
#     j += 1

# THIRD TASK, SEARCHING FOR COMMON ENGLISH WORDS
# k = 0
# while k < len(deciphered):
#     hasWord = deciphered[k].find('DECRYPTION')
#     if hasWord != -1:
#         print(
#             'Verificação nº: ', k , '\n' ,
#             'Chave: ', possibleKeys[k] , '\n' ,
#             deciphered[k] , '\n'
#             '______________________________________________________________________________________________________________________________________________________________________________________','\n')
#     hasWord = None
#     k += 1

# FOURTH TASK, SCALING LEVELS OF IMPORTANCE
j = 0
higherLevelDecyphered = []
higherLevelWords = ['DECRYPTION','THIS']

while j < len(deciphered):
    k = 0
    while k < len(higherLevelWords):
        hasWord = deciphered[j].find(higherLevelWords[k])
        if hasWord != -1:
            higherLevelDecyphered.append(deciphered[j])
        hasWord = None
    j += 1

for h in higherLevelDecyphered:
    print(
        'Verificação nº: ', j , '\n' ,
        'Chave: ', possibleKeys[j] , '\n' ,
        deciphered[j] , '\n'
        '______________________________________________________________________________________________________________________________________________________________________________________','\n')


# x = deciphered[2].find('DECRYPTION')
# y = deciphered[1].find('DECRYPTION')
# print(x,y)