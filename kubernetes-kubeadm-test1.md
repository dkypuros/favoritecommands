How do I install Kubernetes?

# First is Install the Tools

first the tools - [...tools/install-kubectl/](https://kubernetes.io/docs/tasks/tools/install-kubectl/)


## Install kubectl binary with curl on Linux
Option 1.
```
cd ~/

curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl

chmod +x kubectl

sudo mv ./kubectl /usr/local/bin/kubectl

kubectl version --client

```

## Install using native package management (look like another option all together)

Ubuntu, Debian, or HypriotOS or CentOS, RHEL, Fedora (Q: Does RH support this?)

Try Ubuntu First. (Q: What version of Ubuntu is tested here?)
(Q:Does google support the apt package?)
```
sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update -y
sudo apt-get install -y kubectl

...cli output...
"v1.18.2"

```



## Verifying kubectl configuration


```
~/.kube/config # created automatically when you create a cluster
kubectl cluster-info
kubectl cluster-info dump
```


## Optional kubectl configurations
It just assumes Ubuntu (nvmd, it's dug in the instructions.)

```
sudo apt-get install bash-completion
ls /usr/share/bash-completion/bash_completion
cat /usr/share/bash-completion/bash_completion
~/.bashrc # didn't work.
# source /usr/share/bash-completion/bash_completion   //Didn't seem to need this.
# ...close shell / reload...
type _init_completion # spit out a script. I guess that's good?
```

Enable kubectl autocompletion

```
echo 'source <(kubectl completion bash)' >>~/.bashrc
vim ~/.bashrc
# add this to the very end of the script "source <(kubectl completion bash)"
```



# Second install minikube
KVM note, but no KVM test instructions.
```
grep -E --color 'vmx|svm' /proc/cpuinfo
```

[Found this KVM Cosmic (18.10) Test](https://help.ubuntu.com/community/KVM/Installation)
[Test system is Bionic (18.04 LTS)]
```
sudo apt-get install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
whoami
systemctl status libvirtd
sudo adduser `id -un` libvirt
The user `MYNAMEHERE' is already a member of `libvirt'.
#test
virsh list --all
#bonus GUI
sudo apt-get install virt-manager
#Open the "Virtualization Manager"  - look for errors.

#Error
Verify that the "libvirtd" daemon is running.
systemctl enable libvirtd
systemctl start libvirtd

#[TROUBLESHOOTING](https://askubuntu.com/questions/345218/virt-manager-cant-connect-to-libvirt)
ps ax | grep libvirt
ls -l /var/run/libvirt/libvirt-sock

minikube --help
minkube version #minikube version: v1.9.2
virt-host-validate
sudo virsh net-list --all
minikube start -v=8 --alsologtostderr --vm-driver=kvm2
libvirtd --version

MESSAGE: QEMU: Checking if device /dev/kvm exists : FAIL (Check that the 'kvm-intel' or 'kvm-amd' modules are loaded & the BIOS has enabled virtualization)

Forgot to add user to "libvirt" and "kvm" see below:
$ sudo adduser `id -un` libvirt
The user `dkypuros' is already a member of `libvirt'.
$ sudo adduser `id -un` kvm
Adding user `dkypuros' to group `kvm' ...
Adding user dkypuros to group kvm
Done.

Still ERROR: KVM2_NO_DOMAIN

Trying this
minikube delete

```






Install Minikube using a package

```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube

sudo mkdir -p /usr/local/bin/
sudo install minikube /usr/local/bin/
```


# Third Confirm Installation of both a hypervisor and Minikube

```
# Specifying the VM driver
[KVM](https://minikube.sigs.k8s.io/docs/drivers/kvm2/) - for libvirt v1.3.1 or higher
systemctl status libvirtd #Look for version.
#version 2.79

#Example: minikube start --driver=<driver_name>
# Targeting = kvm2

cd ~/
minikube start --driver=kvm2                  #permission error


```

# Next - Minikube commands - Configuring Kubernetes

```
minikube start --driver=kvm2 --extra-config

#Examples:
#change the MaxPods setting to 5 on the Kubelet
minikube start --driver=kvm2 --extra-config=kubelet.MaxPods=5

#set the AuthorizationMode on the apiserver to RBAC
minikube start --driver=kvm2 --extra-config=apiserver.authorization-mode=RBAC

minikube stop

minikube delete

#minikube automatically sets context for kubectl, you reset it.
kubectl config use-context minikube

#dashboard
minikube dashboard

#docs
[Docs](Documentation: https://minikube.sigs.k8s.io/docs/reference/drivers/kvm2/)
```

Try a few kubectl commands.
```

[Here are some sample app Docs](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/)

#Deployment yaml
[kubectl apply -f https://k8s.io/examples/service/access/hello-application.yaml](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/#creating-a-service-for-an-application-running-in-two-pods)

...cli ouput...
deployment.apps/hello-world created

#deployments
kubectl get deployments hello-world
kubectl describe deployments hello-world

#Service
kubectl expose deployment hello-world --type=NodePort --name=example-service
...cli output...
service/example-service exposed
kubectl describe services example-service

...cli output...
NodePort:                 <unset>  30517/TCP

kubectl get pods --selector="run=load-balancer-example" --output=wide
...cli output...
hello-world-86d6c6f84d-kl6kj   1/1     Running   0          47m   172.17.0.7   minikube   <none>           <none>


kubectl cluster-info
...cli output...
Kubernetes master is running at https://192.168.39.88:8443
KubeDNS is running at https://192.168.39.88:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

```


Note:

[If you are using Google Compute Engine instances, you can use the gcloud compute instances list command to see the public addresses of your nodes](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/#creating-a-service-for-an-application-running-in-two-pods)

Isn't this 3rd party stuff.


curl http://172.17.0.7:30517






.
