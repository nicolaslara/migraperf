#!/usr/bin/env bash
for i in `seq $1`
do
cp deep/models.tmpl.1 deep/models.py
./manage.py makemigrations deep
cp deep/models.tmpl.2 deep/models.py
./manage.py makemigrations deep
done