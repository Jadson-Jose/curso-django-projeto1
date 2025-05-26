#!/bin/sh

host="$1"
port="$2"
shift 2  # Remove os dois primeiros parâmetros (host e porta)
command="$@"

until pg_isready -h "$host" -p "$port" -U jadson -d dbname; do
  echo "PostgreSQL não está disponível - aguardando ($host:$port)..."
  sleep 2
done

echo "PostgreSQL pronto! Executando comando: $command"
exec $command