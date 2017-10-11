#Alex Karacaoglu
#Crypto_HW5
#I completed problems 1,2,4,6,7,8

import conversions
import euclid_etc

#After using the hex(number) -> string method it puts '0x' at the front and 'L'
#at the end because it is a long and in order to convert back to ASCII using the
#conversions methods provided you need to have those gone
def hex_string_to_hex(s):
    length = len(s)
    if (s[length-1] == 'L'):
        s = s[:length-1]
    if (s[:2] == '0x'):
        s = s[2:]
    return s

#Taken from Professor's solutions to previous HW
def kthroot(N,k):
    low=2
    high=N
    while high-low>1:
        mid=(high+low)/2
        if mid**k<=N:
            low=mid
        else:
            high=mid
    return low

#Problem 1: Short message, small exponent
# problem1("BOPsNWUf4Wlq0x7slBtDBKBAm8/7DZipepU3kklFB2GcurrqQNuouHpxocau3D5otveYhBw7z2AbETcKMuMkWZdToWSo92mK+UhNeP8wXNqVW7I7Fiy/", 89925312925763822584710378409033190578053125728910169871227932983692156412020390339531051155939673506480017767823980121411205241896041063847997991270201142150794495706134903691987753153769920552199651886672073876514247298569925380985174185832099311517867889120692301373911817723374815064908214018503193857221)
def problem1(cipher_b64, N):
    cipher_hex = conversions.b64_to_hex(cipher_b64)
    cipher_b10 = int(cipher_hex,16)
    plaintext_b10 = kthroot(cipher_b10,3)
    plaintext_hex_string = hex(plaintext_b10)
    plaintext_hex = hex_string_to_hex(plaintext_hex_string)
    plaintext_as = conversions.hex_to_as(plaintext_hex)
    return plaintext_as


#Problem 2: Small exponent
# problem2("PBq5gXUhUHA9odbER2Oow3aBRX5VzEPPRCPdcFPZisJSDtoDQtCGiDdcD4q5qNWtA7dMRZxktHzO1kQy1HNmgg6jjUnxuXPIihJgTG4rAQaAFVJrj9THVoaNb+QxovCU61c7N49H+tekr6xyGyGSok6wNnLZtE0GQd8p3zbyIAg=", "a11Wynb/5BbzR2+gfZ5vgyJvlk0VHAUP08F2tvEZKCsS4Q0zaHok9FBf3QSJxn7X+e9+bADoV0aycZpXh/8hchNE5jER156vamjQm/9cmLwVcQeK/IFJOOmvuFEWYwOg3L8r2Jsii6cn/XrStNZ4JypnOhzbyhR5Jd8hsC2pPIo=", "HlPEAzFjvc1ipxHIaig2o6WwpHfsHmIuS07lM0uKmY0VzcxyiOyB8Q0f4yjo8mu5yPYteO5Kiz5W3sk2j/d5ClmU7yUOVRxm5Q8LXymjpkhLK/I+cxO5P3WRjXF6tUiS/7cz+Koox/r1zC0W4BdfCzr3LSjM/khFHyRyxsmW9Ec=", 116352696909960426025864851693810318405618117771451092066454825684677043175680039111752172705287741166921435658711582887107841565748470707915492808066623281928343866378761016071751094691691153177015920723800541267192488702040046723176890027878282090184778778793686252497241689941158021804171328580092708776333, 113159069239053057823530426012762733579195323934158077138440185385412667833688850511263203419882218256057634130377557866771685834979020529147973323837633935391154851580497106210797073916815264166772985134768913514820393183935763151959349642321950865577799563213986693573189083682991881468336071564883866833467, 84645091220488904665996303582605230466879862527671219768265030555132951506114250139685118956675414529710122137796339176130460114790081203074349445462593477716603703644138088562638660083014885373629701703614641595720381677601897924624948376232277832479665238039958287396790532376148968417689500200999461168369)
def problem2(cipher1_b64, cipher2_b64, cipher3_b64, N1, N2, N3):
    a1_hex = conversions.b64_to_hex(cipher1_b64)
    a2_hex = conversions.b64_to_hex(cipher2_b64)
    a3_hex = conversions.b64_to_hex(cipher3_b64)
    a1_b10 = int(a1_hex,16)
    a2_b10 = int(a2_hex,16)
    a3_b10 = int(a3_hex,16)
    N2N3inv = euclid_etc.extended_euclid(N2*N3,N1)
    N2N3inv = N2N3inv[1][0]                             #This is all just plug and chug
    N1N3inv = euclid_etc.extended_euclid(N1*N3,N2)      #into the CRT equation in the 
    N1N3inv = N1N3inv[1][0]                             #Lecture notes #7. x = ... see notes for full equation
    N1N2inv = euclid_etc.extended_euclid(N1*N2,N3)
    N1N2inv = N1N2inv[1][0]
    parta = a1_b10 * ((N2N3inv) % N1) * (N3*N2)
    partb = a2_b10 * ((N1N3inv) % N2) * (N1*N3)
    partc = a3_b10 * ((N1N2inv) % N3) * (N1*N2)
    x = (parta + partb + partc) % (N1*N2*N3)
    cubeRootx = kthroot(x,3)
    x_hex = hex(cubeRootx)
    x_hex = hex_string_to_hex(x_hex)
    plain = conversions.hex_to_as(x_hex)
    return plain


#Problem 4: Common Factor
# problem4("Ur/BIau7ZZBdwxD8P3xDJFJGMfkJDXNU5rbY7GlvlRkGae4NEMo3pMq9r8Jk2akGSj47SZ00L+eTmeMIIfis3RoG7jjBdj03p5lLtgrLwnjP0lzr31fasl5+NVZIvmnoEt56Figi54lIAXEj4ig06MHFG2KfotLYJTnwabangS4=", "CPEXorDgegEqM6UttzFLaccAN/t4QB1FTDS+NL3TSofQlq3Rs/BebbNn4Qj/Vo4FmTwV3P0+n+hlIhjXzOgEgdgV3BmiBE3rIBHqUc+q0FoVvWJU1+jvFpEeellYZMX8vG7O9us5JKfDAHjPaHWZSwv++BSX4rh+5O01flxzlJA=", 87750187518907655534583445808737942078016029371855217057442341331127022016930461105786023716013285380470222803872626192434912740863485532564125627646878636545449869643527771922181597178447982975143657375859594541373428795038041796818858805812228886812351199020336314262507362189851970680226889619203804537151, 59077605606399909603607705484000546044333045357566473814158491087439387780574866766800852465743470772146755309189078604396507686696592563062056700875467732286553829707195406383141965288479916793429869646143662227281782900822010619445408818002981548245734527538573941174294649831309213962935858200869524073603)
def problem4(cipher1_b64, cipher2_b64, N1, N2):
    cipher1_hex = conversions.b64_to_hex(cipher1_b64)
    cipher2_hex = conversions.b64_to_hex(cipher2_b64)
    cipher1_b10 = int(cipher1_hex,16)
    cipher2_b10 = int(cipher2_hex,16)
    common_factor = euclid_etc.euclid(N1, N2)
    if (common_factor ==1):   #Returning an error as requested if there is no common factor
        return "error: there is no common factor"
    else:
        p1 = N1 / common_factor                 #N1 = common_factor * p1    N1,N2 are the 2 different moduli
        p2 = N2 / common_factor                 #N2 = common_factor * p2
        M1 = (p1 - 1) * (common_factor - 1)     #definition of M as in the notes
        M2 = (p2 - 1) * (common_factor - 1)
        d1 = euclid_etc.extended_euclid(65537, M1)  
        d2 = euclid_etc.extended_euclid(65537, M2)
        d1 = d1[1][0]                           #Need to access the desired part bc we get a tuple and then a tuple within it in the second (technically [1]) so i need to access the actual wanted part
        d2 = d2[1][0] + M2                      #Added M2 because I was getting an error bc originally it was negative and we know that a = b(mod n) -> a+n = b(mod n)
        plaintext1_b10 = euclid_etc.repeated_squaring(cipher1_b10, d1, N1)  #message = c^d(mod n), equation from class and from notes, plug and chug
        plaintext2_b10 = euclid_etc.repeated_squaring(cipher2_b10, d2, N2)
        plaintext1_hex = hex(plaintext1_b10)
        plaintext2_hex = hex(plaintext2_b10)
        plaintext1_hex = hex_string_to_hex(plaintext1_hex)
        plaintext2_hex = hex_string_to_hex(plaintext2_hex)
        plaintext1 = conversions.hex_to_as(plaintext1_hex)
        plaintext2 = conversions.hex_to_as(plaintext2_hex)
        return (plaintext1, plaintext2)         #I returned a tuple of the plaintexts bc I decrypted both of them
    

#Problem 6: Diffie Hellman
# problem6(191147927718986609689229466631454649812986246276667354864188503638807260703436799058776201365135161278134258296128109200046702912984568752800330221777752773957404540495707852046983, 5, 176478319826764259370406117740489882944142268114222243573886354279989450112247437716236796057251798300509450763347865746885560883563075519833320667906000345397226327059751213369961, 42694797205671621659845608467948077104282354898632405210027867058530843815065930986742716022222447350595400603633273172816767784236961837688169657044396569579700949515830214254992, 73982478796308483406582889587923018499575337266536017447507799702797406257043632101045569763590982806403627704785985032506296784648293661856246199184245278019913797261546316759270, 1227561673735205443986782574414500194775280963876704725208507831364630528829422611287956320336912905023628854115065478249082243473610928313596901712034514819305660036543382454852)
def problem6(p, g, gx_mod_p, x, firstComponent, secondComponent):
    gxy = euclid_etc.repeated_squaring(firstComponent,x,p)   #gxy = g^xy (mod p)
    plaintext = euclid_etc.extended_euclid(gxy,p)
    plaintext = plaintext[1][0]                              #Just like problem 4, need to get the desired part
    plaintext_b10 = (plaintext * secondComponent) % p
    plaintext_hex_string = hex(plaintext_b10)
    plaintext_hex = hex_string_to_hex(plaintext_hex_string)
    plaintext_as = conversions.hex_to_as(plaintext_hex)
    return plaintext_as


#Problem 7: 
# problem7(191147927718986609689229466631454649812986246276667354864188503638807260703436799058776201365135161278134258296128109200046702912984568752800330221777752773957404540495707852046983, 5, 176478319826764259370406117740489882944142268114222243573886354279989450112247437716236796057251798300509450763347865746885560883563075519833320667906000345397226327059751213369961, 104862672745740711919811315922065122010281934991422240638097533405207971405689057652673577043484488015740722326384001808611695005135028713487234715202873484670021923322009761545457, 17606878671981551311137298337848994393797765223509173646178261989274226953505667592410786573428076963287971811161509360601971410344413313700739795932040261074709506491861567699546, "Now my charms are all o'erthrown and what strength I have's mine own.", 116115839773157782821329377087409766815814624668492668098672866213651171163182813304753241741593566110843721045751605192482170477996370202802973966889697676265503034822908949368607)
def problem7(p, g, gx_mod_p, firstComponent, first_secondComponent, m, second_secondComponent):
    m_hex = conversions.as_to_hex(m)
    m_b10 = int(m_hex,16)
    gxy = euclid_etc.extended_euclid(m_b10,p)
    gxy = gxy[1][0]
    gxy = (first_secondComponent * gxy) % p
    gxy_inverse = euclid_etc.extended_euclid(gxy, p)
    gxy_inverse = gxy_inverse[1][0]
    plaintext_b10 = (gxy_inverse * second_secondComponent) % p
    plaintext_hex_string = hex(plaintext_b10)
    plaintext_hex = hex_string_to_hex(plaintext_hex_string)
    plaintext_as = conversions.hex_to_as(plaintext_hex)
    return plaintext_as


#Problem 8: We are given the discrete log info, y
# problem8(191147927718986609689229466631454649812986246276667354864188503638807260703436799058776201365135161278134258296128109200046702912984568752800330221777752773957404540495707852046983, 5, 176478319826764259370406117740489882944142268114222243573886354279989450112247437716236796057251798300509450763347865746885560883563075519833320667906000345397226327059751213369961, 68188080109582330879868861330998506151774854600403700625797299927558995162740321112260973638619757922646242302104885437536745080299248852065080008358309735875192480724496530325927, 112018886720018236580229932176683955946063514397085867696250318378121351302079624330821244744748925197792097406122146093507280201522804485024833199924734248052247065779216659451112, 138670566126823584879625861326333326312363943825621039220215583346153783336272559955521970357301302912046310782908659450758549108092918331352215751346054755216673005939933186397777)
def problem8(p, g, gx_mod_p, firstComponent, secondComponent, y):
    gxy = euclid_etc.repeated_squaring(gx_mod_p, y, p)
    plaintext = euclid_etc.extended_euclid(gxy, p)
    plaintext_b10 = plaintext[1][0]
    plaintext_b10 = (plaintext_b10 * secondComponent) % p
    plaintext_hex_string = hex(plaintext_b10)
    plaintext_hex = hex_string_to_hex(plaintext_hex_string)
    plaintext_as = conversions.hex_to_as(plaintext_hex)
    return plaintext_as




    
    




    
    
    
    

    
    
    
    
    
    
    
    
    


    
    
