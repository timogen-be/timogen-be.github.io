rm -r timogen/__pycache__
rm -r timogen/migrate
python manage.py makemigrations timogen
python manage.py migrate timogen
python manage.py loaddata timogen/data/nomenclature_data.json
