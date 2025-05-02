#!/bin/sh
# wait-for-db.sh

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

until nc -z "$host" "$port"; do
  echo "PostgreSQL não está disponível - aguardando ($host:$port)..."
  sleep 2
done

echo "PostgreSQL está pronto! Executando: $cmd"
exec $cmd