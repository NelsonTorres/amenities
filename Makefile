
.PHONY: login/postgres
login/postgres:
	PGPASSWORD=$(kubectl get secret --namespace amenities database-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d) psql --host 127.0.0.1 -U postgres -d postgres -p 5432

