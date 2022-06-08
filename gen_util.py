
import os, re
import hashlib
import list_util, xlsx_util
import unicodedata, shutil
import utf_util
def convert_name_for_xlsx(name) :
    if name.endswith("t") :
        return name[:-1]
    else :
        return re.sub( r'[ABCD]$', '',
                re.sub( r'(\d{4})', r'\1 ', name))

def write_list_into_txt(filename, my_list): 
    with open(filename, "w") as f: 
        for item in my_list : 
            f.write( str(item) + "\n")
    #print "Written into <%s>" % filename
    print("Written into <{}>".format(filename))

def read_list_from_txt(filename): 
    output = [ ]
    with open(filename, "r") as f: 
        for line in f:
            output.append(line.strip())
    return output

def read_tuples_from_csv(filename, sep = ","):
    lines = read_list_from_txt(filename)
    output = [ ] 
    for line in lines : 
        output.append( tuple( line.split(sep) ) )
    return output

def generate_password(salt, user_name, decimal = False ) :
    m = hashlib.md5()
    m.update((salt + user_name).encode())
    if decimal is False : 
        return m.hexdigest()[:6]
    else : 
        return str(int(m.hexdigest()[:8], 16))[:6]

def password_of(st_name, salt="None", suffix="Aa4+"):
    m = hashlib.md5()
    m.update( (salt + st_name).encode())
    return (m.hexdigest()[:6] + suffix)



def num_name_split(st_name) :
    sr = re.search( r'^(\d{4})(\S+)' , st_name)
    if sr :
        return (sr.group(1), sr.group(2))
    else :
        return None


def xlsx_difference_dict( file_one, file_two, keep_fn = None ) :
    one_sheet_lists = xlsx_util.read_xlsx_sheets_into_list(file_one)
    two_sheet_lists = xlsx_util.read_xlsx_sheets_into_list(file_two)
    for sheet_name in list_util.complement( one_sheet_lists.keys(),
                                             two_sheet_lists.keys()):
        #print "%s of %s not found in %s" % (sheet_name, file_one, file_two)
        print("{} of {} not found in {}".format(sheet_name,file_one, file_two))
    for sheet_name in list_util.complement( two_sheet_lists.keys(),
                                             one_sheet_lists.keys()):
        #print "%s of %s not found in %s" % (sheet_name, file_two, file_one)
        print("{} of {} not found in {}".format(sheet_name, 
            file_two, file_one))
    output = { }
    for sheet_name in sorted(list_util.intersect(one_sheet_lists.keys(), 
                                                 two_sheet_lists.keys())):
        first_triples = [ ]
        first_dict = { }
        for i, row in enumerate( one_sheet_lists[sheet_name] ):
            for j, rec in enumerate( row ) : 
                if type(rec) in [int, float] or (type(rec) is str and len(rec)>0) : 
                    first_triples.append( (i, j, rec) )
                    first_dict[ (i,j) ] = rec
        second_triples = [ ]
        second_dict = { }
        for i, row in enumerate( two_sheet_lists[sheet_name] ):
            for j, rec in enumerate( row ) : 
                if type(rec) in [int, float] or (type(rec) is str and len(rec)>0) : 
                    second_triples.append( (i, j, rec) )
                    second_dict[ (i,j) ] = rec
        first_indices = [ (i,j) for i,j,rec in first_triples ]
        second_indices = [ (i,j) for i,j,rec in second_triples ]
        for i,j in list_util.complement( first_indices, second_indices ) : 
            output[ (sheet_name, i, j) ] = (first_dict[ (i,j) ], '')
        for i,j in list_util.complement( second_indices, first_indices ) : 
            output[ (sheet_name, i, j) ] = ('', second_dict[ (i,j) ])
        for i,j in list_util.intersect( first_indices, second_indices ) : 
            if  first_dict[ (i,j)] !=  second_dict[ (i,j) ] : 
                output[ (sheet_name, i, j) ] = (first_dict[ (i,j)], second_dict[ (i,j) ])
        if keep_fn is not None : 
            for i,j in list_util.intersect( first_indices, second_indices ) : 
                if keep_fn(first_dict[ (i,j) ]) : 
                    output[ (sheet_name, i, j) ] = (first_dict[ (i,j)], second_dict[ (i,j) ])
    return output
    


def write_tuples_into_txt(filename, my_list): 
    with open(filename, "w") as f: 
        for item in my_list : 
            #f.write( ' '.join([ str(c).encode() for c in item]) + "\n".encode())
            f.write(' '.join(item) + '\n') 
    #print "Written into <%s>" % filename
    print("Written into <{}>".format(filename))


def apply_dict( my_dict, in_str ) : 
    if in_str in my_dict : 
        return my_dict[in_str]
    else : 
        return in_str

def replace_by_dict(my_dict, in_str):
    my_keys = sorted(my_dict.keys())
    output = in_str 
    for word in my_keys : 
        output = output.replace(word, my_dict[word])
    return output
    


def dict_to_fn( my_dict ) : 
    f = lambda x : apply_dict(my_dict, x)
    return f 


def korean_syllables(utf_str): 
    return [c.encode("utf-8") for c in unicode(utf_str, "utf-8")]

def inserted(input_list, item, idx = 0) : 
    return input_list[:idx] + [item] + input_list[idx:]


def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc



def write_dict_into_txt(filename, in_dict):
    output = [ ] 
    for k in sorted(in_dict.keys()):
        output.append("{},{}".format( k, in_dict[k]))
    write_list_into_txt(filename, output)
    
def nfd_to_nfc(my_str):
    try: 
        output = unicodedata.normalize("NFC", unicode(my_str, 
            "utf-8")).encode("utf-8")
        return output
    except:
        return my_str

def nfc_to_nfd(my_str):
    try: 
        output = unicodedata.normalize("NFD", unicode(my_str, 
            "utf-8")).encode("utf-8")
        return output
    except:
        return my_str


def pad_str(my_str, length, pad_with = " ") :
    given_length = utf_util.korean_len(my_str)
    if  given_length >= length :
        return my_str
    else :
        return (pad_with*(length - given_length ) + my_str)

def print_table( str_tuples ) :
    n = max( map(len, str_tuples))
    padded_list = [ list_util.pad(tpl,  n) for tpl in str_tuples]
    column_widths  = { }
    for i in range(n) :
        column_widths[i] = max( map(
            lambda x: utf_util.korean_len(x[i]) + 1, padded_list))
    lines = [ ]
    for tpl in str_tuples :
        lines.append( ' '.join( [pad_str(c, column_widths[i], " ")
            for i,c in enumerate(tpl)]   ))
    for line in lines :
        print(line)

def write_dict_into_txt(filename, my_dict):
    output = [ ] 
    for k in sorted(my_dict.keys()):
        output.append( str(k) + " " + str(my_dict[k]) )
    write_list_into_txt(filename, output)
    




trashbinname = ".trashbin"
trashbin = os.path.expanduser( "~/" + trashbinname)

def leave_a_backup( fname ) :
    if fname.startswith("/"):
        full_fname = fname
    elif fname.startswith("~"):
        full_fname = os.path.expanduser(fname)
    else:
        full_fname = os.path.abspath("." + os.sep + fname)
    rel_fname = os.path.split(full_fname)[1]
    without_ext, ext = os.path.splitext(rel_fname)
    backed_ups = [c for c in os.listdir(trashbin)
        if c.startswith(without_ext + "-")]
    if len(backed_ups) == 0 :
        backup_fname = "{}{}{}-{}{}".format(trashbin,os.sep , without_ext,
            1, ext)
    else :
        new_num = 1 + max( [ int(os.path.splitext(c)[0].replace(
            without_ext+"-","")) for c in backed_ups])
        backup_fname = "{}{}{}-{}{}".format(trashbin,os.sep , without_ext,
            new_num, ext)
    print(" Backing up..Copying <{}> to <{}>..".format(full_fname,
        backup_fname))
    shutil.copyfile( full_fname, backup_fname )



