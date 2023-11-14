import whois as ws

class Whois:
    def print_whois(self, host):
        """
        host: Host that you are researching
        """
        whois_result = ws.whois(host)
        print(whois_result)

if __name__ == "__main__":
    whois = Whois()
    whois.print_whois("zahariromanov.com")
