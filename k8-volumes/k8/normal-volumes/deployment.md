### Apply the deployment
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
### Run service in minikube  
`minikube service story-service`

### Delete the deployment
```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```
