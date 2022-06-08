import re
import subprocess 

def convert_romans( mystr ) :
    conv_pairs = [("\xe2\x85\xa0", "I"), ("\xe2\x85\xa1", "II"),
            ("\xe2\x85\xa2", "III"), ("\xe2\x85\xa3", "IV"),
        ("\xe2\x85\xa4", "V"), ("\xe2\x85\xa5", "VI"),
    ("\xe2\x85\xa6", "VII"), ("\xe2\x85\xa7", "VIII"),
    ("\xe2\x85\xa8", "IX"), ("\xe2\x85\xa9", "X"),
    ("\xe2\x85\xaa", "XI"), ("\xe2\x85\xab", "XII"),
    (" ", ""), ("\xef\xbc\x86", "&") ]
    output = mystr
    for c in conv_pairs :
        output = output.replace( c[0], c[1])
    return output

def korean_len(my_str) :
    curr_len = len( re.sub( r'\W{3}', 'aa', my_str ) )
    return curr_len 

def revert_romans( mystr ) :
    conv_pairs = [ 
("\xe2\x85\xa7", "VIII"),   ("\xe2\x85\xa6", "VII"), ("\xe2\x85\xa5", "VI"),
("\xe2\x85\xa3", "IV"), ("\xe2\x85\xab", "XII"),
    ("\xe2\x85\xaa", "XI"), ("\xe2\x85\xa8", "IX"), ("\xe2\x85\xa9", "X"),
("\xe2\x85\xa2", "III"), ("\xe2\x85\xa1", "II"),
        ("\xe2\x85\xa4", "V"), ("\xe2\x85\xa0", "I"), ("\xef\xbc\x86", "&") ]
    rev_pairs = [ (c[1], c[0])  for c in  conv_pairs]
    output = mystr
    for c in rev_pairs :
        output = output.replace( c[0], c[1])
    return output

def read_from_clipboard():
    return subprocess.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'})