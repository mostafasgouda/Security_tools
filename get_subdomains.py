#write a function that get all subdomains from a domain
#using serfing the web to get all subdomains
#using requests to get all subdomains
#using socket to get all subdomains
#using dns to get all subdomains
#using crt.sh to get all subdomains
#using sublist3r to get all subdomains
#using assetfinder to get all subdomains
#using amass to get all subdomains
#using findomain to get all subdomains
#using subfinder to get all subdomains
#using knockpy to get all subdomains
#using sublister to get all subdomains
#using subbrute to get all subdomains
#using aquatone to get all subdomains
#using subzy to get all subdomains
#using subjack to get all subdomains
#using subover to get all subdomains
#using subscan to get all subdomains
#using sublert to get all subdomains
#using subrecon to get all subdomains
#using subdomainizer to get all subdomains
#using subdomainer to get all subdomains
#using subdomainfinder to get all subdomains    
#write the code now
import requests
import socket
import dns.resolver
import os
import sys
import json
import argparse
import subprocess
import re
import time
import urllib.parse
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_subdomains(domain):
    subdomains = []
    subdomains += get_subdomains_from_crtsh(domain)
    subdomains += get_subdomains_from_sublist3r(domain)
    subdomains += get_subdomains_from_assetfinder(domain)
    subdomains += get_subdomains_from_amass(domain)
    subdomains += get_subdomains_from_findomain(domain)
    subdomains += get_subdomains_from_subfinder(domain)
    subdomains += get_subdomains_from_knockpy(domain)
    subdomains += get_subdomains_from_sublister(domain)
    subdomains += get_subdomains_from_subbrute(domain)
    subdomains += get_subdomains_from_aquatone(domain)
    subdomains += get_subdomains_from_subzy(domain)
    subdomains += get_subdomains_from_subjack(domain)
    subdomains += get_subdomains_from_subover(domain)
    subdomains += get_subdomains_from_subscan(domain)
    subdomains += get_subdomains_from_sublert(domain)
    subdomains += get_subdomains_from_subrecon(domain)
    subdomains += get_subdomains_from_subdomainizer(domain)
    subdomains += get_subdomains_from_subdomainer(domain)
    subdomains += get_subdomains_from_subdomainfinder(domain)
    return list(set(subdomains))

def get_subdomains_from_crtsh(domain):
    
    subdomains = []
    try:
        url = 'https://crt.sh/?q=%25.' + domain
        response = requests.get(url, verify=False)
        content = response.content.decode('utf-8')
        subdomains = re.findall(r'(?<=<TD>)([a-zA-Z0-9.*-]+\.%s)(?=</TD>)' % domain.replace('.', '\.'), content)
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_sublist3r(domain):
    subdomains = []
    try:
        command = 'sublist3r -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_assetfinder(domain):
    subdomains = []
    try:
        command = 'assetfinder --subs-only %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_amass(domain):
    subdomains = []
    try:
        command = 'amass enum -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains


def get_subdomains_from_findomain(domain):
    subdomains = []
    try:
        command = 'findomain -t %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_subfinder(domain):
    subdomains = []
    try:
        command = 'subfinder -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_knockpy(domain):
    subdomains = []
    try:
        command = 'knockpy %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_sublister(domain):
    subdomains = []
    try:
        command = 'sublister -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_subbrute(domain):
    subdomains = []
    try:
        command = 'subbrute.py %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_aquatone(domain):
    subdomains = []
    try:
        command = 'aquatone-discover -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_subzy(domain):
    subdomains = []
    try:
        command = 'subzy -hide -targets %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_subjack(domain):
    subdomains = []
    try:
        command = 'subjack -w %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_subover(domain):
    subdomains = []
    try:
        command = 'subover -l %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_subscan(domain):
    subdomains = []
    try:
        command = 'subscan -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_sublert(domain):
    subdomains = []
    try:
        command = 'sublert -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_subrecon(domain):
    subdomains = []
    try:
        command = 'subrecon -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_subdomainizer(domain):
    subdomains = []
    try:
        command = 'subdomainizer -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_subdomainer(domain):
    subdomains = []
    try:
        command = 'subdomainer -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_subdomainfinder(domain):
    subdomains = []
    try:
        command = 'subdomainfinder -d %s' % domain
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        subdomains = output.decode('utf-8').split()
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_dns(domain):
    subdomains = []
    try:
        answers = dns.resolver.resolve(domain, 'A')
        subdomains = [answer.address for answer in answers]
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_socket(domain):
    subdomains = []
    try:
        subdomains = socket.gethostbyname_ex(domain)
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_requests(domain):
    subdomains = []
    try:
        response = requests.get('http://' + domain)
        content = response.content.decode('utf-8')
        subdomains = re.findall(r'(?<=<a href="http://)(.*?)"', content)
    except Exception as e:
        pass
    return subdomains

def get_subdomains_from_serfing_the_web(domain):
    subdomains = []
    try:
        response = requests.get('http://' + domain)
        content = response.content.decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        for a in soup.find_all('a', href=True):
            subdomains.append(a['href'])
    except Exception as e:
        pass
    return subdomains

def main():
    parser = argparse.ArgumentParser(description='Get all subdomains from a domain')
    parser.add_argument('domain', help='The domain')
    args = parser.parse_args()
    domain = args.domain
    subdomains = get_subdomains(domain)
    for subdomain in subdomains:
        print(subdomain)

if __name__ == '__main__':
    main()
#run the code now
#python start.py example.com
#output
#subdomain1.example.com
#subdomain2.example.com
#subdomain3.example.com
#subdomain4.example.com
#subdomain5.example.com
#subdomain6.example.com
#subdomain7.example.com
#subdomain8.example.com


