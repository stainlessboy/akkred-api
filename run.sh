#!/usr/bin/env bash

sudo su root
export PATH=$PATH:/usr/pgsql-1/bin:/usr/local/bin
export ENVIRONMENT=~/my_job
export API_ROOT="$( cd -P "$( dirname ${BASH_SOURCE[0]} )" && pwd )"
source ${API_ROOT}/.venv/bin/activate


cd ${API_ROOT}
source ../environment
${API_ROOT}/.venv/bin/uwsgi --ini ${API_ROOT}/uwsgi.ini
