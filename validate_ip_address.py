import re

"""One of the most important thing is how this regex has been written with OR cases everywhere, the other important thing is how I use a $ at the end to make sure that no truncate matches are invloved"""

def check_ips(text):
    ipv4 = re.compile(r'([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\.([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\.([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\.([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])$')
    ipv6 = re.compile(r'([\dabcdef]|[\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef][\dabcdef]):([\dabcdef]|[\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef][\dabcdef]):([\dabcdef]|[\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef][\dabcdef]):([\dabcdef]|[\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef][\dabcdef]):([\dabcdef]|[\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef][\dabcdef]):([\dabcdef]|[\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef][\dabcdef]):([\dabcdef]|[\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef][\dabcdef]):([\dabcdef]|[\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef]|[\dabcdef][\dabcdef][\dabcdef][\dabcdef])$')
        
    if (ipv4.search(text)):
            
        return "IPv4"
    elif(ipv6.search(text)):
        return "IPv6"
    else:
        return "Neither"
def main():
    num = input()
    for i in range(0, num):
        print check_ips(raw_input())
if __name__ == "__main__":
    main()
