import yaml
import sys
import re
from mini_installer import version
from mini_installer import copy_file

def read_yml(file):
    with open(file, 'r') as stream:
        cfg = yaml.load(stream)
        version.check_version(cfg)
        call_copy(cfg)


def call_copy(cfg):
    if ("version" in cfg.keys()):
        print("version information:\n", cfg["version"])
        answer = input("\nwould you like to continue?\nYES/NO\n")

    if (answer.upper() == "YES"):
        print("Installation is started..")

        for x in cfg["copy"]["others"]["files"]: #copied files in others
            print(x["name"])
            path = x["dst"].split("/")
            if (re.search("^[$]{", path[0])):
                x["dst"] = cfg["copy"]["main_dir"]["src"] + "/" + x["dst"].split("/")[1]
                with open('installation.yaml', 'w') as f:
                    yaml.dump(cfg, f, default_flow_style=False)

            copy_file.createFolder(x["src"])
            copy_file.createFolder(x["dst"])
            copy_file.copyAll(x["src"], x["dst"], False, None)

        for x in cfg["copy"]["others"]["dirs"]:
            copy_file.createFolder(x["src"])
            copy_file.createFolder(x["dst"])
            copy_file.copyAll(x["src"], x["dst"], False, None)

        for x in cfg["exec"]["pre"]:  #showed commands in exec pre
            print(x)

        src = cfg["copy"]["main_dir"]["src"]  #copied files in main_dir
        dst = cfg["copy"]["main_dir"]["dst"]
        copy_file.createFolder(src)
        copy_file.createFolder(dst)
        copy_file.copyAll(src, dst, False, None)

        print("Installation is completed.")  #showed commands in exec post
        for x in cfg["exec"]["post"]:
            print(x)

        for x in cfg["variables"]:#to define an unspecified path
            for key in x.keys():
                result = x["filename"].split("/")
                if (re.search("^[$]{", result[0])):
                    x["filename"] = cfg["copy"]["main_dir"]["src"] + "/" + x["filename"].split("/")[1]
                    with open('installation.yaml', 'w') as f:
                        yaml.dump(cfg, f, default_flow_style=False)
