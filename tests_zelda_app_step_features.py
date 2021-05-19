import pytest
import requests

from pytest_bdd import scenarios, when, then

ZELDA_INFO_WEBSITE = "https://www.zeldadungeon.net/wiki/"
ZELDA_API = "https://botw-compendium.herokuapp.com/api/v2/entry/"

scenarios("../zelda_app.feature", example_converters=dict(enemy_name=str, this_enemy=str, enemy_id=int, image_id=int))


@pytest.fixture
@when('the user click on the link of "<enemy_name>"')
def name_result(enemy_name):
    params = {'format': 'json'}
    name = requests.get(ZELDA_INFO_WEBSITE + enemy_name, params=params)
    return name


@then('The information page about "<this_enemy>" should display')
def compare_name(name_result, this_enemy):
    assert name_result == this_enemy


@when('User want to know about this "<enemy>"')
def id_result(enemy_id):
    params = {'format': 'json'}
    the_id = requests.get(ZELDA_API + enemy_id, params=params)
    return the_id


@then('The user should click the link under this "<image_id>" from the zelda api')
def compare_img_id(id_result, image_id):
    assert id_result == image_id
