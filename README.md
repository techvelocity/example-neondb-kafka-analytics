# neondb-kafka-analytics

```
minikube start
minikube addons enable kong
minikube tunnel
```

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-kafka bitnami/kafka --version 23.0.0
```

```
helm template . -f values.yaml | kubectl apply -f -
```

