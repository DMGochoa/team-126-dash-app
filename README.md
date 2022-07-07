This web app is part of the deliverables of the final project of the team 126
at the Data Science for All program from Correlation One. It features different
tools to explore Bogotá's localities as a tourist.

### How to run the app locally

1. Go inside the environment with `source venv/bin/activate`
2. Install requirements with `pip install -r requirements.txt --user`
3. Run the main file with `python app.py`
4. Open the URL `localhost:8050` in a web browser to see the result

### Screenshots

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

Our `app.py` file is the heart of the application, it has the majority of
the callbacks supported and is a place where we import our components and
pages to add interactivity and states.

Additionally, we have the `/pages` and `/components` folders which are
responsible for hosting the re-usable components and main pages of the app.

Finally, we also have an `/assets` folder that hosts any image or styles.


