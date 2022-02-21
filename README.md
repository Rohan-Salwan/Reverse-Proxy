# Reverse Proxy
I implemented reverse proxy server which forwards user/web browser requests to web servers. However, the reverse proxy server protects the web server’s identity. This type of proxy server also moves requests strategically on behalf of web servers, typically to balance the load. Moreover, enhance network performance via caching by storing static content and also provide a security abstraction layer.

Reverse Proxy Servers can:

* Disguise the characteristics and existence of origin servers.
Make initiating takedowns and removing malware easier.

* Distribute load from incoming requests to each of several servers that supports its own application area.

* Function as web acceleration servers, caching dynamic content and static content, reducing load on origin servers.

* “Spoon-feed” dynamically generated pages bit by bit to clients even when they are produced at once, allowing the pages and the program that generates them to be closed, releasing server resources during the transfer time.

* Analyze many incoming requests via a single public IP address, delivering them to multiple web-servers within the local area network.

Installing
----------

Use Clone Command To Install Reverse-Proxy:

    $ git clone https://github.com/Rohan-Salwan/Reverse-Proxy.git

For Installing Dependencies:

    $ pip install -r requirements.txt

Contribution
------------

Firstly Activate Environment:

    $ source Env/bin/activate

Secondly Install Dependencies:

    $ pip install -r requirements.txt

Always Run Tests:

    $ pytest Test_Cache.py
    $ pytest Test_LoadBalancer.py
    $ pytest Test_Security.py
    $ pytest Test_Utility.py

