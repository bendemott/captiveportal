**About**:

    A captive portal is a bit of software trickery that captures network requests going over
    a device and redirects those requests to a special web-page where you ask for something
    from your users.  Places like Mcdonalds, Starbucks and Panera use captive portals.
    Most often a captive portal just requires you to agree to some terms and conditions
    before it lets you continue browsing the internet.
    
    I created this captive portal to use with a Raspberry PI acting as an access point.
    I used the portal to test portal-discovery on several mobile-devices and applications.
    You can see my other repository "raspberryap" for information on how to configure
    a raspberry pi as an access point.
    
    
    This captive portal still needs some work.  It doesn't properly handle HTTPS redirection,
    and it also proxies all allowed traffic, which it should just change the routing rules to
    allow or disallow a list of clients based on hardware address.  I'll fix that in the future.
    
Notice:

    The captive portal issues iptables commands that add rules. These commands are reversed/removed
    when the captive portal is stopped using the ``sudo captiveportal stop`` command.
    
    The captive portal limits the redirection to a single interface, by default wlan0.

Installation::

    1.) Download and unzip, or clone this repository
    2.) Ensure you're in the directory containing the setup.py file
    3.) In a command prompt type: sudo python setup.py install

To manually install the captive portal (`if setup.py doesn't work`)::

    1.) Copy "captiveportal" to /usr/bin/captiveportal
    2.) chmod 755 /usr/bin/captiveportal
    3.) sudo apt-get install python-twisted python-twisted-web
    
Using the captive portal:

    First you may have strange behavior if the tablet is connected to a server not 
    listening on port 80.  The portal works BEST when all requests are heading through
    port 80.
        
    run ``sudo captiveportal start`` to start the portal.
    
    run ``sudo captiveportal stop`` to stop the portal.
    
    run ``sudo captiveportal start --help`` for configuration options.
    
    to reset which addresses are allowed: ``sudo captiveportal reset``
    
**Note:**

    Sometimes there is a delay in the portal working because of already-active http connections
    that will wait to be re-used.  The captive portal attempts to issue a command to reset these
    connections but there may be times when you have to simply wait until your device closes all
    open http connections before the portal will start working.
