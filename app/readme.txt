mongodb+srv://admin:<db_password>@shop.cqyex.mongodb.net/?retryWrites=true&w=majority&appName=shop

username : admin
password :admin


# insert products to database
products = [
    {
        "name" : "Product 1",
        "image" : "/static/images/product1.jpg",
        "price" : 5.99,
        "tag" : "new"
    },
    {
        "name" : "Product 2",
        "image" : "/static/images/product2.jpg",
        "price" : 7.99,
        "tag" : "discontinued"
    }
]


products_collection.insert_many(products)


