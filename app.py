from flask import Flask, render_template

app = Flask(__name__)

# Aapke Handmade Products ka Data
PRODUCTS = [
    {
        "id": 1,
        "name": "Woven Cotton Rope Storage Basket with Premium Leather Handles",
        "category": "cotton",
        "price": "₹1799",
        "image":"cotton_storage_baske.jpg", 
        "buy_link": "https://amzn.in/d/06k1WkwX" 
    },
    {
        "id": 2,
        "name": "Handmade Jute Bag",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg", 
        "buy_link": "https://amazon.in" 
    },
    {
        "id": 3,
        "name": "Handmade Jute Bag",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg", 
        "buy_link": "https://amazon.in" 
    },
    {
        "id": 4,
        "name": "Handmade Jute Bag",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg", 
        "buy_link": "https://amazon.in" 
    },
    {
        "id": 5,
        "name": "Handmade Jute Bag",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg", 
        "buy_link": "https://amazon.in" 
    },
    {
        "id": 6,
        "name": "Handmade Jute Bag",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg", 
        "buy_link": "https://amazon.in" 
    },
    {
        "id": 7,
        "name": "Handmade Jute Bag",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg", 
        "buy_link": "https://amazon.in" 
    },
    {
        "id": 8,
        "name": "Handmade Jute Bag",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg", 
        "buy_link": "https://amazon.in" 
    },
    {
        "id": 9,
        "name": "Handmade Jute Bag",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg", 
        "buy_link": "https://amazon.in" 
    },
    {
        "id": 10,
        "name": "Handmade Jute Bag",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg", 
        "buy_link": "https://amazon.in" 
    },
    {
        "id": 11,
        "name": "Handmade Jute Bag",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg", 
        "buy_link": "https://amazon.in" 
    },
    {
        "id": 12,
        "name": "Designer Khadi Shirt",
        "category": "Cloth",
        "price": "₹899",
        "image": "khadi_shirt.jpg",
        "buy_link": "https://flipkart.com"
    }
]

@app.route("/")
def home():
    # Aapki Contact Details
    owner_info = {
        "name": "YUSUF HUSSAIN",
        "email": "yusuf@gmail.com",
        "phone": "+91 8630850116, 7037380116, 8791791004",
        "about": "We make handmade products, fancy designs of handmade creativity to decorate your home."
    }
    return render_template("shop.html", products=PRODUCTS, owner=owner_info)

if __name__ == "__main__":
    app.run(debug=True)