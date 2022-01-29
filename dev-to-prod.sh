#!/bin/sh

BASENAME=${0%/*}  # /path/to

PROD_BACK="$BASENAME/prod/backend"
DEV_BACK="$BASENAME/dev/backend"

PROD_FRONT="$BASENAME/prod/backend/frontend"
DEV_FRONT="$BASENAME/dev/frontend"

# copy django apps

APPS="therapist timogen"
for app in $APPS; do
    cp -r $DEV_BACK/$app $PROD_BACK/$app
done


# the `project/` django app should not be copied fully because its
# `settings.py` a specific content for prod.

PROJECT="project"
for path in $DEV_BACK/$PROJECT/*; do
    file=${path##*/}
    if [[ $file != "settings.py" ]]; then
        cp -r $DEV_BACK/$PROJECT/$file $PROD_BACK/$PROJECT/$file
    fi
done


# Frontend

rm -rf $PROD_FRONT/dist 

cd $DEV_FRONT
npm install
npm run build
cd -


cp -r $DEV_FRONT/dist $PROD_FRONT/dist
cp $DEV_FRONT/package.json $PROD_FRONT/package.json
cp $DEV_FRONT/vue.config.js $PROD_FRONT/vue.config.js


# Cleanup

rm -rf $PROD_BACK/project/__pycache__
rm -rf $PROD_BACK/therapist/__pycache__
rm -rf $PROD_BACK/timogen/__pycache__


# Static files - this needs to be done only in the prod server

# python manage.py collectstatic
