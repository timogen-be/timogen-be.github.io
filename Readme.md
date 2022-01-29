# Timogen Vue

## TODOs

First of the lists are priority

 - [ ] Report.
 - [ ] HomePage.
 - [ ] BCE Link.
 - [ ] Validation Error.
 - [ ] Mutuality Choice.
 - [ ] Video.
 - [ ] Scrapping to find the last file.
    > Références:
    > (https://www.webkine.be/blog/actualites-membres-2/post/nomenclature-de-kinesitherapie-adaptations-au-1er-juin-2021-3673)
 - [ ] Add translations through `.po` files (or else).
 - [ ] Add BCE (low priority).
 - [ ] Add access to further options.

To determine

 - [ ] Googleize.
 - [ ] Monetize.


## KNOWN BUGS (to fix)

 - [ ] not the same order for locations in prod/dev


## Launch

_Backend_
```bash
python3 -m pip install django
cd backend
./manage.py migrate
./manage.py loaddata therapists_data.json
./manage.py runserver
```

_Frontend_
```bash
npm install --global @vue/cli
cd frontend
npm run serve
```
