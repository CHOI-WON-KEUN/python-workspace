# -*- coding: utf-8 -*-


import sys, os, re
import filecmp, time
from optparse import OptionParser
import shutil

rc_filename = ".dsync"
dropbox = "~/Dropbox/dsync_bin"
trashbin = os.path.expanduser( "~/.trashbin")

def read_rc():
    output = { }
    rc_fn = os.path.expanduser("~/" + rc_filename)
    if not os.path.exists(rc_fn):
        return output
    with open(rc_fn) as f:
        data = f.readlines()
    for line in data : 
        if line.strip().startswith("Source:"):
            curr_source_dir = line.split(":")[1].strip()
            output[curr_source_dir] = [ None, [ ] ]
        elif line.strip().startswith("Target:"):
            curr_target_dir = line.split(":")[1].strip()
            output[curr_source_dir][0] = curr_target_dir 
        elif line.strip().startswith("Files:"):
            continue
        else:
            new_filename = line.strip()
            output[curr_source_dir][1].append(new_filename) 
    return output

def write_rc(connect_dict):
    rc_fn = os.path.expanduser("~/" + rc_filename)
    with open(rc_fn, "w") as f:
        for i, source_dir in enumerate(sorted(connect_dict.keys())):
            target_dir = connect_dict[source_dir][0]
            filename_str = "\n".join(connect_dict[source_dir][1])
            #if len(connect_dict[source_dir][1]) <= 1:
                #print('|{}|'.format(filename_str))
                #print(source_dir,target_dir)
                #print(connect_dict[source_dir][1])
            if i > 0 : 
                f.write("\n")
            f.write("Source:"+source_dir+"\n")
            f.write("Target:"+target_dir+"\n")
            f.write("Files:")
            if len(filename_str)>0:
                f.write("\n" + filename_str)
    print("Finished writing on <{}>".format(rc_fn))

def connect_directory( args ):
    source_dir = "." 
    dropbox_dir = dropbox 
    if len(args)>0 : 
        source_dir = args[0]
    if len(args)>1 : 
        dropbox_dir = args[1]
    my_source_dir = os.path.abspath(os.path.expanduser(source_dir))
    my_dropbox_dir = os.path.abspath(os.path.expanduser(dropbox_dir))
    connect_dict = read_rc()
    if my_source_dir not in connect_dict : 
        connect_dict[my_source_dir] = [ my_dropbox_dir, [ ] ]
        print("New connection {} -> {}".format(my_source_dir, my_dropbox_dir))
    else : 
        old_target = connect_dict[my_source_dir][0]
        if old_target == my_dropbox_dir:
            print("{} <-> {} already is connected. Doing nothing..".format(
                my_source_dir, old_target)) 
        else : 
            print("Updating {} <-> {} to {} <-> {}".format(
                my_source_dir, old_target, my_source_dir, my_dropbox_dir))
            connect_dict[my_source_dir][0] = my_dropbox_dir
    write_rc(connect_dict)


def check_if_connected(connect_dict, in_dir):
    dir_name = os.path.abspath(in_dir)
    if dir_name not in connect_dict : 
        print("{} is not connected. Execute dsync connect {} target_dir first.".format(dir_name, dir_name))
        return False
    else : 
        return True

            
def connect_files(args): 
    connect_dict = read_rc()
    cwd = os.path.abspath(".")
    if not check_if_connected(connect_dict, cwd):
        return False
    #if cwd not in connect_dict : 
        #print("{} is not connected. Execute dsync connect {} target_dir first.".format(cwd, cwd))
        #return False
    if len(args)==0:
        print("No filenames given. Doing nothing.")
        return False
    target_dir = connect_dict[cwd][0]
    in_fnames = args[:]
    candi_set = set().union(os.listdir(cwd), os.listdir(target_dir))
    filtered_fnames = [ ] 
    for in_fname in in_fnames : 
        if in_fname.startswith(os.sep): 
            fname = os.path.split(in_fname)[1]
        else : 
            fname = in_fname
        if fname not in candi_set:
            print("<{}> not found in {} or in {}. Ignoring it.".format(
                fname, cwd, target_dir))
        else : 
            filtered_fnames.append(fname)
    new_names = [ ] 
    old_names = connect_dict[cwd][1]
    #print(old_names)
    for fname in filtered_fnames: 
        if fname in old_names : 
            print("<{}> already has been connected. Doing nothing.".format(
                fname))
        else : 
            new_names.append(fname)
    if len(new_names)>0:
        print("Connecting {}.. on to {}".format(" ".join(new_names), 
            target_dir ))
        connect_dict[cwd][1].extend(new_names)
        #print(connect_dict)
        write_rc(connect_dict)

def h_readable( n ) :
    if n > 1000000 :
        return "{:.1f}M".format( n / 1000000.0 )
    elif n > 1000 :
        return "{:.1f}K".format( n / 1000.0 )
    else :
        return str(n)

def show_stat(full_fname, suffix=""): 
    print(h_readable(os.path.getsize(full_fname)), 
            time.ctime( os.path.getctime(full_fname) ), full_fname, suffix)
    
def check_files(args):
    if len(args)==0:
        in_dir = "."
    else : 
        in_dir = args[0]
    my_source_dir = os.path.abspath(os.path.expanduser(in_dir))
    connect_dict = read_rc()
    if not check_if_connected(connect_dict, my_source_dir):
        return False
    target_dir, fname_list  = connect_dict[my_source_dir]

    fname_classify_dict = { }
    
    for fname in fname_list : 
        full_fname = my_source_dir  + os.sep + fname
        full_target_fname = target_dir + os.sep + fname
        if os.path.exists( full_fname ) and \
              not os.path.exists( full_target_fname ):
            fname_classify_dict[fname] = 1
        elif not os.path.exists( full_fname ) and \
              os.path.exists( full_target_fname ):
            fname_classify_dict[fname] = 2
        elif os.path.exists( full_fname ) and \
              os.path.exists( full_target_fname ) and \
                filecmp.cmp( full_fname, full_target_fname ) :
            fname_classify_dict[fname] = 3
        else : 
            fname_classify_dict[fname] = 4

    fname_list.sort(key = lambda x: (fname_classify_dict[x], x))

    for fname in fname_list : 
        full_fname = my_source_dir  + os.sep + fname
        full_target_fname = target_dir + os.sep + fname

        if fname_classify_dict[fname] == 2: 
            print("You don't have <{}>.".format(fname))
        elif fname_classify_dict[fname] == 1: 
            print("No <{}> found in Dropbox".format( full_target_fname))
        elif fname_classify_dict[fname] == 3: 
            print("<{}> in the dropbox is up to date.".format(fname))
        else : 
            if os.path.exists( full_fname ) : 
                show_stat(full_fname)
                #print(h_readable(os.path.getsize(full_fname)), 
                #time.ctime( os.path.getctime(full_fname) ), full_fname)
            if os.path.exists( full_target_fname ) : 
                show_stat(full_target_fname, suffix = "in Dropbox")
                #print(h_readable(os.path.getsize(full_target_fname)), 
                #time.ctime( os.path.getctime(full_target_fname) ), 
                    #full_target_fname, "in Dropbox")

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
        if re.match( without_ext + r"-\d+" +  "\\" + ext, c) ]
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




def upload_files(args):
    if len(args)==0: in_dir = "."
    else : in_dir = args[0]
    my_source_dir = os.path.abspath(os.path.expanduser(in_dir))
    connect_dict = read_rc()
    if not check_if_connected(connect_dict, my_source_dir):
        return False
    target_dir, fname_list  = connect_dict[my_source_dir]
    for fname in fname_list : 
        full_fname = my_source_dir  + os.sep + fname
        full_target_fname = target_dir + os.sep + fname
        if not os.path.exists( full_fname ) : 
            continue
        if not os.path.exists( full_target_fname ) : 
            print("Copying <{}> from {} to {}.".format(fname, my_source_dir, 
                target_dir))
            shutil.copyfile( full_fname, full_target_fname )
            continue
        if os.path.exists( full_target_fname ) : 
            if filecmp.cmp( full_fname, full_target_fname ) :
                #print("<{}> in {} is up to date.".format(fname, target_dir))
                continue
            d = 'y'
            if os.path.getsize(full_fname) < os.path.getsize(full_target_fname)  or os.path.getctime(full_fname) < os.path.getctime(full_target_fname):
                show_stat(full_fname)
                show_stat(full_target_fname, "in Dropbox")
                d = input( "<{}> in Dropbox may be newer. Are you sure to replace it? (y/n) ".format( fname ))
            if d == 'y':
                leave_a_backup(full_target_fname)
                print("Copying <{}> from {} to {}.".format(fname, 
                    my_source_dir, target_dir))
                shutil.copyfile( full_fname, full_target_fname )


def download_files(args):
    if len(args)==0: in_dir = "."
    else : in_dir = args[0]
    my_local_dir = os.path.abspath(os.path.expanduser(in_dir))
    connect_dict = read_rc()
    if not check_if_connected(connect_dict, my_local_dir):
        return False
    cloud_dir, fname_list  = connect_dict[my_local_dir]
    for fname in fname_list : 
        full_fname = my_local_dir  + os.sep + fname
        full_cloud_fname = cloud_dir + os.sep + fname
        if not os.path.exists( full_cloud_fname ) : 
            continue
        if not os.path.exists( full_fname ) : 
            print("Copying <{}> from {} to {}.".format(fname, cloud_dir, 
                my_local_dir))
            shutil.copyfile( full_cloud_fname, full_fname )
            continue
        if os.path.exists( full_fname ) : 
            if filecmp.cmp( full_fname, full_cloud_fname ) :
                continue
            d = 'y'
            if os.path.getsize(full_fname) > os.path.getsize(full_cloud_fname)  or os.path.getctime(full_fname) > os.path.getctime(full_cloud_fname):
                show_stat(full_fname)
                show_stat(full_cloud_fname, "in Dropbox")
                d = input( "<{}> in Local may be newer. Are you sure to replace it? (y/n) ".format( fname ))
            if d == 'y':
                leave_a_backup(full_fname)
                print("Copying <{}> from {} to {}.".format(fname, 
                    cloud_dir, my_local_dir ))
                shutil.copyfile( full_cloud_fname, full_fname)




def print_help(args):
    print(
'''Syntax:
dsync command [arg1 arg2 .. ]
Example:
dsync help
dsync connect_directory [source_dir=. dropbox_dir=~/Dropbox/dsync_bin]
dsync connect file1 [file2 ..]
dsync upload 
dsync download''' 
)
    return True

'''
dsync disconnect_files file1 [file2 ..]
dsync connect_all_files
dsync disconnect_all_files
dsync check
dsync update
dsync update_files file1 [file2 ..]
dsync upload_files file1 [file2 ..]
dsync download_files file1 [file2 ..]
'''




command_func_dict = { 
    "help": print_help, 
    "connect_directory": connect_directory, 
    "connect": connect_files,
    "check": check_files,
    "upload": upload_files,
    "download": download_files
 }

if __name__ == "__main__" : 

    if len(sys.argv)<=1: 
        command = "help"
    else : 
        command = sys.argv[1]
    args = sys.argv[2:]

    if command in command_func_dict : 
        command_func_dict[command](args) 
    else : 
        print_help(args)


