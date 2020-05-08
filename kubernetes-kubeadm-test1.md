How do I install Kubernetes?

# First is Install the Tools

first the tools - [...tools/install-kubectl/](https://kubernetes.io/docs/tasks/tools/install-kubectl/)


## Install kubectl binary with curl on Linux
Option 1.
```
grep -E --color 'vmx|svm' /proc/cpuinfo

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
























.
