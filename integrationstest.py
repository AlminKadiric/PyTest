def basePrice(x):
    taxesFixed=5
    return x+taxesFixed

def shippingAdded(x):
    shippingAmazon = 12
    return x+shippingAmazon

def priceTotal(x):
    return basePrice(shippingAdded(x))


def test_finalResult():
    expectedResult = 316
    result = priceTotal(299)
    assert result == expectedResult

