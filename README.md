##  **Getting Set Up**
#### Ensure Python 3.5+ is downloaded
 The [Stacks Documentation](https://subinitial.com/misc/doc/index.html) states that the Python 3 version must be version 3.6+, but previous versions have worked

Run in terminal
``` python --version ```

* If Python is not downloaded, install using apt
```
sudo apt install python3
```


* Or download from [here](https://www.python.org/downloads/)

Additional packages needed for install
 - Git
   - Linux (Debian/Ubuntu),  ``` sudo apt install git ```
   - Windows, Download from [here](https://git-scm.com/download/win)

 - Subinitial Stacks Library ``` pip3 install --user git+https://bitbucket.org/subinitial/subinitial.git ```

## **Connecting to the Stacks Core**
 - The default Stacks IP address is 192.168.1.49, but currently the IP address is 192.168.2.49 (the IP address can be changed ) 
 - Set the IP address on your machine to any 192.168.2.xxx IP address manually with netmask or (255.255.255.0)
 - To change the IP address of the Stacks refer to [here](https://www.subinitial.com/misc/pub/SD00170_Stacks_Connectivity_Troubleshooting_Guide.pdf)
 - Ping the IP address of the Stacks to ensure connectivity

``` 
ping 192.168.2.49
```

> Documentation created by [johnnysedor](https://github.com/johnnysedor)
