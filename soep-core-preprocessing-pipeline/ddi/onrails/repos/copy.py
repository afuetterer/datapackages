import os
import shutil

def f(filename, target = None):
    if not target:
        target = filename
    os.system("cp metadata/%s ddionrails/%s" % (filename, target))

def study(inpath, outpath):
    """ Copy the study description from inpath to outpath """
    shutil.copy(inpath, outpath)

def bibtex(inpath, outpath, input_format="latin1"):
    if input_format == "utf8":
        shutil.copy(inpath, outpath)
    elif input_format == "latin1":
        shutil.copy(inpath, outpath)
        #os.system("recode l1..utf8 ddionrails/bibtex.bib")
    else:
        raise Exception("Invalid input_format")

def r2ddi(in_path, out_path):
    os.system("""
        rm -r ddionrails/r2ddi
        mkdir -p ddionrails/r2ddi/
        cp -r %s %s
    """ % (in_path, out_path))
