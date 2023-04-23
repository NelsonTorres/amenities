variable "POSTGRESQL_PASSWORD" {
  type    = string
}

resource "kubernetes_secret" "postgresql-secrets" {
  metadata {
    name = "postgresql-secrets"
    namespace = amenities
  }

  data = {
    POSTGRESQL_DATABASE="postgres" 
    POSTGRESQL_USER="postgres" 
    POSTGRESQL_HOST="127.0.0.1"
    POSTGRESQL_PORT=5432
    POSTGRESQL_PASSWORD=var.POSTGRESQL_PASSWORD
  }

  type = "kubernetes.io/generic"
}

