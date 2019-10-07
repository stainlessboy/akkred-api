#!/usr/bin/env bash

export PATH=$PATH:/usr/pgsql-11/bin:/usr/local/bin
export PROJECT_ROOT=$(pwd)
source ${PROJECT_ROOT}/.venv/bin/activate

cd ${PROJECT_ROOT}

case $1 in
    service)
        source ../environment
        ${PROJECT_ROOT}/.venv/bin/uwsgi --ini ${PROJECT_ROOT}/uwsgi.ini
        ;;
    test2)
        source ~/test_environment
        ${PROJECT_ROOT}/.venv/bin/uwsgi --ini ${PROJECT_ROOT}/test2.ini
        ;;
    test3)
        source ~/test3
        ${PROJECT_ROOT}/.venv/bin/uwsgi --ini ${PROJECT_ROOT}/test3.ini
        ;;
    test4)
        source ~/test4
        ${PROJECT_ROOT}/.venv/bin/uwsgi --ini ${PROJECT_ROOT}/test4.ini
        ;;
    worker)
        source ~/environment
        ${PROJECT_ROOT}/.venv/bin/celery -A crowtech worker --loglevel=INFO --concurrency=10
        ;;
    beat)
        source ~/environment
        ${PROJECT_ROOT}/.venv/bin/celery -A crowtech beat
        ;;
    telegram)
        source ~/environment
        python ${PROJECT_ROOT}/manage.py telegram
        ;;
    notify_application)
        source ~/environment
        python ${PROJECT_ROOT}/manage.py notify_application
        ;;
    clear_skills)
        source ~/environment
        python ${PROJECT_ROOT}/manage.py clear_skills
        ;;
esac
