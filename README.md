# The-Smart-Barn
6IICT 2023-2024 eindproject

## software

- visualisatie en berekeningen met pygame
- plaatsen van graph op website
- berekeningen van graph
- sensoren uitlezen
- ventilatoren aansturen
- meer dingen

## Crontab

- Check eerst of er geen crontab aan de gang is door middel van

crontab -l

- Vervolgens voeg je een crontab toe door

crontab -e

- Hier voeg je deze commando toe:

* * * * * cd /home/rpi/Desktop/The-Smart-Barn && git add . && git commit -m "Automatic commit" && git push origin Software-gang 

- Verander het eerste stukje met jou pad van The-Smart-Barn




## Crontab

- Check eerst of er geen crontab aan de gang is door middel van

crontab -l

- Vervolgens voeg je een crontab toe door

crontab -e

- Hier voeg je deze commando toe:

* * * * * cd /home/rpi/Desktop/The-Smart-Barn && git add . && git commit -m "Automatic commit" && git push origin Software-gang 

- Verander het eerste stukje met jou pad van The-Smart-Barn




## Instructies push-crontab vanuit RPi.

### Crontab instructies
1. open crontab editor
crontab -e
2. Voeg onderstaand commando toe. Controleer locatie van Smartbarn-map.


### Overige instructies
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
* * * * * cd /home/rpi/Desktop/The-Smart-Barn && git add . && git commit -m "Automatic commit" && git push origin Software-gang
