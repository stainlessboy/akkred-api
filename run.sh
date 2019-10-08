#!/usr/bin/env bash

export PATH=$PATH:/usr/pgsql-11/bin:/usr/local/bin
export ENVIRONMENT=~/akkred
export API_ROOT="$( cd -P "$( dirname ${BASH_SOURCE[0]} )" && pwd )"
source ${API_ROOT}/.venv/bin/activate


cd ${API_ROOT}
source ../environment
${API_ROOT}/.venv/bin/uwsgi --ini ${API_ROOT}/uwsgi.ini
