# 03_dig_info.py

import pydig as pd

class DigInfo:
    def print_dig_info(self, host, type):
        """
        
            host: Host to dig
            type: Can be A, NS, CNAME, etc

        """

        dig_info = pd.query(host, type)
        print(dig_info)

if __name__ == "__main__":
    dig_info = DigInfo()
    # Print Record
    dig_info.print_dig_info("zahariromanov.com", "A")
    dig_info.print_dig_info("zahariromanov.com", "NS")
    dig_info.print_dig_info("zahariromanov.com", "CNAME")
    dig_info.print_dig_info("zahariromanov.com", "MX")
    dig_info.print_dig_info("zahariromanov.com", "TXT")