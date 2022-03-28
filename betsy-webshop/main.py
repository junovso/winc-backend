__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from decimal import Decimal
import peewee

def main():
    pass

def insert_test_data():
    queries = (
        'INSERT INTO "main"."user" ("name", "address", "zipcode", "city", "state", "country", "billing_name", "billing_account", "username", "password") VALUES("Juno", "teststraat 17", "1111XX", "Venlo", "", "Netherlands", "J.J.H van Som", "298484327", "junovso", "wachtwoord");',
        'INSERT INTO "main"."product" ("name", "description", "price_per_unit", "quantity_in_stock") VALUES("Apple", "Golden Apple", "1.50", "10");',
        'INSERT INTO "main"."product" ("name", "description", "price_per_unit", "quantity_in_stock") VALUES("Pear", "Green Pear", "1.00", "3");',
        'INSERT INTO "main"."tag" ("name") VALUES("Apple");',
        'INSERT INTO "main"."tag" ("name") VALUES("Pear");',
        'INSERT INTO "main"."tag" ("name") VALUES("Green Pear");',
        'INSERT INTO "main"."producttag" ("product_id", "tag_id") VALUES("Apple", "Golden Apple");',
        'INSERT INTO "main"."producttag" ("product_id", "tag_id") VALUES("Pear", "Green Pear");',
        'INSERT INTO "main"."producttag" ("product_id", "tag_id") VALUES("Strawberry", "Red Strawberry");',
        'INSERT INTO "main"."userproduct" ("user_id", "product_id") VALUES("juno", "Apple");',
        'INSERT INTO "main"."userproduct" ("user_id", "product_id") VALUES("juno", "Pear");'
    )
    for q in queries:
        # print('test data query: ', q)
        db.execute_sql(q)


def create_tables():
    with db:
        db.create_tables(
            [User,
             Product,
             Tag,
             Transaction,
             UserProduct,
             ProductTag
             ]
        )


def search(term):
    query = (Product
             .select()
             .where(
                 Product.name ** term | Product.description ** term)
             .order_by(Product.name)).dicts()
    # print('search: ', query)
    result = list(query.execute())
    if len(result) > 0:
        return result
    return []


def list_user_products(user_id):
    query = (Product
             .select()
             .join(UserProduct, on=(Product.name == UserProduct.product))
             .join(User, on=(User.username == UserProduct.user))
             .where(User.username == user_id)
             ).dicts()
    # print('list_user_products: ', query)
    result = list(query.execute())
    if len(result) > 0:
        return result
    return []


def list_products_per_tag(tag_id):
    query = (Product
             .select()
             .join(ProductTag, on=(Product.name == ProductTag.product))
             .join(Tag, on=(Tag.name == ProductTag.tag))
             .where(Tag.name == tag_id)
             ).dicts()
    # print('list_products_per_tag: ', query)
    result = list(query.execute())
    if len(result) > 0:
        return result
    return []


def add_product_to_catalog(user_id, product):

    Product.create(
        name=product['name'],
        description=product['description'],
        price_per_unit=product['price_per_unit'],
        quantity_in_stock=product['quantity_in_stock']
    )

    UserProduct.create(
        user=user_id,
        product=product['name']
    ).save()

    return True


def remove_product(product_id):
    query = (UserProduct
             .delete()
             .where(UserProduct.product == product_id)
             )
    # print('remove_product: ', query)
    result = query.execute()
    if result:
        return True
    return False


def update_stock(product_id, new_quantity):
    query = (Product
             .update({Product.quantity_in_stock: new_quantity})
             .where(Product.name == product_id)
             )
    # print('update_stock: ', query)
    result = query.execute()
    if result:
        return True
    return False


def purchase_product(product_id, buyer_id, quantity):
    firstQuery = (User
              .select(User.username)
              .join(UserProduct, on=(User.username == UserProduct.user))
              .join(Product, on=(Product.name == UserProduct.product))
              .where(Product.name == product_id)
              ).dicts()
    # print('purchase_product, seller:', query)
    seller = list(firstQuery.execute())

    secondQuery = (Product
              .select()
              .where(Product.name == product_id)
              ).dicts()
    # print('purchase_product, product:', query)
    product = list(secondQuery.execute())

    price_total = product[0]['price_per_unit'] * quantity

    # print(buyer_id, seller[0]['username'],
    #       product[0]['name'], quantity, price_total)

    thirdQuery = Transaction(
        buyer_id='juno',
        seller_id=seller[0]['username'],
        product_id=product[0]['name'],
        quantity=quantity,
        price_total=price_total
    )
    transaction = thirdQuery.save()
    # print('purchase_product, transaction:', query)

    new_quantity_in_stock = product[0]['quantity_in_stock'] - quantity
    update_stock(product_id, new_quantity_in_stock)

    fourthQuery = (Transaction
              .select()
              .where(Transaction.id == transaction)
              )
    # print('transaction:', query)
    result = fourthQuery.execute()
    if result:
        return True
    return False


if __name__ == '__main__':
    main()
