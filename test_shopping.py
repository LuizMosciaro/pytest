from shopping import ShoppingCart
import pytest

#Fixtures = Faz nao ser preciso instanciar o objeto/classe/configuracoes individualmente
@pytest.fixture
def cart():
    #Todas configuracoes vêm aqui etc...
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    #cart = ShoppingCart(3)
    cart.add('Apple')
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item(cart):
    #cart = ShoppingCart(2)
    cart.add('Apple')
    assert 'Apple' in cart.get_items()

def test_when_add_more_than_max_items_to_list(cart):
    #cart = ShoppingCart(5)
    for _ in range(5):
        cart.add('Apple')
    
    with pytest.raises(OverflowError):
        cart.add('Banana')

def test_can_get_total_price(cart):
    #cart = ShoppingCart(5)
    cart.add('Apple')
    cart.add('Banana')

    price_map = {'Apple':1.50,'Banana':2.00}
    assert cart.get_total_price(price_map) == 3.50

def test_can_list_all_items(cart):
    cart.add("A")
    cart.add("B")
    cart.add("C")
    assert ['A','B','C'] == cart.get_items()
