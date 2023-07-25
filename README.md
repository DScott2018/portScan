This port scanner is a simple Python script that uses the 'socket' module. This allows you to work with sockets and perform network operations.

If you were to plug and play using this script, you would be asked to input a domain name or an IP address as your target host to scan. 
Since the script has no hard coded target, you can input whatever target destination you like.

The output of this script will be "Scanning..." as the script runs through every port in the designated range (1-1024), but this can be changed very easily to fit whatever range necessary.
After the script has scanned every port, it will return a list of open ports. This can also be changed, with some modification, to show all closed ports as well.
