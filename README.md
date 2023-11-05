---

## SECTION 1 : PROJECT TITLE
## ISS Project – AI Image Detection
---

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT


---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-------------------------| :-----|
| Wee De Li, Darren | A0269370X | | e1112241@u.nus.edu |
| Seow Teck Han, Michael | A0270178B | Cloud Architect and Systems Integrator | e1117140@u.nus.edu |
| Sankalp | A0226756W | | sankalp@u.nus.edu |
| Kelvin | A0269365N | Report Writing, Video Editor | e1112236@u.nus.edu |

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO
[![ISS Project – AI Image Detection](https://img.youtube.com/vi/UKxGmrfKkME/0.jpg)](https://youtu.be/UKxGmrfKkME "PRS-PM-2023-ISY5002 ISS Project – AI Image Detection")

---

## SECTION 5 : USER GUIDE
## Installation Instructions 

<ins>System Requirements</ins>
1) At least 4GB of RAM 
2) Internet connection 
3) Docker and Docker Compose to be installed on the system 

<ins>Installation Procedure</ins>
1) Install Docker and Docker Compose, if not yet installed. 
2) git clone the git repository (https://github.com/sink257/PRS-PM-2023-ISY5002.git) to a folder. 
3) Navigate into the SystemCode folder.
4) `chmod +x 00_buildFE.sh` and `chmod +x 01_buildBE.sh` to allow execution permissions of the build scripts. 
5) `./00_buildFE.sh` to build the frontend image and wait until it completes. 
6) `./01_buildBE.sh` to build the backend image and wait until it completes. 
7) `docker compose up -d` to start both the backend and frontend containers. 

After running the above steps, the website should be able to be viewed by accessing the browser and keying in the following address: http://<IP address>/ 

To stop the containers, navigate to the SystemCode folder and run the command: 
`docker compose down`

Note: The frontend website is hosted on port 80 and the backend API is hosted on port 8000. 

 

<ins>Troubleshooting</ins>  
Issue: After uploading of image and pressing continue, the prediction result does not show but just stays stuck with a black loading bar.  
Possible Cause: The backend API is not responding to the request, either due to a crash or some other error.  
Resolution: Check that the backend container is still running and not exited, by typing `docker ps`. If needed, restart the container by navigating to SystemCode folder and typing `docker compose up -d`. 
 

Issue: Image upload fails with a message saying the website has exceeded its free Bytescale limit.  
Possible Cause: Bytescale image upload service has hit the free API usage limit.  
Resolution: Create a Bytescale account and attach an API key by saving the following line NEXT_PUBLIC_UPLOAD_API_KEY="<API_KEY>" into a file named `.env` and place it into the frontend folder.  

---
## SECTION 6 : PROJECT REPORT / PAPER

The project report could be found in the ProjectReport folder in this repository. 


