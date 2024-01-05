import json
    
# GET /cryptoCurrencies
def test_characters_page(client):
    response = client.get("/cryptocurrencies")
    assert response.status_code == 200
    data = json.loads(response.data)
 
    assert data['id'] == 1
    assert data['name'] == 'Bitcoin'
    assert data['inventor_name'] == 'Satoshi Nakamoto'
    assert data['greatest_of_all_time_price'] == '$67.566'
    assert data['launch_date'] == '3rd of January 2009'
    assert data['id'] == 1
    assert data['name'] == 'Bitcoin'
    assert data['inventor_name'] == 'Satoshi Nakamoto'
    assert data['greatest_of_all_time_price'] == '$67.566'
    assert data['launch_date'] == '3rd of January 2009'
    
# GET/:id cryptoCurrencies
def test_cryptoCurrency_page(client):
    response = client.get('/cryptoCurrencies/1')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    print(data)
    assert len(data) == 5
    assert data['id'] == 1
    assert data['name'] == 'Bitcoin'
    assert data['inventor_name'] == 'Satoshi Nakamoto'
    assert data['greatest_of_all_time_price'] == '$67.566'
    assert data['launch_date'] == '3rd of January 2009'

