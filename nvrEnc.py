######################################
#        Code-decode .py file        #
#    https://vk.com/neverhidehere    #
#            Python 3.7.1            #
######################################

######################################
#              Settings              #

verbose = 1
    # if verbose = 1 shows a detailed report in the NHVcoder.log file
    # if verbose = 0, only the encoding result will be displayed
    #
    # default is verbose = 1

#                                    #
######################################



import math
import random
import time

symblog = open("NHVcoder.log",'w')
symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Load variables' + '\n')
if verbose != 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] verbose != 1' + '\n')
pi = math.pi
chars = "abcdefghijklmnopqrstuvwxyz"
symb = {}
symbn = 0
if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Load arrays and dicts' + '\n')
char = {'a': 1.1, 'b': 2.2, 'c': 3.3, 'd': 4.4, 'e': 5.5,
        'f': 6.6, 'g': 7.7, 'h': 8.8, 'i': 9.9, 'j': 10.1,
        'k': 11.11, 'l': 12.12, 'm': 13.13, 'n': 14.14, 'o': 15.15,
        'p': 16.16, 'q': 17.17, 'r': 18.18, 's': 19.19, 't': 20.20, 'u': 21.21,
        'v': 22.22, 'w': 23.23, 'x': 24.24, 'y': 25.25, 'z': 26.26}
numblist = [1,2,3,4,5,6,7,8,9,0]
vals = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1,
        11.11,12.12,13.13,14.14,15.15,16.16,17.17,
        18.18,19.19,20.2,21.21,22.22,23.23,24.24,25.25,26.26]



if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Starts working! ' + '\n')

for i in range(26):
    for j in range(26):
        K = round(vals[j]*vals[i],5)
        V = [chars[j],chars[i]]
        V.sort()
        
        if (symb.get(K,False)):
            old = symb.get(K)
            if (not(V[0] in old[0] and V[1] in old[1])):
                symb[K][0].append(V[0])
                symb[K][1].append(V[1])
                
                symb[K][0].sort()
                symb[K][1].sort()
        else:
            symb[K] = [[V[0]], [V[1]]]
if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Creating symbdb ' + '\n')

symbdb = open('symdb.txt','w')
kk = len(symb)
for m in symb:
    symbdb.write('| ' + str(m) + ' -> ' + str(symb[m]) + " | \n")
symbdb.write(str(symb))
symbdb.close
if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Closing symbdb' + '\n')

#print(symb)
n = '' 

def ncoder(inputnumb):
    numres = round(float(inputnumb*inputnumb*pi),5)
    n = "3"+"-"+str(numres)
    print(n)
    return n
    
                
#print(len(symb.items()),len(symb2.items()))
#print("\n")
#print()
    
def ec_c(char):
    if (char==" "): return "0-0"
    elif (char == '.'): return '0-1'
    elif (char == ','): return '0-2'
    elif (char == ':'): return '0-3'
    elif (char == ';'): return '0-4'
    elif (char == '?'): return '0-5'
    elif (char == '!'): return '0-6'
    elif (char == '('): return '0-1.5'
    elif (char == ')'): return '0-1.6'
    char = char.lower()
    if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] "Char" lower!' + '\n')

    if char not in chars:
        if int(char) == int(char):
            char = int(char)
            if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Found (int)!' + '\n')

    typechar = type(char)
    if typechar == int:
        numbret = ncoder(int(char))
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Gen number!' + '\n')

        return numbret    
    try:
        char_ind = chars.index(char)
    except:

        return "?"
    if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Creating random..' + '\n')
    side_ind = random.randint(0,25)
    char_val = vals[char_ind]
    side_val = vals[side_ind]
    
    if (side_val==0.0):
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Returning "0-' + str(char_val) + '"\n')
        return "0-" + str(char_val)
        
    inTocd = round(char_val * side_val, 5)
    
    if (char_val < side_val):ind = 1
    else: ind = 2
    ind2 = symb[inTocd][ind-1].index(char)+1
    if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
        ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Returning "' 
        + str(str(ind) + str(ind2) + "-" + str(inTocd)) + '"\n')
    return str(ind) + str(ind2) + "-" + str(inTocd)
    
def ec(text):
    text = list(text)
    code = []
    
    for i in range(len(text)):
        code.append(ec_c(text[i]))
    
    return "/".join(code)


def dc_c(code):
    if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Decoding... ' + '\n')

    if (code == "0-0"): 
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show _ ' + '\n')

        return " "

    elif (code == '0-1'): 
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show . ' + '\n')

        return '.'
    elif (code == '0-2'): 
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show ","' + '\n')
        return ','
    elif (code == '0-3'): 
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show ":" ' + '\n')

        return ':'
    elif (code == '0-4'): 
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show ";" ' + '\n')
        return ';'
    elif (code == '0-5'): 
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show "?" ' + '\n')

        return '?'
    elif (code == '0-6'): 
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show "!" ' + '\n')

        return '!'
    elif (code == '0-1.5'): 
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show "(" ' + '\n')

        return '('
    elif (code == '0-1.6'): 
        if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show ")" ' + '\n')

        return ')'
    if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Number or letter ' + '\n')

    code = code.split("-")
    err = len(code)
    #print(err, end=' ')
    if err != 1: code[1] = float(code[1])
    if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Splitted!' + '\n')
    if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Start place numbers!' + '\n')

    if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] No numbers here ' + '\n')

    if (len(code)==1): return ""
    if (code[0]=="0"): return chars[vals.index(code[1])]
    if (code[0]=='3'):
        numbEnc = round(code[1]/pi, 5)
        numbEn = math.sqrt(numbEnc)
        numbEn = int(numbEn)
        return str(numbEn)
    
    if (not(symb.get(code[1], True))): return "?"
    if verbose == 1: symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
    ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) +
     ' ] Returning "' + symb[code[1]][int(code[0][0])-1][int(code[0][1])-1] +'"\n')

    return symb[code[1]][int(code[0][0])-1][int(code[0][1])-1]
    
    
def dc(code):
    code = code.split("/")
    text = ""
    
    for i in range(len(code)):
        text += dc_c(code[i])
        
    return text



qq = 'cmd'
while qq != 'quit':
    if qq == 'end' or qq == 'break': break
    elif qq == 'verbose':
        if verbose == 0:
            verbose = 1
            print("Verbose msgs was enabled")
            symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
            ' [ Logging to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Verbose was enabled!' + '\n')
        if verbose == 1:
            verbose = 0
            print("Verbose msgs was disabled")
            symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
            ' [ Logging to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Verbose was disabled!' + '\n')
    elif qq == 'cd':
        inp = str(input('Type ur text here: '))
        enc = ec(inp)
        if verbose == 1: symblog.write('\n')
        dec = dc(enc)
        symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
            ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Stop decoding..' + '\n')
        symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
            ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show output ' + '\n')

        print(inp,"\n\n", enc, "\n\n")
        symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
            ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] End! ' + '\n\n')
        symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
            ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Comleted in ' + str(time.clock()) 
            + '(s) \n| Result: (txt and enc) \n' + str(enc) + '\n' + str(dec)  + '\n\n\n')
        print(inp,"\n\n", enc, "\n")
        print('\n Open NHVcoder.log for more info')
    elif qq == 'enc':
        enc = str(input('Type ur encoded text here: '))
        if verbose == 1: symblog.write('\n')
        dec = dc(enc)
        symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
            ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Stop decoding..' + '\n')
        symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
            ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Show output ' + '\n')

        print(dec,"\n\n", enc, "\n\n")
        symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
            ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] End! ' + '\n\n')
        symblog.write(str(time.strftime("%Y.%m.%d | %H.%M.%S")) + 
            ' [ Wtiting to NHVcoder.log | Time\'s been wasted: ' + str(time.clock()) + ' ] Comleted in ' + str(time.clock()) 
            + '(s) \n| Result: (txt and enc) \n' + str(enc) + '\n' + str(dec)  + '\n\n\n')
        print(dec,"\n\n", enc, "\n")
        print('\n Open NHVcoder.log for more info')
    elif qq == 'cmd':
        if verbose == 1:
            vcmd = 'true'
        elif verbose == 0:
            vcmd = 'false'
        print('\n\n\n\n\n\n\n\n\n ███╗░░██╗██╗░░░██╗██████╗░ \n' +
        ' ████╗░██║██║░░░██║██╔══██╗ \n'+
        ' ██╔██╗██║╚██╗░██╔╝██████╔╝ \n'+
        ' ██║╚████║░╚████╔╝░██╔══██╗ \n'+
        ' ██║░╚███║░░╚██╔╝░░██║░░██║ \n'+
        ' ╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝ \n')

        print(' ███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░█████╗░███╗░░██╗\n'+
        ' ██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║\n'+
        ' █████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║ \n'+
        ' ██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║\n'+
        ' ███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║\n'+
        ' ╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝\n')

        print(' ░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗\n'+
        ' ██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║\n'+
        ' ╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║\n'+
        ' ░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║\n'+
        ' ██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║\n'+
        ' ╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝\n')

        print('                          - - - Commands - - -\n'+
        '"cd" - you enter text: the encoded version is returned to NVHloger.log file\n'+
        '"enc" - you enter the encoded text: the decoded version is returned to NVHloger.log.\n'+
        '"cmd" - show commands menu\n'+
        '"verbose" - disabling/enabling verbose msgs in NVHloger.log ( now verbose: ' + str(vcmd) + ' )\n'
        '"end" - program stop\n\n'+
        'vk.com/neverhidefamily | NVR coder | 24.01.2020\n')
    else: print('Invalid command')
    qq = str(input(str(__file__) + ' $nvr -> '))
symblog.close
