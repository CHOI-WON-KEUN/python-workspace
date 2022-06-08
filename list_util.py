# -*- coding: utf-8 -*-

import functools

def all_true( mylist ) : 
    for item in mylist : 
        if item is False : 
            return False 
    else: 
        return True

def some_true( mylist ) : 
    for item in mylist : 
        if item is True : 
            return True 
    else: 
        return False

        
def flatten( mylist ) : 
    if len(list(mylist)) == 0 : 
        return [ ] 
    else : 
        return list(functools.reduce( lambda x,y : list(x)+list(y), mylist, [ ] ))

def union( mylist, *sec_lists ) :
    output = [ ]
    for c in mylist : 
        if c not in output : 
            output.append(c) 
    for sec in sec_lists : 
        for c in sec : 
            if c not in output : 
                output.append(c) 
    return output

def intersect( mylist, *sec_lists ) :
    output = [ ] 
    for c in mylist : 
        for sec in sec_lists : 
            if c not in sec : 
                break 
        else : 
            output.append(c)
    return output

            
def complement( mylist, *sec_lists ) :
    if len(sec_lists) == 0 : 
        return mylist 
    myunion = union( *sec_lists)
    output = [c for c in mylist if c not in myunion ]
    return output


def count( mylist, cond_f ) : 
    mycount = 0 
    for c in mylist : 
        if cond_f(c) is True : 
            mycount += 1 
    return mycount
    

def partition(mylist, n) : 
    output = [ ] 
    for i, item in enumerate(mylist) : 
        if i%n == 0 : 
            output.append( [ ] )
        output[-1].append( item )
    return output

def partition_by_list(mylist, num_list) : 
    output = [ ]
    i = 0
    for n in num_list : 
        output.append( [ ] )
        for k in range(n):
            output[-1].append(mylist[i])
            i += 1 
    return output


def jpr( mylist ) :
    print(' '.join(mylist))

def npr( mylist, rtn  = False  ) :
    for i, c in enumerate(mylist):
        print(i, '"' + c + '"' )
    if rtn : 
        return mylist


def is_subset( myset, bigset ) :
    for c in myset :
        if c not in bigset :
            return False
    else :            
        return True
            

def maximizer( cells, func ) :
    output = cells[0]
    curr_val = func( cells[0] )
    for i in range(1,len(cells)) :
        test_val = func( cells[i] )
        if test_val > curr_val :
            curr_val = test_val
            output = cells[i]
        else :
            continue
    return output


def minimizer( cells, func ) :
    return maximizer(cells, (lambda x : - func(x) ) )


def transposed( my_list ) : 
    my_dict = { }
    for i, row in enumerate(my_list) : 
        for j, item in enumerate(row) : 
            my_dict[ (i, j) ] = item 
    output = [ ] 
    for k in range( max( [j for i,j in my_dict] ) + 1) : 
        tmp_row = [ ]
        for n in range(max( [i for i,j in my_dict]) + 1) : 
            if (n, k) in my_dict : 
                tmp_row.append( my_dict[ (n,k) ] ) 
            else : 
                tmp_row.append( "" )
        output.append(tmp_row)
    return output 


                
def collect_on_first(pairs) : 
    st_name_list = sorted( union([c[0] for c in pairs]) )
    output = [ ]
    for st_name in st_name_list : 
        new_list = [st_name] + sorted([c[1] for c in pairs if c[0] == st_name]) 
        output.append(new_list)
    return output


def pad(input_list, length, pad_item = "") :
    if type(input_list) is list :   
        my_list = input_list
    else : 
        my_list = list(input_list)
    if len(my_list) >= length : 
        return my_list 
    else : 
        return my_list + [pad_item for i in range(length - len(my_list))]



def join_npr( mylist, sep = ' ' ) :
    for i, c in enumerate(mylist):
        print(i, sep.join(c) )

def is_maximal_in( a_set, set_list, compare = is_subset) :
    set_size = len(a_set)  
    for b_set in set_list : 
        if b_set != a_set and compare(a_set, b_set) : 
            return False
    else: 
        return True

def difference_list(a_set, b_set) : 
    return (complement(a_set, b_set) + complement(b_set, a_set))


def reversed_dict(my_dict) :
    vals = union( [my_dict[k] for k in my_dict] )
    output = { }
    for v in vals : 
        output[v] = [ k for k in my_dict if my_dict[k] == v ]
    return output

def reversed_list_dict(my_dict) : 
    output = { } 
    for k in my_dict.keys() : 
        for val in my_dict[k] : 
            output[val] = k 
    return output


def check_append( my_list, new_item, str_fn = str, silent=False ) :
    if new_item in my_list :
        if not silent:
            #print "%s is already in the list. Doing nothing."%str_fn(new_item)
            print("{} is already in the list. Doing nothing.".format(
                str_fn(new_item)))
        return False
    else :
        my_list.append(new_item)
        if not silent:
            #print "%s is appended." % str_fn(new_item)
            print("{} is appended.".format(str_fn(new_item)))
        return True



def check_remove( my_list, memb_item, str_fn = str, silent=False ) :
    if memb_item not in my_list :
        if not silent:
            print("{} is not in the list. Doing nothing.".format(
                str_fn(memb_item)))
        return False
    else :
        my_list.remove(memb_item)
        if not silent:
            print("{} is removed.".format(str_fn(memb_item)))
        return True


def move_in_list(my_list, from_ind, to_ind) :
    item = my_list.pop(from_ind)
    my_list.insert(to_ind, item)
    #print "Moving.. %d:%s -> %d:%s " % ( from_ind, item, to_ind, my_list[to_ind] )
    print("Moving.. {}:{} -> {}:{} ".format( from_ind, 
        item, to_ind, my_list[to_ind] ))
    return True

def show_dict(my_dict, key_fn = str, val_fn = str) : 
    for k in sorted(my_dict.keys()) : 
        print(key_fn(k), "->",  val_fn(my_dict[k]))
    

def distinct_pairs(my_list) : 
    if len(my_list) <= 1 : 
        return [ ]
    else : 
        output = [ ] 
        for i in range(0,len(my_list)-1) : 
            for j in range(i+1,len(my_list)) : 
                output.append( (my_list[i], my_list[j]) )
    return output


def distinct_triples(my_list) : 
    if len(my_list) <= 2 : 
        return [ ]
    else : 
        output = [ ] 
        for i in range(0,len(my_list)-2) : 
            for j in range(i+1,len(my_list)-1) : 
                for k in range(j+1, len(my_list)):
                    output.append( (my_list[i], my_list[j], my_list[k]) )
    return output



def do_cycle(my_list, count = 1 ) :
    if count == 1 : 
        my_list.append( my_list[0])
        my_list.pop(0)
        #print "Cycling.. 0:%s -> %d:%s " % ( my_list[-1], len(my_list)-1, my_list[-1])
        print("Cycling.. 0:{} -> {}:{} ".format( my_list[-1],
                len(my_list)-1, my_list[-1]))
        #print "Now 0:%s" % my_list[0]
        print("Now 0:{}".format(my_list[0]))
        return True
    else : 
        for k in range(count) : 
            do_cycle(my_list, 1)
        return True

def cycled(my_list, count = 1, start = 0, end = 0) : 
    if end == 0 : 
        r_end = len(my_list)
    else : 
        r_end = end
    fix_list = my_list[:start]
    ending_fix_list = my_list[r_end:]
    head_list = my_list[start:(start+count)]
    tail_list = my_list[(start+count):r_end]
    return fix_list + tail_list + head_list + ending_fix_list

def uncycled(my_list, count = 1, start = 0, end = 0) : 
    if end == 0 : 
        r_end = len(my_list)
    else : 
        r_end = end
    fix_list = my_list[:start]
    ending_fix_list = my_list[r_end:]
    tmp_list = my_list[start:r_end]
    head_list = tmp_list[:-count]
    tail_list = tmp_list[-count:]
    return fix_list + tail_list + head_list + ending_fix_list

def copy_inserted_at( my_list, ind ) : 
    head_list = my_list[:ind]
    tail_list = my_list[ind:]
    return ( head_list + [ tail_list[0] ] + tail_list )

def column_pack(my_tuples, n) : 
    pad_tuple = ['' for c in my_tuples[0]]
    clr =  n - (len(my_tuples) % n)
    longer_one = my_tuples + [ pad_tuple for k  in range(clr)]
    blocks = partition(longer_one, n)
    output = transposed( flatten( [ transposed(bl) for bl in blocks ] ))
    return output

def filter_dict( fn, in_dict, on_key = False ) : 
    output = { }
    for k in in_dict : 
        if on_key is False and fn(in_dict[k]) is True : 
            output[k] = in_dict[k]
        elif on_key is True and fn(k) is True : 
            output[k] = in_dict[k]
    return output

#def partial(fn, first_arg) : 
    #return ( lambda x: fn(first_arg, x) )


def map_at( fn, my_list, level = 2 ) : 
    if level == 1 : 
        return list(map(fn, my_list))
    else : 
        return list(map( lambda x: map_at( fn, x, level = level-1), my_list))

def map_by_index(fn, index, my_list) : 
    output = [ ] 
    for i, item in enumerate(my_list) : 
        if i == index : 
            output.append( fn(item) )
        else : 
            output.append(item)
    return output


def dict_map(in_dict, in_list):
    output = [ ] 
    for item in in_list:
        if item in in_dict : 
            output.append(in_dict[item])
        else : 
            output.append(None)
    return output



def collect_items( tuples, item_index = 0, filter_index = 1, fn = (lambda x: False) ) : 
    output = [ ] 
    for items in tuples : 
        if fn( items[filter_index] ) : 
            output.append(items[item_index])
    return output
    
def lookup_in_tuples(my_tuples, in_str) : 
    for rec in my_tuples : 
        for fd in rec : 
            if fd.find(in_str) >= 0 : 
                return rec

def grep_from_list(keyword_list, items):
    output = [ ] 
    for item in items:
        for k in keyword_list:
            if item.find(k) >= 0 : 
                output.append(item)
                break
    return output
                

def prefix_filter(prefix, str_list): 
    return [item for item in str_list if item.startswith(prefix)]

def grep_filter(subword, str_list): 
    return [item for item in str_list if item.find(subword)>=0]


def filter_on_entry( search_value, tuples,  filter_index = 0, fn = (lambda x: x) ) : 
    output = [ ] 
    for items in tuples : 
        if fn( items[filter_index] ) == search_value : 
            output.append(items)
    return output
    
def lookup_in_tuples(my_tuples, in_str) : 
    for rec in my_tuples : 
        for fd in rec : 
            if fd.find(in_str) >= 0 : 
                return rec

def mode(input_list, nth = 0 ):
    max_n = 0
    output = [ ] 
    for item in union(input_list) : 
        new_count = input_list.count(item)
        if new_count >= max_n : 
            max_n = new_count
            output.append( item )
    return output[-1 - nth]


def update_value_by_dict(target_dict, val_val_dict, verbose=True):
    k_list = target_dict.keys()
    k_list.sort()
    for k in k_list : 
        if target_dict[k] in val_val_dict : 
            print(k, target_dict[k], "->", val_val_dict[target_dict[k]])
            target_dict[k] = val_val_dict[target_dict[k]]


def duplicates(my_list):
    uniq_list = [ ] 
    output = [ ]
    for item in my_list:
        if item not in uniq_list:
            uniq_list.append(item)
        else:
            output.append(item)
    return union(output)

def firsts(my_list) : 
    return list(map(lambda x:x[0], my_list))

def seconds(my_list) : 
    return list(map(lambda x:x[1], my_list))

def lasts(my_list) : 
    return list(map(lambda x:x[-1], my_list))

def last_index(my_list, item):
    for i in range( len(my_list) -1, -1, -1):
        if my_list[i] == item : 
            return i
    else:
        raise ValueError("No {} found in the list".format(item))

def splice_by_indices(my_list, ind_list, to_j ):
    trimmed = [ ] 
    for i, item in enumerate(my_list): 
        if i not in ind_list : 
            trimmed.append(item)
    inserts = [ my_list[i] for i in ind_list]
    output = trimmed[:to_j] + inserts + trimmed[to_j:]
    return output






