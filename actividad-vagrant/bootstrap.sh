#!/usr/bin/env bash

# Actualizo el manejador de paquetes
apt-get -q update

# Instalo nodejs v16.x por compatibilidad y npm
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash - &&\
sudo apt-get -q install -y nodejs

# Instalo git
sudo apt -q install git-all

# Instalo el web server Apache
apt-get -q install -y apache2

# Si no existe la carpeta myresume en /vagrant, clono el repositorio
if [ ! -d "./ariadna18.gitlab.io" ]; then
    git clone https://gitlab.com/ariadna18/ariadna18.gitlab.io.git
fi

# Actualizo el repositorio local
cd ariadna18.gitlab.io
git pull origin main
sudo npm i
sudo npm audit fix
sudo npm run resume export index.html

if ! [ -L /var/www/html ]; then
    rm -rf /var/www/html
    ln -fs /home/vagrant/ariadna18.gitlab.io /var/www/html
fi
