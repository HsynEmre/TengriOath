import random
import questionary
from questionary import Choice
import os

#CHARACTER
class Character():
    def __init__(self, character_name, character_weapon, character_class):
        self.character_name = character_name
        self.character_weapon = character_weapon
        self.character_class = character_class
    def pot(self, valueTotalHP,valueBoss):
        valueTotalHP += 200
        os.system("cls")
        print(f"------------------------------- \n Canınız : {valueTotalHP}  Boss canı : {valueBoss.character_hp}")
        print("iyileştirildi")
        return  valueTotalHP
    def normalAttack(self,valueBoss,valueHero,valueTotalHP):
        valueBoss.character_hp = valueBoss.character_hp - (valueHero.character_damage + valueHero.character_weapon.weapon_damage)
        valueHero.character_mana += 50
        os.system("cls")
        print(f"------------------------------- \n Canınız : {valueTotalHP}  Boss canı : {valueBoss.character_hp}")
        print(f"{valueBoss.character_name} e {valueHero.character_damage+valueHero.character_weapon.weapon_damage} hasar verildi")
        return valueHero.character_mana
    def ultiAttack(self,valueBoss,valueHero,valueTotalHP):
        valueBoss.character_hp = valueBoss.character_hp - 100
        valueHero.character_mana -= 50
        os.system("cls")
        print(f"------------------------------- \n Canınız : {valueTotalHP}  Boss canı : {valueBoss.character_hp}")
        print(f"{valueBoss.character_name} e {100} hasar verildi")
        return valueHero.character_mana

class Alp(Character):
    def __init__(self, character_name, character_weapon, character_class):
        super().__init__(character_name, character_weapon, character_class)
        self.character_hp = 100
        self.character_armor = 20
        self.character_damage = random.randint(10,20)
        self.character_range = "Yakın"
        self.character_mana = 50
    def fastAttack(self):
        pass

class Kam(Character):
    def __init__(self, character_name, character_weapon, character_class):
        super().__init__(character_name, character_weapon, character_class)
        self.character_hp = 100
        self.character_armor = 20
        self.character_damage = random.randint(10, 20)
        self.character_range = "Yakın"
        self.character_mana = 50
    def ultiAttack(self):
        pass
    def normalDefense(self):
        pass

class Alpagu(Character):
    def __init__(self, character_name, character_weapon, character_class):
        super().__init__(character_name, character_weapon, character_class)
        self.character_hp = 100
        self.character_armor = 20
        self.character_damage = random.randint(10,20)
        self.character_range = "Yakın"
        self.character_mana = 50
    def ultiAttack(self):
        pass
    def powerDefense(self):
        pass

class Mergen(Character):
    def __init__(self,character_name, character_weapon, character_class):
        super().__init__(character_name, character_weapon, character_class)
        self.character_hp = 100
        self.character_armor = 20
        self.character_damage = random.randint(10,20)
        self.character_range = "Yakın"
        self.character_mana = 50
    def fastAttack(self):
        pass
    def ultiAttack(self):
        pass
    def normalDefense(self):
        pass
class Boss(Character):
    def __init__(self, character_name, character_weapon, character_class, character_hp):
        super().__init__(character_name,character_weapon, character_class)
        self.character_hp = character_hp
        self.character_armor = 0
        self.character_damage = random.randint(20,30)
        self.character_range = "Yakun"
        self.character_mana = 50



#WEAPON
class Weapon():
    def __init__(self, weapon_name, weapon_damage, weapon_rarity):
        self.weapon_name = weapon_name
        self.weapon_damage = weapon_damage
        self.weapon_rarity = weapon_rarity

class Sword(Weapon):
    def __init__(self, weapon_name, weapon_damage, weapon_rarity):
        super().__init__(weapon_name,weapon_damage,weapon_rarity)
class Longsword(Weapon):
    def __init__(self, weapon_name, weapon_damage, weapon_rarity):
        super().__init__(weapon_name,weapon_damage,weapon_rarity)
class Firewand(Weapon):
    def __init__(self, weapon_name, weapon_damage, weapon_rarity):
        super().__init__(weapon_name,weapon_damage,weapon_rarity)
class Wand(Weapon):
    def __init__(self, weapon_name, weapon_damage, weapon_rarity):
        super().__init__(weapon_name, weapon_damage,weapon_rarity)
class Bow(Weapon):
    def __init__(self, weapon_name, weapon_damage, weapon_rarity):
        super().__init__(weapon_name, weapon_damage,weapon_rarity)
class Magicbow(Weapon):
    def __init__(self, weapon_name, weapon_damage, weapon_rarity):
        super().__init__(weapon_name,weapon_damage,weapon_rarity)
class Heavysword(Weapon):
    def __init__(self, weapon_name, weapon_damage, weapon_rarity):
        super().__init__(weapon_name,weapon_damage,weapon_rarity)
class Bun(Weapon):
    def __init__(self, weapon_name, weapon_damage, weapon_rarity):
        super().__init__(weapon_name, weapon_damage, weapon_rarity)



#DEFINITION
sword = Sword("sword",50,0)
longsword = Longsword("longsword",0,0)
firewand = Firewand("firewand",0,0)
wand = Wand("wand",0,0)
bow = Bow("bow",0,0)
magicbow = Magicbow("magicbow",0,0)
heavysword = Heavysword("heavysword",0,0)
bun = Bun("bun",0,0)

#BOSS DEFINITION
fireBoss = Boss("fireboss",sword,"boss",200)
skullBoss = Boss("skullboss",sword,"boss",280)
finalBoss = Boss("finalboss",sword,"boss",400)


fireDungeon_status = 0
skullDungeon_status = 0
finalBoss_status = 0

#MENU
hero = None
def mainMenu():
    value = questionary.select("",choices=["🎮 Oyna","🧙 Karakter","📖 Yardım","⚙️  Ayarlar","🚪 Çıkış"],qmark="",instruction=" ").ask()
    os.system("cls")
    global hero
    if value == "🎮 Oyna":
        if hero is None:
            print("Önce karakter oluşturun")
        else:
            gameMenu(hero)
    elif value == "🧙 Karakter":
        hero = characterMenu()
    elif value == "📖 Yardım":
        helpMenu()
    elif value == "⚙️  Ayarlar":
        settingMenu()
    elif value == "🚪 Çıkış":
        raise SystemExit

def gameMenu(hero):
    while True:
        valueDungeon = questionary.select("",choices=["🔥 Ateş Zindanı","💀 Kafatası Zindanı","🗺️  İlerle"],qmark="",instruction=" ").ask()
        if valueDungeon == "🔥 Ateş Zindanı":
            if fireDungeon_status == 1:
                print("Ateş zindanını tamamladınız")
                input("")
                os.system("cls")
            else:
                fireDungeon(hero)
        if valueDungeon == "💀 Kafatası Zindanı":
            if skullDungeon_status == 1:
                print("Kafatası zindanını tamamladınız")
                input("")
                os.system("cls")
            else:
                skullDungeon(hero)
        if valueDungeon == "🗺️  İlerle":
            if skullDungeon_status == 1 and fireDungeon_status == 1:
                print("İlerliyorsunuz")
                input("")
                print("Finall Zindanına geldiniz savasmak ıcın tıklayınız...")
                input("")
                finalDungeon(hero)
            else:
                print("Zindanları tamamlayınız2")
def fireDungeon(hero):
    print("------------------------------- \n Boss Görüldü : Ateşin Tanrısı")
    input("")
    os.system("cls")
    global fireDungeon_status
    hero_totalHP = hero.character_hp + hero.character_armor
    while True:
        print(f"------------------------------- \n Canınız : {hero_totalHP}  Boss canı : {fireBoss.character_hp}")
        valueFight = questionary.select("İşlem",choices=["⚔️ Saldır","❤️ İyileş", Choice("🔥 Ulti",disabled="Mana yetersiz" if hero.character_mana<100 else None)],qmark="",instruction=" ").ask()
        if valueFight == "⚔️ Saldır":
            hero.character_mana = hero.normalAttack(fireBoss,hero,hero_totalHP)
        if valueFight == "❤️ İyileş":
            hero_totalHP = hero.pot(hero_totalHP,fireBoss)
        if valueFight == "🔥 Ulti":
            hero.character_mana = hero.ultiAttack(fireBoss,hero,hero_totalHP)
        input("")
        os.system("cls")
        if fireBoss.character_hp <= 0:
            print("🏆 Zafer!")
            fireDungeon_status = 1
            return
        print("Ateş Tanrısı saldırıyor")
        input("")
        hero_totalHP -= fireBoss.character_damage
        print(f"{fireBoss.character_name} size {fireBoss.character_damage} kadar hasar verdi")
        input("")
        os.system("cls")
        if hero_totalHP <= 0:
            print("💀 Yenildin!")
            return
        os.system("cls")
def skullDungeon(hero):
    print("------------------------------- \n Boss Görüldü : Kafatası Tanrısı")
    input("")
    global skullDungeon_status
    hero_totalHP = hero.character_hp + hero.character_armor
    while True:
        print(f"------------------------------- \n Canınız : {hero_totalHP} Boss canı : {skullBoss.character_hp}")
        valueFight = questionary.select("",choices=["⚔️ Saldır","❤️ İyileş",Choice("🔥 Ulti",disabled="Mana yetersiz" if hero.character_mana<100 else None)],qmark="",instruction=" ").ask()
        if valueFight == "⚔️ Saldır":
            hero.character_mana = hero.normalAttack(skullBoss,hero,hero_totalHP)
        if valueFight == "❤️ İyileş":
            hero_totalHP = hero.pot(hero_totalHP,skullBoss)
        if valueFight == "🔥 Ulti":
            hero.character_mana = hero.ultiAttack(skullBoss,hero,hero_totalHP)
        input("")
        os.system("cls")
        if skullBoss.character_hp <= 0:
            print("🏆 Zafer!")
            skullDungeon_status = 1
            return
        print("Kafatası Tanrısı saldırıyor")
        input("")
        hero_totalHP -= skullBoss.character_damage
        print(f"{fireBoss.character_name} size {fireBoss.character_damage} kadar hasar verdi")
        input("")
        os.system("cls")
        if hero_totalHP <= 0:
            print("💀 Yenildin!")
            return
        os.system("cls")

def finalDungeon(hero):
    print("------------------------------- \n Boss Görüldü : Final Tanrısı")
    input("")
    global finalBoss_status
    global mana
    hero_totalHP = hero.character_hp + hero.character_armor
    while True:
        print(f"------------------------------- \n Canınız : {hero_totalHP} Boss canı : {finalBoss.character_hp}")
        valueFight = questionary.select("",choices=["⚔️ Saldır","❤️ İyileş",Choice("🔥 Ulti",disabled="Mana yetersiz" if hero.character_mana<100 else None)],qmark="",instruction=" ").ask()
        if valueFight == "⚔️ Saldır":
            hero.character_mana = hero.normalAttack(finalBoss, hero, hero_totalHP)
        if valueFight == "❤️ İyileş":
            hero_totalHP = hero.pot(hero_totalHP,finalBoss)
        if valueFight == "🔥 Ulti":
            hero.character_mana = hero.ultiAttack(finalBoss,hero,hero_totalHP)
        input("")
        os.system("cls")
        if finalBoss.character_hp <= 0:
            print("🏆 Zafer!")
            finalBoss_status = 1
            return
        print("Ateş Tanrısı saldırıyor")
        input("")
        hero_totalHP -= finalBoss.character_damage
        print(f"{fireBoss.character_name} size {fireBoss.character_damage} kadar hasar verdi")
        input("")
        os.system("cls")
        if hero_totalHP <= 0:
            print("💀 Yenildin!")
            return
        os.system("cls")

def characterMenu(value = ""):
    #DEFINITION
    print("-------------------------------")
    valueName = input("👤 Kahramanına isim ver: ")
    print("-------------------------------")
    valueClass = questionary.select("Sınıf Seçiniz",choices=["⚔️  Alp","🔥 Alpagu","🔮 Kam","🏹 Mergen"],qmark="",instruction=" ").ask()
    valueCharacter = None
    if valueClass == "⚔️  Alp":
        valueSword = questionary.select("Silahınızı Seçiniz",choices=["🗡️ Kılıç","⚔️ Büyük Kılıç"],qmark="",instruction=" ").ask()
        if valueSword == "🗡️ Kılıç":
            alpCharacter = Alp(valueName,sword,"")
            valueCharacter = alpCharacter
        elif valueSword == "⚔️ Büyük Kılıç":
            alpCharacter = Alp(valueName,longsword,"")
            valueCharacter = alpCharacter
    elif valueClass == "🔥 Alpagu":
        valueBun = questionary.select("Silahınızı Seçiniz",choices=["🔨 Topuz","🪓 Ağır Kılıç"],qmark="",instruction=" ").ask()
        if valueBun == "🔨 Topuz":
            alpaguCharacter = Alp(valueName,bun,"")
            valueCharacter = alpaguCharacter
        if valueBun == "🪓 Ağır Kılıç":
            alpaguCharacter = Alp(valueName,heavysword,"")
            valueCharacter = alpaguCharacter
    elif valueClass == "🔮 Kam":
        valueWand = questionary.select("Silahınızı Seçiniz",choices=["🪄 Asa","⚡ Yıldırım"],qmark="",instruction=" ").ask()
        if valueWand == "🪄 Asa":
            kamCharacter = Kam(valueName,wand,"")
            valueCharacter = kamCharacter
        if valueWand == "⚡ Yıldırım":
            kamCharacter = Kam(valueName,firewand,"")
            valueCharacter = kamCharacter
    elif valueClass == "🏹 Mergen":
        valueWand = questionary.select("Silahınızı Seçiniz",choices=["🏹 Yay","✨ Büyülü Yay"],qmark="",instruction=" ").ask()
        if valueWand == "🏹 Yay":
            mergenCharacter = Kam(valueName,bow,"")
            valueCharacter = mergenCharacter
        if valueWand == "✨ Büyülü Yay":
            mergenCharacter = Kam(valueName,magicbow,"")
            valueCharacter = mergenCharacter
    input("")
    os.system("cls")
    print(f"👤Karakter : {valueCharacter.character_name}")
    print(f"⚔️ Sınıf : {valueCharacter.character_class}")
    print(f"❤️ Can : {valueCharacter.character_hp}")
    print(f"🛡️ Zırh : {valueCharacter.character_armor}")
    print(f"💥Hasar : {valueCharacter.character_damage}")
    print(f"🗡️ Silah : {valueCharacter.character_weapon.weapon_name}")
    print(f"🏹Menzil : {valueCharacter.character_range}")
    input("")


    return valueCharacter


def helpMenu(value = ""):
    print("Tengri Oath Prototype 1.0")
    input("")
def settingMenu(value = ""):
    print("Henüz aktif değil")
    input("")


#CODE
while True:
    os.system("cls")
    mainMenu()



