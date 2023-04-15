#! /bin/bash

helm repo add bitnami https://charts.bitnami.com/bitnami

helm upgrade \
    database \
    bitnami/postgresql \
    --install \
    --namespace amenities 
