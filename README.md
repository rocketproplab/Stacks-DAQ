1.  **Getting Set Up**
    1.  Ensure Python 3.5+ is downloaded
        *   The [Stacks Documentation](https://subinitial.com/misc/doc/index.html) states that the Python 3 version must be version 3.6+, but previous versions have worked
        
        *   Run in terminal

            ``` python --version ```

        *   If Python is not downloaded, install using apt

            ``` sudo apt install python3 ```


        *   Or download from [here](https://www.python.org/downloads/)
    2.  Additional packages needed for install
        *   Git
            *   Linux (Debian/Ubuntu)

                ```
                sudo apt install git
                ```


            *   Windows

                Download from [here](https://git-scm.com/download/win)

        *   Ensure the Stacks python library is installed
            *   Inside a python shell

                ```python
                >>> import subinitial.stacks as stacks
                >>> print("Stacks Version:", stacks.VERSION_STACKS[0])
                Stacks Version: 1
                ```


            *   If not installed, install using pip3

                ```
                pip3 install --user git+https://bitbucket.org/subinitial/subinitial.git
                ```
