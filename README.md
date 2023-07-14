# FreeGPT WebUI 
## GPT 3.5/4

<strong>NOT REQUIRE ANY API KEY</strong> ❌🔑 

This project features a WebUI utilizing the [G4F API](https://github.com/xtekky/gpt4free). <br>
Experience the power of ChatGPT with a user-friendly interface, enhanced jailbreaks, and completely free.

## Known bugs 🚧
- GPT-4 model offline.

## News 📢
I have created a new version of FreeGPT WebUI using the [ChimeraGPT API](https://chimeragpt.adventblocks.cc/). 
<br>
<br>
This free API allows you to use various AI chat models, including <strong>GPT-4, GPT-4-32k, Claude-2, Claude-2-100k, and more.</strong> <br>
Check out the project here: [FreeGPT WebUI - Chimera Version](https://github.com/ramonvc/freegpt-webui/tree/chimeragpt-version).

## Note ℹ️ 
<p>
  FreeGPT is a project that utilizes various free AI conversation API Providers. Each Provider is an API that provides responses generated by different AI models. The source code related to these services is available in <a href="https://github.com/ramonvc/freegpt-webui/tree/main/g4f">G4F folder</a>.

It is important to note that, due to the extensive reach of this project, the free services registered here may receive a significant number of requests, which can result in temporary unavailability or access limitations. Therefore, it is common to encounter these services being offline or unstable.

We recommend that you search for your own Providers and add them to your personal projects to avoid service instability and unavailability. Within the project, in the <a href="https://github.com/ramonvc/freegpt-webui/tree/main/g4f/Provider/Providers">Providers folder</a>, you will find several examples of Providers that have worked in the past or are still functioning. It is easy to follow the logic of these examples to find free GPT services and incorporate the requests into your specific FreeGPT project.

Please note that the choice and integration of additional Providers are the user's responsibility and are not directly related to the FreeGPT project, as the project serves as an example of how to combine the <a href="https://github.com/xtekky/gpt4free">G4F API</a> with a web interface.
</p>

## Table of Contents  
- [To-Do List](#to-do-list-%EF%B8%8F)  
- [Getting Started](#getting-started-white_check_mark)  
  - [Cloning the Repository](#cloning-the-repository-inbox_tray)  
  - [Install Dependencies](#install-dependencies-wrench)  
- [Running the Application](#running-the-application-rocket)  
- [Docker](#docker-)  
  - [Prerequisites](#prerequisites)  
  - [Running the Docker](#running-the-docker)
- [Incorporated Projects](#incorporated-projects-busts_in_silhouette)
  - [WebUI](#webui) 
  - [API FreeGPT](#api-g4f)
- [Star History](#star-history)
- [Legal Notice](#legal-notice) 

##

## To-Do List ✔️

- [x] Integrate the free GPT API into the WebUI
- [x] Create Docker support
- [x] Improve the Jailbreak functionality
- [x] Add the GPT-4 model
- [x] Enhance the user interface
- [ ] Check status of API Providers (online/offline)
- [ ] Enable editing and creating Jailbreaks/Roles in the WebUI
- [ ] Refactor web client

## Getting Started :white_check_mark:  
To get started with this project, you'll need to clone the repository and have [Python](https://www.python.org/downloads/) installed on your system.  
  
### Cloning the Repository :inbox_tray:
Run the following command to clone the repository:  

```
git clone https://github.com/akun-y/freegpt-webui.git
```

### Install Dependencies :wrench: 
Navigate to the project directory:
```
cd freegpt-webui
```

Install the dependencies:
```
pip install -r requirements.txt
```
## Running the Application :rocket:
To run the application, run the following command:
```
python run.py
```

Access the application in your browser using the URL:
```
http://127.0.0.1:1338
```
or
```
http://localhost:1338
```


## Docker 🐳
### Prerequisites
Before you start, make sure you have installed [Docker](https://www.docker.com/get-started) on your machine.

### Running the Docker
Pull the Docker image from Docker Hub:
```
docker pull ramonvc/freegpt-webui
```

Run the application using Docker:
```
docker run -p 1338:1338 yinghk/freegpt-webui-x:v0.0.2
```

Access the application in your browser using the URL:
```
http://127.0.0.1:1338
```
or
```
http://localhost:1338
```

When you're done using the application, stop the Docker containers using the following command:
```
docker stop <container-id>
```

## Incorporated Projects :busts_in_silhouette:
I highly recommend visiting and supporting both projects.

### WebUI
The application interface was incorporated from the [chatgpt-clone](https://github.com/xtekky/chatgpt-clone) repository.

### API G4F
The free GPT-4 API was incorporated from the [GPT4Free](https://github.com/xtekky/gpt4free) repository.

<br>

## Star History
[![Star History Chart](https://api.star-history.com/svg?repos=ramonvc/freegpt-webui&type=Timeline)](https://star-history.com/#ramonvc/freegpt-webui&Timeline)

<br>

## Legal Notice
This repository is _not_ associated with or endorsed by providers of the APIs contained in this GitHub repository. This
project is intended **for educational purposes only**. This is just a little personal project. Sites may contact me to
improve their security or request the removal of their site from this repository.

Please note the following:

1. **Disclaimer**: The APIs, services, and trademarks mentioned in this repository belong to their respective owners.
   This project is _not_ claiming any right over them nor is it affiliated with or endorsed by any of the providers
   mentioned.

2. **Responsibility**: The author of this repository is _not_ responsible for any consequences, damages, or losses
   arising from the use or misuse of this repository or the content provided by the third-party APIs. Users are solely
   responsible for their actions and any repercussions that may follow. We strongly recommend the users to follow the
   TOS of the each Website.

3. **Educational Purposes Only**: This repository and its content are provided strictly for educational purposes. By
   using the information and code provided, users acknowledge that they are using the APIs and models at their own risk
   and agree to comply with any applicable laws and regulations.

4. **Copyright**: All content in this repository, including but not limited to code, images, and documentation, is the
   intellectual property of the repository author, unless otherwise stated. Unauthorized copying, distribution, or use
   of any content in this repository is strictly prohibited without the express written consent of the repository
   author.

5. **Indemnification**: Users agree to indemnify, defend, and hold harmless the author of this repository from and
   against any and all claims, liabilities, damages, losses, or expenses, including legal fees and costs, arising out of
   or in any way connected with their use or misuse of this repository, its content, or related third-party APIs.

6. **Updates and Changes**: The author reserves the right to modify, update, or remove any content, information, or
   features in this repository at any time without prior notice. Users are responsible for regularly reviewing the
   content and any changes made to this repository.

By using this repository or any code related to it, you agree to these terms. The author is not responsible for any
copies, forks, or reuploads made by other users. This is the author's only account and repository. To prevent
impersonation or irresponsible actions, you may comply with the GNU GPL license this Repository uses.
