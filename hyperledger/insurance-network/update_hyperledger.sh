# - update version

composer archive create -t dir -n .
composer network install -a insurance-network\@0.0.10.bna -c PeerAdmin@hlfv1
composer network upgrade -c PeerAdmin@hlfv1 -n insurance-network -V 0.0.10
composer-rest-server -c admin@insurance-network -n never -w true