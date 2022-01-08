# Therapist

This app contains the API to request information about Therapists.

## Overview

### Fields
 - activity
 - name
 - inami_nb
 - bank_account
 - bce
 - address
 - contracted

### Endpoints

`/api/therapists/`

_query parameter_ therapists= :
> give parts of name separated with spaces, and get the names containing these parts.

`/api/therapists/`

## Populate

The popultate folder contains a script to create the `.json` file 
(_populate.py_), and the _scrap.py_ is a script to retrieve data from the INAMI
website.

```bash
>backend/therapist/populate$ python scrap.py  # get the latest data
>backend/therapist/populate$ python populate.py  # re-create the json file
```

Then with the _manage.py_, we can update the data:

```bash
>backend$ python manage.py loaddata therapist/populate/therapists_data.json
```
