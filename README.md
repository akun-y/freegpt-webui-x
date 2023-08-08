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

- [FreeGPT WebUI](#freegpt-webui)
  - [GPT 3.5/4](#gpt-354)
  - [Known bugs 🚧](#known-bugs-)
  - [News 📢](#news-)
  - [Note ℹ️](#note-ℹ️)
  - [Table of Contents](#table-of-contents)
  - [](#)
  - [To-Do List ✔️](#to-do-list-️)
  - [Getting Started :white\_check\_mark:](#getting-started-white_check_mark)
    - [Cloning the Repository :inbox\_tray:](#cloning-the-repository-inbox_tray)
    - [Install Dependencies :wrench:](#install-dependencies-wrench)
  - [Running the Application :rocket:](#running-the-application-rocket)
  - [Docker 🐳](#docker-)
    - [Prerequisites](#prerequisites)
    - [Running the Docker](#running-the-docker)
  - [Docker build](#docker-build)
  - [Incorporated Projects :busts\_in\_silhouette](#incorporated-projects-busts_in_silhouette)
    - [WebUI](#webui)
    - [API G4F](#api-g4f)

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
git clone https://github.com/akun-y/freegpt-webui-x.git
```

### Install Dependencies :wrench:

Navigate to the project directory:

```
cd freegpt-webui-x
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
docker pull yinghk/freegpt-webui-x
```

Run the application using Docker:

```
docker run -p 1338:1338 yinghk/freegpt-webui-x:v0.0.2
```
for macos m1:

```
docker run -p 1338:1338 --platform linux/amd64 -v /Users/yhk/.cache/gpt4all:/app/gpt4all -v ./config-macos.json:/app/config.json --name=iKonwMGPT yinghk/freegpt-webui-x:latest
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

## Docker build

1. docker build -t yinghk/freegpt-webui-x:v0.1.1 -t yinghk/freegpt-webui-x:latest .
2. docker login
3. docker push yinghk/freegpt-webui-x

```
docker-compose -f docker-compose-image.yml up -d
```

## Incorporated Projects :busts_in_silhouette

I highly recommend visiting and supporting both projects.

### WebUI

The application interface was incorporated from the [chatgpt-clone](https://github.com/xtekky/chatgpt-clone) repository.

### API G4F

The free GPT-4 API was incorporated from the [GPT4Free](https://github.com/xtekky/gpt4free) repository.
