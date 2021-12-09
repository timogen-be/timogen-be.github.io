# Timogen Vue

I really need to learn a frontend framework, and I think it will be Vue.js.
Based on this video: [Django Vue Tutorial: Django REST Framework + VUE.js | Django REST framework tutorial](https://www.youtube.com/watch?v=7GWKv03Osek)
Also, I think that separating the backend classes will make it easier.

## Dev Steps

_The main advantage is that these steps do not require to be achieved in a specific order._

1. Therapist API endpoint
 - [x] Therapist class.
 - [x] Scrapping to find all the Therapists. (inami + BCE)
 - [x] Script for Populate/Update db with scrap results.
 - [ ] Improve the API (->list of kine for a searchbar + search by ID)
 - [ ] Add BCE (low priority)

2. Timogen API endpoint
 - [ ] Timogen class.
 - [ ] Create the pdf with django when receiving the data.

3. Nomenclature code
 - [ ] Nomenclature class.
 - [ ] Scrapping to find the last file.
 - [ ] Parsing the file.
 - [ ] Populate/update (create a json file).

4. Vue side
 - [ ] Create the Vue.js App with fields that we will fill thanks to the django app.

5. Backend
 - [ ] Add translations through `.po` files.


## Launch the django App

```bash
python3 -m pip install django
cd backend
./manage.py migrate
./manage.py loaddata therapists_data.json
./manage.py runserver
```

## Launch the Vue App

```bash
npm install --global @vue/cli
cd frontend
npm run serve
```

## calendar to use

https://vcalendar.io/examples/datepickers.html
