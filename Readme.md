# Timogen Vue

Application pour générer des tickets modérateurs pour les kinésithérapeutes en Belgique.

Le projet est relativement fonctionnel, mais abandonné pour des raisons de temps, et de modifications des lois relatives à la déclaration des tickets.


## TODOs

First of the lists are priority

 - [ ] Report.
 - [ ] Accelerate dev-to-prod by removing unused stuffs in prod.
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
