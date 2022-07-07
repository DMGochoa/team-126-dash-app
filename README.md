This web app is part of the deliverables of the final project of the team 126
at the Data Science for All program from Correlation One. It features different
tools to explore Bogotá's localities as a tourist. The web app is accessible through the url
https://explora-bogota.herokuapp.com/

### How to run the app locally

1. Go inside the environment with `source venv/bin/activate`
2. Install requirements with `pip install -r requirements.txt --user`
3. Run the main file with `python app.py`
4. Open the URL `localhost:8050` in a web browser to see the result

### Screenshots

<img width="1552" alt="image" src="https://user-images.githubusercontent.com/36432023/177794269-2fbfdf95-9419-4a1d-8c8b-e422fccfe600.png">
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/36432023/177794318-6892b1c9-334a-4f56-b774-e36fd5088658.png">
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/36432023/177794420-b58ac21c-7602-4ceb-bb2f-acf2f885473e.png">

![screencapture-127-0-0-1-8050-delincuencia-2022-07-07-09_10_57](https://user-images.githubusercontent.com/36432023/177794631-33aec4ba-ba77-4f31-b176-9308b9df3296.png)

![screencapture-127-0-0-1-8050-sobre-nosotros-2022-07-07-09_11_51](https://user-images.githubusercontent.com/36432023/177794768-07c98a94-1849-4d3a-8284-530810670349.png)

### Features

On each page we display different views that can be used to explore Bogotá
or know more about the city, our pages are:

* Home page: explore the map of Bogotá and filter by locality in order to
see key points such as hotels, touristic attractions, wifi hotspots, public
transport and malls.
* Tu perfil: a set of 15 questions will tell you more about your tourist
profile and give you useful recommendations that you can try on your next visit!
* Delitos: know more about the crime profile of Bogotá by locality or time of day
* Sobre nosotros: know more about the people that made this app possible, team 126
and information sources.

### Architecture

We have two data folders, `data` and `data-cleaned` which contain the
raw information that will be exported and consumed in our application
mainly on the `app.py` file.

<img width="1147" alt="image" src="https://user-images.githubusercontent.com/36432023/177792413-a9cb3f2f-1111-4dea-b6a9-64e148bdb14a.png">

Our `app.py` file is the heart of the application, it has the majority of
the callbacks supported and is a place where we import our components and
pages to add interactivity and states.

Additionally, we have the `/pages` and `/components` folders which are
responsible for hosting the re-usable components and main pages of the app.

Finally, we also have an `/assets` folder that hosts any image or styles.


