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
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.3/deploy/static/provider/cloud/deploy.yaml
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=nginxsvc/O=nginxsvc"
kubectl create secret tls tls-secret --key tls.key --cert tls.crt
```

```
kubectl create secret generic neondb-credentials --from-literal=password=<value>
```

```
helm template . -f values.yaml | kubectl apply -f -
```

