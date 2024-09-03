#IF Database Cannot Remove
SELECT pid, usename, application_name, client_addr, backend_start
FROM pg_stat_activity
WHERE datname = '[database name]';

SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = '[database name]'
  AND pid <> pg_backend_pid();
 
DROP DATABASE [database name];

#Error Symbol not found: _PQbackendPID
https://gist.github.com/peter-gy/0ebe072acb9065944ecb04d95a4c3096