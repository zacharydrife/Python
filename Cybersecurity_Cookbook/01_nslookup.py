import socket

class NetworkUtilities:
    def nslookup(self, domain):
        """
        Find the IP Address for a domain using socket.
        Args:
            domain (string): Domain that you want to find the IP Addr.
        """
        nslookup_result_ip = socket.gethostbyname(domain)
        print(nslookup_result_ip)

    @staticmethod
    def test() -> None:
        network_utilities = NetworkUtilities()
        network_utilities.nslookup("zahariromanov.com")

# Create an instance of NetworkUtilities and call the test method
NetworkUtilities.test()
