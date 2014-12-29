To install the captive portal::

    1.) Copy "captiveportal" to /usr/bin/captiveportal
    2.) chmod 755 /usr/bin/captiveportal
    3.) sudo apt-get install python-twisted python-twisted-web
    
Using the captive portal:

    # First you may have strange behavior if the tablet is connected to a server not 
        listening on port 80.  The portal works BEST when all requests are heading through
        port 80.
        
    # run ``sudo captiveportal start``
    
    # to reset which addresses are allowed: `sudo captiveportal reset``
    
**Note:**

    Sometimes there is a delay because of ARP caching in denying requests.  It's best to
    restart the application with it using port 80 before you begin your tests.
