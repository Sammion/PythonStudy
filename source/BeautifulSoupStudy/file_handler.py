# -*- coding: utf-8 -*-
"""
Created on 2018/6/12

@author: Samuel
@Desc: 
@dependence: Noting
"""


def read_urls(file_input, mid="="):
    res_url = dict()
    with open(file_input, 'r', encoding="UTF-8") as fr:
        lines = fr.readlines()
        for line in lines:
            if line[0] == '#':
                print("Skip line:" + line)
                continue

            name = line.split(mid)[0].strip()
            url = line.split(mid)[1].strip()
            res_url[name] = url
    return res_url


# Return a list of agents which configured in the config file.
def get_agents(agents_file='config/agents.lis'):
    agents = list()
    with open(agents_file) as fr:
        agents = fr.readlines()
        fr.close()
    return agents


# Write ip&port to file
def record_ips(path, text):
    with open(path, 'a', encoding='utf-8') as f:
        f.writelines(text)
        f.write('\n')
        f.close()


# Read IP and port from file
def read_ips(path):
    with open(path, 'r', encoding='utf-8') as f:
        txt = []
        for s in f.readlines():
            txt.append(s.strip())
    return txt


# Truncate file
def truncate_file(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.truncate()
        f.close()

