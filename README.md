# Instructies push-crontab vanuit RPi.

## Crontab instructies
1. open crontab editor
crontab -e
2. Voeg onderstaand commando toe. Controleer locatie van Smartbarn-map.
	* * * * * cd /home/thesmartbarn/Desktop/The-Smart-Barn && git add . && git commit -m "Automatic commit [skip netlify]"  && git push origin website 
3. Controleer of commando is toegevoegd aan crontab.
crontab -l


## Overige instructies
# 1. Genereer key
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# 2. Voeg key toe aan SSH agent.
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

# 3. kopieer key naar kladblok.
cat ~/.ssh/id_rsa.pub

	--> Voeg key toe in je GitHub account under Settings>SSH.

# 4. Configure git (reeds klaar)
git config --global user.email "your_email@example.com"
git config --global user.name "Your Name"
* * * * * cd /home/thesmartbarn/Desktop/The-Smart-Barn && git add . && git commit -m "Automatic commit" && git pull origin website && git push origin website