import re
from colorama import init, Fore, Back, Style
init()

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
            i = i % len(self.key)
            ret += self.i2a(self.a2i(c) - self.a2i(self.key[i]))
        return ret  

def formatString(stringToFormat):    
    # IF CORRECT MATCH IS FOUND, LOWER ALL CASES AND ADDING SPACE AND SPECIAL CHARACTERS ON CORRECT DECHIPERED 
    dicio = list(stringToFormat.lower())
    dicio = { i : dicio[i] for i in range(0, len(dicio) ) }

    def addSignals(index, char):
        afterIndex = { i+1 : dicio[i] for i in range(i, len(dicio) ) }
        dicio.update({i : char})
        dicio.update(afterIndex)
        return dicio

    i = 0
    for c in receivedCipher:

        if i == 0:
            dicio.update({i : dicio.get(i).upper()})
                
        if c == " ":
            addSignals(i, " ")
                
        if c == ".":
            addSignals(i, ".")
            if dicio.get(i+1) != None:
                dicio.update({i+1 : dicio.get(i+1).upper()})
                        
        if c == ",":
            addSignals(i, ",")
                                
        if c == "!":
            addSignals(i, "!")  

        if c == "?":
            addSignals(i, "?")  

        if c == "@":
            addSignals(i, "@")   

        if c == "#":
            addSignals(i, "#")  

        if c == "$":
            addSignals(i, "$")   

        if c == "%":
            addSignals(i, "%")  
            
        if c == "&":
            addSignals(i, "&")  

        if c == "*":
            addSignals(i, "*")   

        if c == "-":
            addSignals(i, "-")  
            
        if c == "+":
            addSignals(i, "+") 
            
        if c == "_":
            addSignals(i, "_")  
            
        if c == "+":
            addSignals(i, "+") 

        if c == "[":
            addSignals(i, "[")
                
        if c == "(":
            addSignals(i, "(")
                
        if c == ")":
            addSignals(i, ")")
                        
        if c == "[":
            addSignals(i, "[")
                
        if c == "]":
            addSignals(i, "]")
                        
        if c == "{":
            addSignals(i, "{")
                
        if c == "}":
            addSignals(i, "}")
                        
        if (c == "/"):
            addSignals(i, "/")
                                
        if (c == "\\"):
            addSignals(i, "\\")
                
        if c == "'":
            addSignals(i, "'")
                                            
        if c == "’":
            addSignals(i, "’")
                
        if c == "“":
            addSignals(i, "“")
        
        if c == "”":
            addSignals(i, "”")
                
        if c == "9":
            addSignals(i, "9")
                        
        if c == "8":
            addSignals(i, "8")
                        
        if c == "7":
            addSignals(i, "7")
                        
        if c == "6":
            addSignals(i, "6")
                        
        if c == "5":
            addSignals(i, "5")
                        
        if c == "4":
            addSignals(i, "4")
                        
        if c == "3":
            addSignals(i, "3")
                        
        if c == "2":
            addSignals(i, "2")
                        
        if c == "1":
            addSignals(i, "1")

        if c == "0":
            addSignals(i, "0")
                        
        if c == "ç":
            addSignals(i, "ç")
                                
        if c == "ã":
            addSignals(i, "ã")
                                        
        if c == "á":
            addSignals(i, "á")
                                    
        if c == "à":
            addSignals(i, "à")
                                    
        if c == "ó":
            addSignals(i, "ó")
                                    
        if c == "à":
            addSignals(i, "à")
                                    
        if c == "õ":
            addSignals(i, "õ")
                                    
        if c == "é":
            addSignals(i, "é")
                                    
        if c == "è":
            addSignals(i, "è")
                                    
        # if c == "0":
        #     addSignals(i, "0")
                                    
        # if c == "0":
        #     addSignals(i, "0")
                                    
        # if c == "0":
        #     addSignals(i, "0")
                                    
        # if c == "0":
        #     addSignals(i, "0")
                                    
        # if c == "0":
        #     addSignals(i, "0")
                                    
        # if c == "0":
        #     addSignals(i, "0")
                                    
        # if c == "0":
        #     addSignals(i, "0")
        
        i += 1

    ponctuatedAnswer = "".join(dicio.values())

    # PRINTING AND WRITING IN EXTERNAL FILE THE CORRECT RESULT
    print('\n', ponctuatedAnswer, '\n') 
    if (len(receivedCipher) - len(ponctuatedAnswer) != 0):
            print("Comprimento da string encriptada: " , Fore.YELLOW, len(receivedCipher) , Style.RESET_ALL)
            print("Comprimento da string final: " , Fore.YELLOW, len(ponctuatedAnswer) , Style.RESET_ALL)
    else:
        print("Comprimento da string encriptada: " , Fore.GREEN, len(receivedCipher) , Style.RESET_ALL)
        print("Comprimento da string final: " , Fore.GREEN, len(ponctuatedAnswer) , Style.RESET_ALL)


    # CREATING EXTERNAL FILE
    file = open("decipheredAnswer.txt","w")
    file.write("Chave correta: " + keyFound + "\n")
    file.write(ponctuatedAnswer)
    file.close()

# TEST VARIABLES
ciphered1 = 'Vvv roggf ugdzehj vvv fwcgadcg icwjgr sa hyg wdrzvosevokkce qt kjs Stoqkzzcb ukuzvoc esivwwkqrvsj’ umjvsd (Dfrbwc’u DBK) oef hyg diqqvug fh wehciookknrvwfp cw khj eclthj. Vvv Dfrbwc’u DBK kru sjvosnwjjsu dm kjs Echzqbrn Weuhzvikg cw Kbwqfdchzqb Kgqypccqup  (“Kbjvwkwhf Potkcecz ug Hvebfncxko uc Wehciooçãf”, czjq yeqk sa wku ottceaa “ZVW”) rocei o tqbkglk qt gqzzvwtcz kwfdqwc czfpu nkhy c zfv cw efzvwtkgd. Vvv Hsugfrn Qfwbtkz fh hyg Prt Ojuctkokkce (“Eceuscjc Wgrvtoc fo Ftrvo rfu Ouxcxcrfu rf Dfruwc”) ooug sjrstkocnm ycfjj qikhzeg riozpgk vvv umjvsd. Vvrv kru rlg hf khj kbkgfvuh zp hyg rvhseus fp gfos tqfgqfrvwmg digffiokkjvu, zzms kjs vowjuwfp cw nonasiu WUu. Ocuc, zv vrf pvgb gnoepwei hf nolpqy khj qke fwxkhrn qvthzhwtchvu’ gpuhvo. Hyg qfptckqk ifvy we ooea otvwfpg, zpqcwrzpu tqbjvwkwhzqbrn oef cifwecfp nonuizvg, nkhyqik cbp xwjkpcg gfnikkce. Vvv roggf uggttwsgg kjs Stoqkz GMW jagkga’j kagnsdgbkchzqb gtctggj, cbu vvv oozp qfpqvrhj qt kjs kgqypccqup. Vvvp wk cbrnmjgg kjs cgurn ticavycim oef hyg qikhzeg ugzzxsigr lrce kh. Kjs gcdvt kru plkzu hffo o iggvcftj arfs nkhy kbkgfmksnu oef o jwfmgm zpelkfp cpfwh kjs dqrvng fh arpoxkbx fwxkhrn qvthzhwtchvu’ gpuhvog. Kjsigtfts, zv qfpqcwrvu hych sqhy vvv vstjbzeoc cbu vvv nsxcz ugprvs jjcn c gfewrn rzudlvs, njwtj vru hf ds rugvugvf tiqa kjs tqagtsygbjkce qt kjs kgqypccqup’u gfewrn ijg. Vvtsrhhvt, hyg zrey fh rzhtluwfp cw c uvpsicz lus kgqypccqup vc xwoicbkgs uchr kbkgftjoeisj qpmkcluzp fsccmj vvv liukqzcz jagkga zptftarvwqchzqb.'
ciphered2 = 'Xn ztcmct gtazh, tpt cppoa qaatd kgyxioogaxwik plodrqihuh hike ajgotsbtd admm cee pnl tfnxcqtnb lagh tw sedtlwe smruzt iupgm tnkgyxiiwc tmrhvxqcts. Qc tpxs kdmujnqrabxov, le xgoxdsm p nml axerwpcp uoz xmive mccznpbxov qaatd wc cppobxc tdgqhtqr mies qc ozsez io uteb ihm geyjiztmmcta df bwe atccge qbaot tzpnauez. Xn bwe xgoxdsms iupgm tnkgyxiiwc skweut, av txbtrvpl atcztt sty wu 80-bqi avs ted cppobxc tdgqhtqr mies ige mbptdyms. Tpt ivxtqpl kdnlxtqdna uoz ihm qobw lwviaiik baxh azt dmgidtd chivv tpt efiezcat hekgeb zeg qy xgodxdqcg lxfntrmct etiowtive bd ata ibh bqis. Njrbwez, xn bwe xgoxdsms evrrgetqdn xgoktsa, tiowt lxfntrmct bnpmh on dpmgabxovh azt uatd bd evrrget bwe xxxmas wu av xmive icd ewikw ovt on ihmb wqal jt uatd ndr i eaziikjlig pqmet xs ltcqsel qy bwe wjtkdmm df bwe tdgqhtqr mie. Tw bast tpt cqehmg mwge zdbcht ivaqcsb png ptbpcs, ihm hekgeb zeg xs uddquims aniez tnkgyxiivv eirh jaokz on hifiemc pqmeth on ihm xmive. Bwe ztscata df atvmgat txxtrqbeviat, htiiiaiikpl icatnsqh avs kmn smcsqiidxtg ieais awoe ihii tpt pzdpwhel xmive mccznpbxov hcptmm erwkilts ic enuikxevi avs smruzt win fwg rmpl-bxmm xmive mccznpbxov pnl iricsuxsaxov.'
ciphered3 = '“Nokuscduyrire” rclepy tm oljteqy, alj hmsoqkxsglgzy fgd june hect evilsjeb lrms tfk lgyt ml dgyeyyeq. “Nokuscduyrire” iq ufrkn syeb hy pklgmimas ru ipxirgtc mawy, a lkgyzitklw vrmboione gtrotsje rnar ksagpcy Gmj\'s nxikurboaj rau - rotk. Ipunw os jonikd ru syxcyym ytd kucikrw, chgih mvpmye rne yhijotw zo juvc unc\'y ncogfhop. Napjlw, xapklw, gnb chw tor yaw, ot gy ikvoqyizre, ru tfos bgy, ru hcgr / pkab g nccsjktrkr unepk tfk hcgdjonc xeyjs: “Y nerkrmyevaaj iosvlc nab hect bcgtct, kgrlcj, bcgtct op ycmlfcj fmx sfuwgtg ylfcitgun gt pshlgi” alj / op "G srxagmhr sal roqz hgy lgle zkcyasc ne ugs qnouone ufd niq nerkrmyevaaj ihyxaazeposrocq."'
ciphered4 = 'Th tscs hirv qe cyvtmie uno zocgawfy dnuos tsy nznizh oq jrzry nlyanorlaaby. Thtfcttpews, vllizos alois ffhcecoym awfoh nwz wozjecutthg aureced Z (tsy “FMC”) ayx P (ebe “alois”) tz xuafinutp nhp zuywttinlfies aguiwubwy tz nhp nhtld aures U (ebe “fmec”), qiebofn bpcnr ubwy tz jeczocg tscs qonnnizhawctj in ebetl ohh (wtnhzot nioayrlnizh). Tsy czhcpjt tm cwispfy cyllneo no ebe yittin zz tsledbowx ccspeigcupss, eiwean wp xelf wtnh zhlj nwz jacnipm P lhd Q, uno jllwe gyrj mtccce lednrtwttind in ebe huy ebe zjecuttind urp jeczocgeo (qhtwh tm dzhe qir ebe dukp if pzftwiphcj, oslviwctj uno mclfamcltny). Qir praxjlp, zoc xenlyanizh (rpmp. dcgyutfle) A (Z) sphdd u sthgwy mpmslae ei F (A), ufeyr hbinb tsy llntpl clh dpwrjjt (dcgy) nhp gedmary. Ofl fzlmlf mzxewcnr if alois ccspeigcupss stantzinunefy rynplawczpm, stgpwcftys lhd dcmfftlhezosws cwurtzipm tsy mzxew if “lnoxcc alois” sfagpmtpx bj Vllte lhd Dnrlosd [4]. Cn aureccffac, qe oyfthe mcdtlennizhaw uno ontxicycecoyul gurtunem oq iuc gooyl1, lhd dboh yxelexylj mixjlp aeyyrtw szfuecoym fzl pcixj mirhaeorp uno ynnlyanizh iy nhpme xidpfs. Hy awmo rcvp gocy eqzinceyn szfuecoym fzl sppecul djencftw snbexys. Hy czhcwodp nhln pcixj wrjjtzarljhj cs l lewuttpews stgpwy czhcpjt ei slnidzy hbey fozeeo zrzg tsy czlrpwt lhd qirxul dnayxpzcne'
ciphered5 = 'Vly eyltihv mhhsloenksh esgoyhkguvmip luu klqah dvichfa. Gioqopmwcxcqr ih mhhsloenksh ylyvlyt mh vly hslo sz gbwjehimhi qyuwuiim, vvupwuexcqrm vs nji yzgbcrag sz eshhmxgrnkef krzqvgcxcqr bcw vgih wwcpk nji wqqjwxyt xyelhqpiic uph ansvcp hgxqqve kw qkhy crx esgrpyz. Xbg flgexvl ih mhhsloenksh esgoyhkguvmip ynkpcbmhi kfqfun giotovil crx pinyslmmhi xyelhqpiimyu em vlya elg xifes nix vs nji yoiliihei ih tutxcgw qjs qcrngh nq wngef vly krzqvgcxcqr. Nq ihuylg xbg wyeylkxs crx krngklkxs qj u hmfg, eh grwqhcpk jtswgwm kw lguokvyf. Ihevsrxcqr cu hipi qjih vly hmfg mm uihv. Xbkw jtswgwm ymfn gipzytx hc slkkcp jcni cpxi c wyevyv jcni njen eeh psn di lgex. Oiupabkpy, vly fiwtcjvmip tlqgyuw cu hipi va xbg vyemjkihv sz vly uihv jcni. Nji lggykzyf wyevyv jcnim ymfn fy elupkyf fueo nq slkkcpef hmfg. Fs yes qj ypgifmhi, xbg slkkcpef hmfg acnp hqx vg vych va yhcynjslkdyf tutxcgw, vwx ipps dc nji lggcrmypx qjs bcw nji xgglatnksh mis. Qry qj nji unkitmnjqm wwyf xi rilhslo huve mggotmna mm vly Psymiip efislkxbo. Rigoyqr\'m cpaqvcvlg eeh di urtfkix kr ypglatnksh crx fiwtcjvmip sz oimueagw nq fy uiwwvyf fs fmpkhcpk nji wjelcgngvm krnq rigoyqr vnswmw.'
ciphered6 = 'Mifxekcit PntcygeifyTD ts ry acroittyx wytcy saj mevy dvgeczpvo tf detfrvwy ctnb lnu cekcivge r oixttrw kvj ujtnx ehv tnkprrntzzn fq a stodptitc zxaxp, slnh rd a wtnxprgciee, wzeh r detfrv mlfnk fq drea, byony aj l BzzstcygeTD. Ehv vep nae me ldeu, qoi pxrxpcp, aj ln vycijpktoe/oetcygeify kvj. Typ BzzstcygeTD nodarzdej l fzwtvc flycktoe, hhznh zd crwclwakpd ldier ae tmrre gcotpsjtnx llxzrzehd, lnu ztypr zyffcmreify wytcy ts ipqltrvo tf qiidt iptitemp, aeo typn mprzqy kse mllzoikj ow, ehv vep. Ehv vep ts iptitempd ldier ieqoixaktoe qrfx ae zukauk aakeeiy ffcmvo vzl typ ieeeilcktoe zf kse stodptitc zxaxp wzeh kse wtlkpr wfnteify. Typrvqoip, typ fzwtvc flycktoe xuje bv oejtgepd jz tylt ze pizdlnej l cfyszdtvyt fftgft gltkpre (lnu ehld, kvj). Typ fzwtvc flycktoe xuje acdo sp dvdixyeu eo sp svnuip (i.v. tnwzrdltzzn rmole typ fzygvcpitnk naeyok me iptitempd wcod ehv qiceei quentzzn). Kse tznjtskpntj ow ehv zukauk aakeeiy aeo typ svnuittp zf kse wtlkpr wfnteify aip typ tnz tfaitd dzdcldsvo ie ehzd praei.'
ciphered7 = 'Br unesf huttxbc eusdbkq brp sifsmqwex tceuiy qvawmpfw m nioiezjwy us fseztquu b-dbc unesfw ag tmsgqmw fp szf sd nsdf vqnsff aasoeuefjszt. Xtf mybkqt qmz fq brzpxmuip bx fiief aasoeuefjszt xa ttqdmrjgmmpk jhqoxugc msxudpqt xa ci fbvsfxqe jas qasi fisdpysi mzwieumsbxupr. Fii unesf huttxbc eusdbkq brp sifsmqwex tceuiy dsyqvutie br j-sek jqmhi epyddi fp mxmyyjrmui m qeddix xmfi b-dbce, tgmo xtf vqdiuwip y-vmz tmuxqsr bsspvgqe jdpq fii j-sekt tmtwuok fivavkt ulq qeddix, brp emsjxuai fii j-sek jqmhi ag xtf tmsgqm, ez jruummm wosiqomzh wfbxupr iiidf mybkqt edf mzjxubpxz vqdiuwip brp nek ci moraueffh, mo mzttqdxupr euefjsz xlqsi fii unesfw (ijxt pv ijxtpyf brzpxmumao) eze tmsgqmw fp fq jreqiouip bvq siofmhfh, mo sbumaoex qeddix qefi wijxoi xa emdfgf qeddixt xa fmfiid b gxfedbrof wfbxupr as ez jreqioumao wfbxupr, m eefb wfpvmhi moh dfxdjihbp pfzudi fp vqdsde eze vquvufzq jqmhie, b hmue bssofwepv fp vqdiuwi fii unesfw moh m eefb rquaaso oprzfgfjrs ulq jruummm wosiqomzh wfbxupr, fii uowbfgfjsz txmumao, xtf sbumaoex qefi wijxoi, xtf hmue eusdbkq brp sifsmqwex eihjgq brp ulq eefb tdpgqtwas wa bw fp izbfxf xtf ijdlmokq pj pbxm'
ciphered8 = 'Flp ureqvloxtard nieiipz lzex ygxcuxtar lzh amvlemeuwx ur cgqtzeyfw ldi guihqh huxsur l rvlyihavv fllf enosfzxd rsc flp mpwaglfmzz sq egldgp zyedmpzx cqwzgvnqw, dggs mw pzicsc lzh adseqmy, nieiipz xsq zldmzgw naqaqxtzk mahj ryyoxtard aj eti sawe. Flpei tzgwghp ryyoxtard fllf ecq xsq htdinf vpeywf sq becmwtfmdy. Wtzgp ux te tcatzeio fllf xsq lzex ruzpe tcuscuxj fs eti cqzpdwlx sq flp beetsatcduswaktoew osyeibgiyoid aj amvlemeuwx azpd setic nsok jfzgeusye, me uw ea fp qbaqgeqh etee uqadsgqh ygxcuxtar hupw mphmcd xilp xz uqadsgqh cqwtxmpzgp. Ar eti zflpd llzh, tf md bvzbsdqh etee flp ryyoxtar zr kcaaet, tcqkymrnk eyp ploxlfmzz ecq tcuscuxteio azpd xsq iibvpewtar zr mxyyyuxj. Flfe, mxbvzhio zyedmeusy yej mjqqge flp pirdip aj pjtcqwdusy aj tyqfzmek hfdmys xsqwp blleid. Flp rvlyihavv uw feiqgp lf ltslwuksfmys ecqed aj qgxfdi cqwpmvnt sy tsdf/tldeduxp/zyedmeusy ureqvloxtard. Uxd eyrsidfmzzw nmr logzgre rsc flp afdqvgmxtard aj eti aqvtbecfycuiyf vpxeimxtar zr mxyyyuxj ur cqtcahfomys jpyewqw, le apxp le xsq vppynfmzz my iscy ffdhpz my eqlxp cgqtzeyfw dgtaxixqreqh huxs mhouxtarlx tcaxpur. Lxxsayrt hphiwatpp jzd klexcamyfidfmymp yqqlfsoqw tz vfymymree, xsq gzzgpbxd aj eti qdexqazdo dtsfxh mq eabptoemxi ea xsq myficmgeusye sq zyedmeusy ur zflpd tldeduxto hteileid.'

# VERIFICATION VARIABLES
extendedPossibleKeys = [ 'ceu','dar','lua','ler','mar','sob', 'fel', 'vil', 'paz', 'mal', 'ver', 'ser', 'ego', 'ter', 'bem', 'vir', 'dar', 'bom', 'mas', 'rol', 'elo', 'era', 'tal', 'vis', 'ora', 'dia', 'luz', 'tez', 'com', 'ato', 'dor', 'eis', 'dou', 'hum', 'mim', 'ler', 'fiz', 'dom', 'pro', 'voo', 'sem', 'num', 'mau', 'uma', 'rua', 'sol', 'lei', 'que', 'ajo', 'foi', 'rio', 'pau', 'nau', 'seu', 'ode', 'eco', 'voz', 'fim', 'fez', 'nem', 'ido', 'meu', 'sim', 'vez', 'aia', 'via', 'boi', 'rei', 'jus', 'pai', 'sub', 'asa', 'jaz', 'som', 'tem', 'uns', 'azo', 'ali', 'for', 'rir', 'ata', 'agi', 'por', 'lhe', 'boa', 'uso', 'toa', 'sal', 'amo', 'ufa', 'sua', 'van', 'pra', 'cor', 'cia', 'cal', 'ovo', 'nos', 'par', 'tom', 'kit', 'fio', 'ira', 'mar', 'mui', 'giz', 'loa', 'lar', 'neo', 'mor', 'uau', 'ais', 'rim', 'uno', 'ano', 'pus', 'noz', 'top', 'gay', 'pez', 'mel', 'ele', 'cem', 'pal', 'aio', 'pia', 'cio', 'hem', 'oba', 'foz', 'tio', 'ela', 'uni', 'ida', 'ave', 'gia', 'jia', 'imo', 'tua', 'duo', 'uva', 'dum', 'teu', 'sic', 'cru', 'aro', 'vau', 'gol', 'dez', 'evo', 'ama', 'tia', 'exu', 'das', 'leu', 'deu', 'pio', 'aos', 'box', 'rap', 'dio', 'zen', 'nas', 'val', 'tai', 'oco', 'gaz', 'bio', 'ala', 'dei', 'mil', 'per', 'bis', 'tri', 'rum', 'opa', 'lia', 'aba', 'nua', 'sul', 'bar', 'oca', 'eia', 'pua', 'ado', 'ria', 'sus', 'bel', 'moa', 'oro', 'pan', 'ema', 'ipu', 'sai', 'sor', 'til', 'pum', 'vei', 'iso', 'spa', 'gel', 'min', 'qui', 'nom', 'mol', 'zoo', 'noa', 'aff', 'ero', 'ate', 'pop', 'ror', 'uru', 'itu', 'ola', 'zum', 'aca', 'lio', 'uai', 'ova', 'are', 'coa', 'eta', 'gir', 'gim', 'iru', 'bau', 'fot', 'upa', 'ono', 'ura', 'oma', 'xis', 'osa', 'sio', 'lis', 'bei', 'ulo', 'nha', 'mua', 'raz', 'feo', 'chi', 'var', 'mia', 'ati', 'obi', 'del', 'odo', 'rer', 'net', 'bit', 'ram', 'mio', 'gnu', 'ume', 'idi', 'IDH', 'tau', 'rau', 'ara', 'uca', 'pru', 'ose', 'aga', 'ade', 'dal', 'avo', 'ava', 'ota', 'ilu', 'afe', 'rep', 'omo', 'elu', 'qid', 'eva', 'ogo', 'reo', 'yin', 'cau', 'sen', 'Eva', 'abu', 'ago', 'emu', 'gio', 'psi', 'anu', 'apa', 'ril', 'fum', 'apo', 'ufo', 'gil', 'pul', 'far', 'heu', 'mir', 'out', 'ten', 'meo', 'axe', 'bos', 'uro', 'axi', 'aru', 'uga', 'ula', 'Gal', 'zio', 'adu', 'gau', 'sax', 'opo', 'hic', 'iva', 'Rem', 'ani', 'DDA', 'nit', 'dag', 'efi', 'ujo', 'rus', 'maz', 'uri', 'ren', 'nai', 'edu', 'iri', 'efe', 'oja', 'aal', 'tuo', 'ruz', 'nim', 'log', 'jau', 'bid', 'ppd', 'ozo', 'poa', 'ipo', 'joa', 'iba', 'upo', 'ovi', 'efo', 'udo', 'iei', 'uxi', 'ubi', 'oci', 'uja', 'rem', 'lev', 'bug', 'ici', 'ulu', 'uje', 'saa', 'udu', 'doa', 'poe', 'cha', 'mes', 'nao']
allPossibleKeys = ['sob','fel','vil','paz','mal','ver','ser','ego','ter','bem','vir','dar','bom','mas','rol','elo','era','tal','vis','ora','dia','luz','tez','com','ato','dor','eis','dou','hum','mim','ler','fiz','dom','pro','voo','sem','num','mau','uma','rua','sol','lei','que','ajo','lua','foi','rio','pau','nau','seu','ode','eco','voz','fim','fez','nem','ido','meu','sim','vez','aia','via','boi','rei','jus','pai','sub','asa','jaz','som','tem','uns','azo','ali','for','rir','ata','agi','por','lhe','boa','uso','toa','sal','amo','sua','ufa','van','pra','cor','cia','cal','ovo','nos','par','tom','kit','fio','ira','mar','mui','giz','loa','lar','neo','mor','uau','ais','rim','uno','ano','pus','top','noz','gay','pez','ele','mel','cem','pal','aio','CPF','mEq','pia','hem','cio','oba','foz','tio','ela','uni','ida','ave','gia','OTC','jia','imo','tua','duo','uva','dum','Don','teu','cru','sic','aro','vau','gol','dez','evo','DNA','ama','tia','CEP','exu','leu','das','deu','pio','aos','box','MEC','rap','dio','DIU','zen','nas','val','tai','oco','gaz','bio','dei','ala','mil','per','bis','gap','tri','ONU','rum','opa','lob','aba','lia','nua','sul','bar','lux','him','oca','eia','web','pua','ONG','ado','ria','sus','bel','boy','moa','DOS','oro','pan','ema','ipu','fax','sor','sai','til','PIB','VIP','pum','bip','vei','spa','iso','gel','qui','min','nom','mol','zoo','noa','aff','ero','ate','TPM','pop','ror','mds','hit','emo','ECT','vox','uru','CPI','HIV','fon','itu','ola','vlw','zum','CEO','aca','uai','lio','off','ova','are','coa','abc','eta','gir','MIF','iru','gim','bau','fot','TNT','upa','ono','CBD','ura','oma','xis','app','osa','sio','lis','nhu','hub','bei','CDF','hot','ADP','LSD','ulo','pub','nha','mua','raz','feo','AVC','chi','mia','var','ECG','PVC','IPI','dry','ADN','FSA','set','ati','Rui','DST','obi','del','odo','STJ','net','OMS','rer','bit','mio','gnu','ram','ume','idi','IDH','tau','ara','rau','SOS','uca','HPV','pru','UTI','job','sta','DVD','rpm','ISS','ose','aga','ade','ATP','dal','gag','avo','TOC','ava','bul','fog','PET','www','ota','ilu','afe','rep','sir','omo','MMC','elu','qid','ogo','eva','STF','reo','yin','hip','fox','bru','han','sen','adi','uge','GHz','cau','Eva','abu','ago','emu','psi','gio','anu','BCG','apa','fum','ril','apo','heu','gil','ufo','pul','far','mir','out','ten','CTI','hia','meo','AMB','axe','LDL','bos','uro','axi','aru','HDL','TCU','uga','ula','ppm','Gal','zio','adu','gau','sax','opo','hic','iva','GLP','Rem','ani','DDA','dag','nit','efi','ujo','rus','maz','ren','uri','edu','nai','iza','CBF','IOF','erg','TSE','efe','iri','KGB','csi','oja','tuo','aal','ruz','nim','log','B2C','jau','bid','ppd','DEM','ozo','poa','ipo','joa','B2B','iba','upo','ovi','Ohm','COO','ohm','efo','udo','iei','EEG','uxi','ska','ubi','vhs','oci','uja','rem','bug','lev','ici','ulu','PSL','uje','PSD','saa','uci','LCD','udu','RAM','PMB','PRB','ips','PRP','PPL','PDT','MDB','PCO','PSC','PHS','PTC','PSB','PCB','PMN','PTB','TBT','GPS','duz','lhe','los','mae','mis','nus','ore','pie','pue','reu','soe','tos','tvs','use','voe','vai','zoa','zoe','zua']
securityWords = ['DECRYPTION','SECURITY','SAFETY','TECHNOLOGY','SYSTEM','PAPER','INFORMAT','PROCESS', 'DIGITAL', 'CURRENCY', 'DEVELOPING','ENCRYPTION', 'ANALYSIS', 'RESULTS', 'SECURE', 'APPROACH']
commonWords = ['THIS','OTHER','THE', 'BOTH']

# CIPHERED TEXTS USED IN THE COMPETITIONS

disputa1 = 'nb yonjualyr lbral pghgahhanl shq kopuyfk ca sh vfwewufahtds tdiosf nfx pzuaycay mbucrls, jzyew ieyuaatnlcbfm awyqli uspr mmrxoy shq fypwmfsll ahsglzsnvgh ndqnqm nnuvduody vf u ssmg shq wzsawvwhg euafye ah bjxrj nb vyiwfbh nuwcevuvds nunvncgayf, ahsglzsnvgh fwwhjcgq vruizwm n cyl xuplie. lbvk mgmxl am zwual nb chbo quwnuwl gzy owbnncbj uavuplcbfm bx caxieeugaia ksflyzk ofwlf slr s lvke bj u cjigwwgaia li gzyfw mlknrem fwwhjcgq. ca glqwl gg lrswu lbvkiobyplciw qr uuejcrv ihl u oavyaitjuczcpsf ewpvwq osmrv ia kypghqsll kihjwrk nusn ndfboyq mm gg xrnyygj n iorknvghascewzbj xnlu pgfywwgaia. kypghqds jw ofwx nf iadcaw khwmgaiafuvjy gg anlbrj uakqrjm sjiz 780 koobyplm jzi jglxwx zscads vf jbjnhyuy.lbr uiydyplyq vugs qrjy fmvwwwg li n kczhfr knnlcflcpsf gjynlgrfn, fhypauyds sjydmyaus nfx nfuyqmvk is eynfm. gzy zsca uiaufhkcbf xrjciwx sjiz lbvk mgmxl kbbom gzug ah twhrjuy mmrjm njy pghfaxrjyq li ow u cjigwwgaia xie lbr ahsglzsnvgh fqmgwgf kypmlvls vf ieyuaatnlcbfm.'
disputa2 = 'k axqckkvçt ni bxnhbutçãy é lxpqgslt xi ibmlozokçãw wk khxnbnmgmqtvqwklx, svmooksltnm, wsaiyvblqesltnm x kcmovmskbniwo lx dwwka bxnhbutçõoa x niwya bxlbcxxxaáooql zikk i hbotxqskçãw x/yc bxlbfílny.'
disputa3 = 'kvhgzbgb gqkwct bgbkqzykvu ympuqhga qqvhcqbu i kgizvp ch avczsf qbhwfoihkwb cucpo wva iumfu evq xfqdwfm hjmwt xstacpiz fihc acom ch bvgu ggvgkbwxm opl wv jsewaga oxiwnipnm hq izn whjmf uwqkiz pmhywfm usojsta wv asgug nqyg bvgas wasta ct ucub ch bvgu rq vcv mjgv vcds kv akvr vpov bvgas kvtqzacbwqv wu jskvu ewbukwqcg cvr wvqqvgeqcwaza lwubfkjivmr cvr vpsp bvgg rq vcv jscz wp uwpl hjm woxctbopks qn acqbviwpqbi i ggkitm spdwtwbombv bc rzcvmqv bvgqf umbuqhkds fihc nfqu dgwdnm opl actweqcwa qqls qv hjm'

# FINALS

disputa4 = 'Tas eosr bbcksalwnz isx cf gstpcrd-wnmsgkotxr igtokaamwog gylhefg il on Bbfhfmthihb Shqixhy’l zagrmtfk. Mvil inbjekge ht dbuimol vcnmsnmg agr mxrit ws ifogs th gofs tafeths mvam gekwonglr qofdrhails tas sxqukwtr cf mve ngek-gylhef-wnycrfotbcn kslthihbsawp. Bbfhfmthihb txqhgclhuy von ligxgt iorm cf mvil drhplxa’s lclnhihb, bnh ctbnhh shzvx wt bbtxurtzlr. Hhx wnycrfotbcn lscnfimm phzivwel aulh ougekje mve uoltbcx pemkexb tas hnaag onw hevvnhzozm ilguxg aucum wnycrfotbcn lscnfimm, ig qoghrtgt pwta qukfegh phzivm mhreeg, eqhrxaeem dxjomsd mc txqhgclhuivol jielhihbs. Mvil koky htr fhf pnfphge mve tbaemsbg oy hhx fejiiksd uocdurhinwg fhf tas tksamaegh oy hhx wnycrfotbcn lscnfimm, br aetbs ht igtokaamwog gevirbhy iclbqixg pkcphgae, palsd hb a lhrthezm oy dhxbofsnhzozwc tbaemsbg. Taws tdpkcavv abas mc gbje mc tas phzivwel o shqitz bhorwwnz, cf aimtbilh pxfsiscmwvxg, fhqulsd bb tas ulsrl’g phwnmg oy jixk agr ig cpicsbhihb th hhx qukfegh txqhgclhuiv aowsll'


receivedCipher = disputa4

# TRANSLATE AND STORE DECYPHERS
i = 0
deciphered = []
while i < len(extendedPossibleKeys):
    deciphered.append(Vigenere(extendedPossibleKeys[i]).decipher(receivedCipher))
    i += 1

# SEARCHING AND PRINTING DECIPHERS WITH SECURITY ENGLISH WORDS
j = 0
thisIsCorrect = None
while j < len(deciphered):
    k = 0
    hasWord = -1
    while (k < len(securityWords) and hasWord == -1):
        hasWord = deciphered[j].find(securityWords[k])
        if hasWord != -1:
            thisIsCorrect = deciphered[j]
            keyFound = extendedPossibleKeys[j]
            print( Fore.GREEN + 
                '*** Verificação nº: ', j , '\n' ,
                'Chave: ', keyFound , '\n' ,
                thisIsCorrect , '\n' + Style.RESET_ALL +
                '______________________________________________________________________________________________________________________________________________________________________________________','\n')
        k += 1
    j += 1

if thisIsCorrect != None:
    formatString(thisIsCorrect)

# SEARCHING AND PRINTING DECIPHERS WITH COMMON ENGLISH WORDS
if thisIsCorrect == None:
    j = 0
    while j < len(deciphered):
        k = 0
        hasWord = -1
        while (k < len(commonWords) and hasWord == -1):
            hasWord = deciphered[j].find(commonWords[k])
            if hasWord != -1:
                thisIsCorrect = deciphered[j]
                print( Fore.YELLOW + 
                    '** Verificação nº: ', j , '\n' ,
                    'Chave: ', extendedPossibleKeys[j] , '\n' ,
                    thisIsCorrect , '\n' + Style.RESET_ALL +
                    '______________________________________________________________________________________________________________________________________________________________________________________','\n')
            k += 1
        j += 1

    keyFound =  input(" Insira a chave da descriptação correta : \n")   
    nonPonctuatedAnswer =  input(" Insira a descriptação para formatar para o envio: \n")
    if nonPonctuatedAnswer != '' and keyFound != '':
        formatString(nonPonctuatedAnswer)


# IF NO CORRECT MATCH IS FOUND, PRINT ALL DECIPHERS
if thisIsCorrect == None:
    j = 0
    while j < len(deciphered):
        print(
            'Verificação nº: ', j , '\n' ,
            'Chave: ', extendedPossibleKeys[j] , '\n' ,
            deciphered[j] , '\n'
            '______________________________________________________________________________________________________________________________________________________________________________________','\n')
        j += 1
    
    keyFound =  input(" Insira a chave da descriptação correta : \n")   
    nonPonctuatedAnswer =  input(" Insira a descriptação para formatar para o envio: \n")
    if nonPonctuatedAnswer != '' and keyFound != '':
        formatString(nonPonctuatedAnswer)