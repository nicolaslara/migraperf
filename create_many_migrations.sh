#!/usr/bin/env bash
for i in `seq $1`
do
cp inheritchains/models.tmpl.1 inheritchains/models.py
time ./manage.py makemigrations
cp inheritchains/models.tmpl.2 inheritchains/models.py
time ./manage.py makemigrations
done
