
.PHONY: login/postgres
login/postgres:
	PGPASSWORD=$(kubectl get secret --namespace amenities database-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d) psql --host 127.0.0.1 -U postgres -d postgres -p 5432



requirements.txt:
	poetry export --without-hashes --format=requirements.txt > src/requirements.txt

.PHONY: docker/build
docker/build: requirements.txt
	docker build -t save-amenities:latest src/

.PHONY: docker/run
docker/run:
	docker run save-amenities