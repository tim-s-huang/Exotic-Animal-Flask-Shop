from flask import Blueprint, Flask, render_template, request
import re
import sqlite3

pages = Blueprint('pages', __name__)

capyDescrip = '''The world's largest rodent, this oversized guinea pig is a great pet for all ages'''
gatorDescrip = '''Growing up to 14 feet long, this unique reptile is for more adventerous owners'''
chimpDescrip = '''This highly intelligent and social pet sure to become a beloved family member'''
dilloDescrip = '''Charming and adorable, this exotic animal is fantastic for its low-maintenance'''
bearDescrip = '''One of the largest carnivores on earth, this magnificent pet is only for the brave'''
uniDescrip = '''Thought to be a myth, the ultimate fantasy creature is our finest pet available'''

def create_db():
    ## SQL - Products

    productconnect = sqlite3.connect('products.db')
    productcursor = productconnect.cursor()
    productcursor.execute('DROP TABLE IF EXISTS products')

    #Create products table
    productcursor.execute('CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, image TEXT, price REAL, EI TEXT)')                   

    #Add products
    productcursor.execute('INSERT INTO products (name, description, image, price, EI) VALUES (?, ?, ?, ?, ?)', ("Capybara", capyDescrip, 'static/capybara.jpg', '89.99', 'Enviromental Impact: 1/5 (Least Concern)'))
    productcursor.execute('INSERT INTO products (name, description, image, price, EI) VALUES (?, ?, ?, ?, ?)', ("Alligator", gatorDescrip, 'static/alligator.jpg', '174.99', 'Enviromental Impact: 2/5 (Threatened)'))
    productcursor.execute('INSERT INTO products (name, description, image, price, EI) VALUES (?, ?, ?, ?, ?)', ("Chimpanzee", chimpDescrip, 'static/chimp.jpg', '249.99', 'Enviromental Impact: 4/5 (Endangered)'))
    productcursor.execute('INSERT INTO products (name, description, image, price, EI) VALUES (?, ?, ?, ?, ?)', ("Armadillo", dilloDescrip, 'static/armadillo.jpg', '119.99', 'Enviromental Impact: 2/5 (Threatened)'))
    productcursor.execute('INSERT INTO products (name, description, image, price, EI) VALUES (?, ?, ?, ?, ?)', ("Polar Bear", bearDescrip, 'static/bear.jpg', '349.99', 'Enviromental Impact: 3/5 (Vunerable)'))
    productcursor.execute('INSERT INTO products (name, description, image, price, EI) VALUES (?, ?, ?, ?, ?)', ("Unicorn", uniDescrip, 'static/unicorn.jpg', '999.99', 'Enviromental Impact: 5/5 (Extinct?)'))

    productconnect.commit()
    productconnect.close()

    ## SQL - Basket
    basketconnect = sqlite3.connect('basket.db')
    basketcursor = basketconnect.cursor()

    #Remove existing basket
    basketcursor.execute('DROP TABLE IF EXISTS basket')

    #Create basket table
    basketcursor.execute('CREATE TABLE basket (itemid INTEGER, item TEXT, price REAL, quantity INTEGER DEFAULT 0)')

    basketconnect.commit()
    basketconnect.close()
    
create_db()

def purchase():
    homeconnect = sqlite3.connect('products.db')
    homecursor = homeconnect.cursor()
    
    productID = request.form['product-id']
    
    basketproduct = []
    
    homecursor.execute("SELECT id, name, price FROM products WHERE id = ?", (productID,))
    fetch = homecursor.fetchone()
    
    basketproduct = list(fetch)
    
    homeconnect.commit()
    homeconnect.close()
    
    basketconnect = sqlite3.connect('basket.db')
    basketcursor = basketconnect.cursor()
    
    basketcursor.execute("SELECT * FROM basket where itemid = ?", (basketproduct[0],))
    itemFound = basketcursor.fetchone()

    if itemFound is None:
        basketcursor.execute('INSERT INTO basket (itemid, item, price) VALUES (?, ?, ?)', tuple(basketproduct)) 
        basketcursor.execute('UPDATE basket SET quantity = 1 WHERE itemid = ?', (basketproduct[0],))

    else:
        basketcursor.execute('UPDATE basket SET quantity = quantity + 1 WHERE itemid = ?', (basketproduct[0],))

    basketconnect.commit()
    basketconnect.close()
    
def calcTotal():
    basketconnect = sqlite3.connect('basket.db')
    basketcursor = basketconnect.cursor()
    
    priceList = [price[0] for price in basketcursor.execute("SELECT price FROM basket")]
    quantList = [quantity[0] for quantity in basketcursor.execute("SELECT quantity FROM basket")]
    
    totalPrice = 0
    
    for i in range (0, len(priceList)):
        totalPrice = totalPrice + (priceList[i]*quantList[i])
        
    basketconnect.commit()
    basketconnect.close()
    
    totalPrice = round(totalPrice, 2)
    
    return totalPrice

def removeItem():
    basketconnect = sqlite3.connect('basket.db')
    basketcursor = basketconnect.cursor()
    
    productID = request.form['product-id']
    
    basketcursor.execute("SELECT quantity from basket WHERE itemid = ?", (productID,))
    removalQuant = basketcursor.fetchone()
    
    if removalQuant == None:
        pass
    elif removalQuant[0] == 1:
        basketcursor.execute("DELETE from basket WHERE itemid = ?", (productID,))
    else:
        basketcursor.execute('UPDATE basket SET quantity = quantity - 1 WHERE itemid = ?', (productID,))
        
    basketconnect.commit()
    basketconnect.close()

## WEBSITE
@pages.route('/', methods=['GET', 'POST'])
def home(): 
    
    if request.method == 'POST':
        purchase()
    
    homeconnect = sqlite3.connect('products.db')
    homecursor = homeconnect.cursor()
    
    homecursor.execute("SELECT * FROM products")
    data = homecursor.fetchall()
    
    homeconnect.commit()
    homeconnect.close()
    
    products = []
    
    for row in data:
        products.append(list(row))
    
    return render_template("home.html", products=products)

@pages.route('/capybara', methods=['GET', 'POST'])
def capybara():
    
    if request.method == 'POST':
        purchase()
        
    return render_template("capybara.html")

@pages.route('/alligator', methods=['GET', 'POST'])
def alligator():
    
    if request.method == 'POST':
        purchase()
        
    return render_template("alligator.html")

@pages.route('/chimp', methods=['GET', 'POST'])
def chimp():
    
    if request.method == 'POST':
        purchase()
        
    return render_template("chimp.html")

@pages.route('/armadillo', methods=['GET', 'POST'])
def armadillo():
    
    if request.method == 'POST':
        purchase()
        
    return render_template("armadillo.html")

@pages.route('/bear', methods=['GET', 'POST'])
def bear():
    
    if request.method == 'POST':
        purchase()
        
    return render_template("bear.html")

@pages.route('/unicorn', methods=['GET', 'POST'])
def unicorn():
    
    if request.method == 'POST':
        purchase()
        
    return render_template("unicorn.html")

@pages.route('/basket', methods=['GET', 'POST'])
def basket():
    
    if request.method == 'POST':
        removeItem()
    
    basketconnect = sqlite3.connect('basket.db')
    basketcursor = basketconnect.cursor()
    
    basketcursor.execute('SELECT * FROM basket')
    data = basketcursor.fetchall()
   
    basket = []
    
    for row in data:
        basket.append(list(row))
        
    basketconnect.commit()
    basketconnect.close()
    
    total = calcTotal()
    
    return render_template("basket.html", basket=basket, total=total)


@pages.route('/checkout')
def checkout():
    total = calcTotal()
    return render_template('checkout.html', total=total)
    
@pages.route('/success')
def success():
    return render_template("success.html")

@pages.route('/cardNoValid', methods=['POST'])
def cardNoVaild():
    total = calcTotal()
    cardNum = request.form['cardNo']
    cardNum = re.sub('\D', '', cardNum)
    validCardNo = cardNum.replace("-","").replace(" ","")
    if len(validCardNo) == 16:
        return render_template('success.html')
    else:
        return render_template('checkout.html', validCard=False, total=total)
    
@pages.route('/addBasket', methods=['POST'])
def addBasket():
    item_name = request.form['item_id']
    item_price = request.form['item_price']
