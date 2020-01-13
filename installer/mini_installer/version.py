import argparse
import yaml
import sys
from mini_installer import copy_file
import os


def check_version(cfg):
    copy_file.createFolder("pkg/main_app")
    if "VERSION.txt" in os.listdir("pkg/main_app"):
        file = open("pkg/main_app/VERSION.txt", "r+")
        print(file.read())
        file.truncate(0)
        file.write(cfg["version"])
        file.close()

    else:
        file = open("pkg/main_app/VERSION.txt", "w")
        file.write(cfg["version"])
        file.close()


def replace_version(var_1, var_2, file):
    fileBuffer = list()

    with open(file, "r")as fin:
        for line in fin:
            fileBuffer.append(line)
        fin.close()
    with open(file, "w") as fout:
        for line in fileBuffer:
            fout.write(line.replace(var_1, var_2))
        fout.close()


def replace_version_from_cmd(vars):
    l_buffer = vars.split(" ")
    versions = {}
    for i in l_buffer:
        l_buffer2 = i.split("=")
        versions.update({l_buffer2[0]: l_buffer2[1]})


    for k, v in versions.items():
        replace_version(k, v, "rep_file.txt")


