import whois as ws

class Whois:
    def print_whois(self, host):
        
        """
            host: Host that you are researching
        """
        whois = ws.whois(host)

if __name__ == "__main__":
    whois = Whois()
    whois.print_whois("zahariromanov.com")