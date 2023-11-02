#!/usr/bin/env bash

source .env

echo "Syncing directory ${local_directory:?} to ${remote_directory:?}" \
    "on ${remote_server:?} via user ${remote_user:?}"

rsync -rv \
    "${local_directory}/" \
    "${remote_user}@${remote_server}:${remote_directory}" \
    --delete-after
