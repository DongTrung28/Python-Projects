#TrungDong
#U42594715
#enter a text file, function will use the dictionary to encrypt the text and return the encrypted version 

Encrypt_Code =  {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8', 
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s', 
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p', 
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m', 
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j', 
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g', 
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d', 
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a', 
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<', 
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=', 
        '{':'[','[':'{','}':']',']':'}'} 

def encrypted(textfile):
    with open(textfile, "r") as encrypted:
        new_file = encrypted.read()

    encrypted_txt = ""
    for character in new_file:
        if character in Encrypt_Code:
            encrypted_txt += Encrypt_Code[character]
        elif character.isspace():
            encrypted_txt += character
    return encrypted_txt


initial_name = input()
final_name = input()

encrypted_text = encrypted(initial_name)
with open(final_name, "w") as encrypted_file:
    encrypted_file.write(encrypted_text)

